# Dual‑Path SNN+ANN Prototype

**Purpose:** Prototype a dual‑path neuromorphic system: event‑driven SNN on FPGA + ANN/VMM accelerator, memristor testbed integration, calibration, and HIL fine‑tuning.

## Quick start
1. Clone repo.
2. Provision hardware: FPGA dev board, memristor dev kit (or emulator), SMU/pulse generator, ADC front end.
3. Install Python deps: `pip install -r requirements.txt` (numpy, scipy, pyserial, pyvisa, matplotlib).
4. Build FPGA RTL with your toolchain (Vivado/Quartus). Example RTL in `fpga/rtl/`.
5. Run `python testbed/hil_orchestrator.py` to start HIL loop (edit config for your instruments).

## Contents
- `fpga/rtl/`: Verilog modules (LIF neuron, event router, converters, fusion).
- `firmware/`: write‑verify firmware pseudocode for memristor programming.
- `testbed/`: orchestration, calibration, and model fitting scripts.
- `tools/`: power measurement helpers.

## Goals & metrics
- Measure ANN wake frequency, energy per inference, and fusion accuracy.
- Target: reduce ANN wake duty by ≥50% while keeping fusion accuracy within 1–2% of ANN baseline.

## License
MIT
