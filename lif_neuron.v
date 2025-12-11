// Simple fixed-point LIF neuron (event-driven)
// Note: parameterize bit widths for your FPGA
module lif_neuron #(
  parameter WIDTH = 16,
  parameter THRESH = 16'h0C00 // example threshold
)(
  input clk,
  input rst,
  input spike_in,            // event input
  input signed [WIDTH-1:0] w, // synaptic weight (fixed point)
  output reg spike_out
);
  reg signed [WIDTH-1:0] v; // membrane potential
  always @(posedge clk) begin
    if (rst) begin
      v <= 0;
      spike_out <= 0;
    end else begin
      spike_out <= 0;
      if (spike_in) v <= v + w;
      // simple leak
      v <= v - (v >>> 8);
      if (v >= THRESH) begin
        spike_out <= 1;
        v <= 0;
      end
    end
  end
endmodule
