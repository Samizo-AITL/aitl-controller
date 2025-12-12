# Simulation — Minimal flow for FSM RTL

## Philosophy
We keep the simulation minimal:
- No UVM
- No constrained random
- No full regression infrastructure

But we still enforce:
- deterministic reset
- known state coverage for representative sequences
- at least one “negative test” (invalid input combination) if applicable

## Minimal tool choices (concept)
You can simulate with:
- Icarus Verilog (`iverilog`, `vvp`)
- Verilator (optional concept)

This chapter provides a minimal **Icarus-style** Makefile.

## Directory layout used in this chapter
- RTL: `code/rtl/fsm_rtl.sv`
- TB : `code/tb/tb_fsm_min.sv`
- Sim: `code/sim/Makefile`

## How to run (concept)
From `docs/chapter3/code/sim/`:

```sh
make clean
make run
make wave
