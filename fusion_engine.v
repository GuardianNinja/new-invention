// Simple confidence-based fusion: choose SNN output if confidence > threshold,
// otherwise use ANN output. Inputs are fixed-point scores.
module fusion_engine #(
  parameter WIDTH = 16
)(
  input clk, rst,
  input snn_valid,
  input signed [WIDTH-1:0] snn_score,
  input ann_valid,
  input signed [WIDTH-1:0] ann_score,
  input [7:0] snn_conf, // 0..255
  input [7:0] conf_thresh,
  output reg out_valid,
  output reg signed [WIDTH-1:0] out_score
);
  always @(posedge clk) begin
    if (rst) begin
      out_valid <= 0;
      out_score <= 0;
    end else begin
      if (snn_valid && (snn_conf >= conf_thresh)) begin
        out_valid <= 1;
        out_score <= snn_score;
      end else if (ann_valid) begin
        out_valid <= 1;
        out_score <= ann_score;
      end else begin
        out_valid <= 0;
      end
    end
  end
endmodule
