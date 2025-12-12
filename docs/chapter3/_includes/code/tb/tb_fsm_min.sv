// docs/chapter3/code/tb/tb_fsm_min.sv
// Minimal self-checking testbench for fsm_rtl.sv (concept).
// Replace sequences with those derived from your Chapter2 formal transition table.

`timescale 1ns/1ps

module tb_fsm_min;

  localparam int STATE_W = 3;

  logic clk;
  logic rst_n;

  logic in_start;
  logic in_done;
  logic in_fault;

  logic out_busy;
  logic out_error;
  logic [STATE_W-1:0] state_q;

  // DUT
  fsm_rtl #(.STATE_W(STATE_W)) dut (
    .clk      (clk),
    .rst_n    (rst_n),
    .in_start (in_start),
    .in_done  (in_done),
    .in_fault (in_fault),
    .out_busy (out_busy),
    .out_error(out_error),
    .state_q  (state_q)
  );

  // Clock: 100MHz (10ns)
  initial clk = 1'b0;
  always #5 clk = ~clk;

  // VCD
  initial begin
    $dumpfile("build/wave.vcd");
    $dumpvars(0, tb_fsm_min);
  end

  // Helpers
  task automatic apply_inputs(input logic s, input logic d, input logic f);
    // Drive on negedge to avoid race with posedge sampling
    @(negedge clk);
    in_start = s;
    in_done  = d;
    in_fault = f;
  endtask

  task automatic expect_state(input logic [STATE_W-1:0] exp, input string msg);
    @(posedge clk);
    #1;
    if (state_q !== exp) begin
      $display("FAIL: %s | state_q=%0d expected=%0d", msg, state_q, exp);
      $fatal(1);
    end else begin
      $display("PASS: %s | state_q=%0d", msg, state_q);
    end
  endtask

  task automatic expect_outputs(input logic exp_busy, input logic exp_err, input string msg);
    @(posedge clk);
    #1;
    if ((out_busy !== exp_busy) || (out_error !== exp_err)) begin
      $display("FAIL: %s | out_busy=%b exp=%b | out_error=%b exp=%b",
               msg, out_busy, exp_busy, out_error, exp_err);
      $fatal(1);
    end else begin
      $display("PASS: %s | out_busy=%b out_error=%b", msg, out_busy, out_error);
    end
  endtask

  // State encoding must match RTL localparams (keep consistent)
  localparam logic [STATE_W-1:0] S_IDLE  = 'd0;
  localparam logic [STATE_W-1:0] S_RUN   = 'd1;
  localparam logic [STATE_W-1:0] S_DONE  = 'd2;
  localparam logic [STATE_W-1:0] S_FAULT = 'd3;

  initial begin
    // Init inputs
    in_start = 1'b0;
    in_done  = 1'b0;
    in_fault = 1'b0;

    // Reset
    rst_n = 1'b0;
    repeat (3) @(posedge clk);
    rst_n = 1'b1;

    // Check reset landing
    expect_state(S_IDLE, "Reset -> IDLE");
    expect_outputs(1'b0, 1'b0, "IDLE outputs after reset");

    // Sequence 1: IDLE -> RUN -> DONE -> IDLE
    apply_inputs(1'b1, 1'b0, 1'b0); // start
    expect_state(S_RUN, "start triggers RUN");
    expect_outputs(1'b1, 1'b0, "RUN outputs");

    apply_inputs(1'b1, 1'b1, 1'b0); // done
    expect_state(S_DONE, "done triggers DONE");
    expect_outputs(1'b0, 1'b0, "DONE outputs");

    apply_inputs(1'b0, 1'b0, 1'b0); // release start
    expect_state(S_IDLE, "release start returns IDLE");
    expect_outputs(1'b0, 1'b0, "IDLE outputs");

    // Sequence 2: fault path
    apply_inputs(1'b0, 1'b0, 1'b1); // fault
    expect_state(S_FAULT, "fault triggers FAULT");
    expect_outputs(1'b0, 1'b1, "FAULT outputs");

    // Clear fault policy: fault=0 and start=0
    apply_inputs(1'b0, 1'b0, 1'b0);
    expect_state(S_IDLE, "fault cleared -> IDLE");
    expect_outputs(1'b0, 1'b0, "IDLE outputs after fault clear");

    $display("ALL TESTS PASSED");
    #20;
    $finish;
  end

endmodule
