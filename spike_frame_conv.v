// Aggregate spikes into short-window frames for ANN consumption.
// Window length parameterizable.
module spike_frame_conv #(
  parameter ADDR_WIDTH = 8,
  parameter WINDOW = 256
)(
  input clk, rst,
  input spike_valid,
  input [ADDR_WIDTH-1:0] spike_addr,
  output reg frame_ready,
  output reg [31:0] frame_hash // simple checksum/feature vector placeholder
);
  reg [15:0] counter;
  reg [31:0] acc;
  always @(posedge clk) begin
    if (rst) begin
      counter <= 0;
      acc <= 0;
      frame_ready <= 0;
    end else begin
      if (spike_valid) acc <= acc + {24'b0, spike_addr};
      counter <= counter + 1;
      if (counter == WINDOW) begin
        frame_ready <= 1;
        frame_hash <= acc;
        counter <= 0;
        acc <= 0;
      end else frame_ready <= 0;
    end
  end
endmodule
