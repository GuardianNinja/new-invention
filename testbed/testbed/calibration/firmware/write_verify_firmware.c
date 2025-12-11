// Pseudocode for write-verify programming loop.
// Target platform: microcontroller or softcore on FPGA with SPI/ADC access.

#include <stdint.h>
#include <stdbool.h>

// Configurable parameters
#define MAX_ATTEMPTS 64
#define COARSE_PULSES 4
#define FINE_PULSE_STEP 1
#define VERIFY_TOLERANCE 0.02f // relative

// Abstract hardware APIs (implement per platform)
bool apply_pulse(uint8_t row, uint8_t col, int amplitude);
float read_conductance(uint8_t row, uint8_t col);
void log_program_event(uint8_t row, uint8_t col, float g, int attempts);

bool program_cell(uint8_t row, uint8_t col, float target_g) {
    // Coarse phase
    for (int i=0;i<COARSE_PULSES;i++) {
        apply_pulse(row, col, 10); // coarse amplitude
    }
    // Fine phase with verify
    int attempts = 0;
    while (attempts < MAX_ATTEMPTS) {
        float g = read_conductance(row, col);
        float err = (g - target_g) / target_g;
        if (fabs(err) <= VERIFY_TOLERANCE) {
            log_program_event(row, col, g, attempts);
            return true;
        }
        // Decide pulse direction and amplitude adaptively
        int amp = (err < 0) ? 1 : -1; // simplistic
        apply_pulse(row, col, amp * FINE_PULSE_STEP);
        attempts++;
    }
    // Failed to program within attempts
    float g = read_conductance(row, col);
    log_program_event(row, col, g, attempts);
    return false;
}
