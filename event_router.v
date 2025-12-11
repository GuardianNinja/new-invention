// Minimal event router: accepts spike packets and routes to neuron addresses.
// Packet format (example): [addr(8) | timestamp(16) | qos(2)]
module event_router (
  input clk, rst,
  input pkt_valid,
  input [25:0] pkt_in,
  output reg route_valid,
  output reg [7:0] route_addr,
  output reg route_spike
);
  always @(posedge clk) begin
    if (rst) begin
      route_valid <= 0;
      route_addr <= 0;
      route_spike <= 0;
    end else begin
      if (pkt_valid) begin
        route_valid <= 1;
        route_addr <= pkt_in[25:18];
        route_spike <= 1;
      end else begin
        route_valid <= 0;
        route_spike <= 0;
      end
    end
  end
endmodule
