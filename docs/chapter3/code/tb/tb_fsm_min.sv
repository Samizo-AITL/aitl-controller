`timescale 1ns/1ps

module tb_fsm_min;
  logic clk = 0;
  always #5 clk = ~clk;

  logic rst_n;
  logic in_start, in_done, in_fault;
  logic out_busy, out_error;
  logic [2:0] state_q;

  fsm_rtl dut (
    .clk, .rst_n,
    .in_start, .in_done, .in_fault,
    .out_busy, .out_error,
    .state_q
  );

  initial begin
    $dumpfile("build/wave.vcd");
    $dumpvars(0, tb_fsm_min);

    rst_n = 0;
    in_start = 0; in_done = 0; in_fault = 0;
    #20 rst_n = 1;

    #10 in_start = 1;
    #10 in_done  = 1;
    #10 in_start = 0; in_done = 0;

    #10 in_fault = 1;
    #10 in_fault = 0;

    #20 $finish;
  end
endmodule
