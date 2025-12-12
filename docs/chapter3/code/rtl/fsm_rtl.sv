module fsm_rtl (
  input  logic clk,
  input  logic rst_n,
  input  logic in_start,
  input  logic in_done,
  input  logic in_fault,
  output logic out_busy,
  output logic out_error,
  output logic [2:0] state_q
);

  localparam S_IDLE  = 3'd0;
  localparam S_RUN   = 3'd1;
  localparam S_DONE  = 3'd2;
  localparam S_FAULT = 3'd3;

  logic [2:0] state_d;

  always_ff @(posedge clk or negedge rst_n) begin
    if (!rst_n)
      state_q <= S_IDLE;
    else
      state_q <= state_d;
  end

  always_comb begin
    state_d   = state_q;
    out_busy  = 1'b0;
    out_error = 1'b0;

    case (state_q)
      S_IDLE:  if (in_start) state_d = S_RUN;
      S_RUN: begin
        out_busy = 1'b1;
        if (in_fault) state_d = S_FAULT;
        else if (in_done) state_d = S_DONE;
      end
      S_DONE:  if (!in_start) state_d = S_IDLE;
      S_FAULT: begin
        out_error = 1'b1;
        if (!in_fault) state_d = S_IDLE;
      end
    endcase
  end
endmodule
