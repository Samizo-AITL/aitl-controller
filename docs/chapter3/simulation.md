---
layout: default
title: "Simulation"
nav_order: 2
parent: "Chapter 3"
---

# Simulation — Minimal FSM Verification

This document describes the **minimum simulation flow** required to verify that
the FSM RTL from Chapter 2 is behaviorally correct and structurally sane before
entering the ASIC synthesis flow.

The goal is not exhaustive verification, but confirmation that:
- reset behavior is deterministic
- representative state transitions work as specified
- outputs behave according to Moore / Mealy definitions
- the RTL is free from obvious simulation hazards

---

## 1. Role of Simulation in Chapter 3

Simulation confirms behavioral correctness.
Synthesis confirms structural feasibility.

Both are required to claim hardware realism.

---

## 2. Simulation Scope

Included:
- Clock and reset verification
- Representative state transition checks
- Output behavior checks
- Waveform generation (VCD)

Excluded:
- Full state coverage
- Randomized testing
- Performance or timing analysis
- PPA considerations

---

## 3. Directory Structure

docs/chapter3/code/
  rtl/fsm_rtl.sv
  tb/tb_fsm_min.sv
  sim/Makefile

---

## 4. Simulation Tooling

Reference tooling:
- iverilog (compile)
- vvp (execute)
- GTKWave (waveform inspection)

---

## 5. How to Run

cd docs/chapter3/code/sim
make clean
make run
make wave

---

## 6. Clock and Reset

Clock:
- Single clock
- Positive-edge sampling
- Inputs driven on negative edge

Reset:
- Active-low rst_n
- Must define all state and outputs

---

## 7. What to Check

Reset:
- Correct initial state
- Safe output values
- No X/Z propagation

Transitions:
- Nominal path
- Alternate branch
- Stay condition
- Fault path

Outputs:
- Moore outputs stable per state
- Mealy outputs evaluated at defined boundary

---

## 8. Waveform Inspection

Observe:
- clk
- rst_n
- state register
- inputs
- outputs

---

## 9. Typical Issues

- Incomplete reset
- Missing default assignments
- TB/DUT race conditions
- Combinational glitches

---

## 10. Exit Criteria

Proceed when:
- Simulation passes cleanly
- Behavior matches spec
- Waveforms are stable

---

Next: openlane.md
