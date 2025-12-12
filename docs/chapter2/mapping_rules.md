# File: docs/chapter2/mapping_rules.md

# Python-to-Verilog FSM Mapping Rules  
## Formal Translation from Software to Hardware

This document defines **explicit mapping rules** that translate a Python-defined FSM
into **synthesizable Verilog RTL**.  
These rules ensure that the FSM behavior remains deterministic and hardware-safe.

---

## Mapping Philosophy

Python FSMs are written for **execution**.  
Hardware FSMs are written for **realization**.

The goal of this mapping is to:

- Remove software execution assumptions
- Make all states and transitions explicit
- Guarantee clocked, deterministic behavior
- Preserve logical equivalence with the Python FSM

---

## State Representation Mapping

### Python Level

- States represented as:
  - Enum values
  - Strings
  - Class attributes
- Implicit state storage in variables

### Verilog Level

- States represented as:
  - Explicit registers
  - Fixed-width binary encodings
- State storage in a clocked register

### Rule

- Every Python state → one Verilog state symbol
- No dynamic state creation is allowed

---

## State Encoding Rules

- Encoding type: **Binary encoding**
- Bit width:  
  ```
  state_width = ceil(log2(number_of_states))
  ```

- Encoding example:

| State | Binary Code |
|------|-------------|
| IDLE | 3'b000 |
| INIT | 3'b001 |
| RUN | 3'b010 |
| FAULT | 3'b011 |
| RECOVER | 3'b100 |

Encoding is fixed and must not change during synthesis.

---

## Input Condition Mapping

### Python Level

- Boolean expressions:
  ```
  if start and not fault:
  ```

### Verilog Level

- Combinational logic using signals:
  ```
  if (start && !fault_detected)
  ```

### Rule

- Python boolean expressions map directly to Verilog logical operators
- All input signals must be synchronous to the FSM clock
- No blocking or waiting constructs are allowed

---

## Transition Logic Mapping

### Python Level

```
if state == IDLE:
    if start:
        state = INIT
```

### Verilog Level

```
case (state)
  S_IDLE: begin
    if (start)
      next_state = S_INIT;
    else
      next_state = S_IDLE;
  end
endcase
```

### Rules

- Transition logic must be **purely combinational**
- All branches must assign `next_state`
- No latch inference is allowed

---

## Output Logic Mapping

### Python Level

- Outputs often set imperatively:
  ```
  mode = RUN
  ```

### Verilog Level

- Outputs derived from state (Moore FSM):
  ```
  assign mode_run = (state == S_RUN);
  ```

### Rules

- Outputs depend only on current state
- Output logic must be combinational
- No output registers are required

---

## Reset Mapping

- Python reset often implicit
- Verilog reset must be explicit and synchronous

### Rule

```
if (reset)
  state <= S_IDLE;
```

Reset dominates all other transitions.

---

## Forbidden Constructs

The following are **not allowed** in RTL FSM implementation:

- Dynamic state variables
- Python-style loops
- Blocking delays
- Event-driven callbacks
- Incomplete case statements

---

## Summary

This mapping enforces:

- One-to-one correspondence between Python states and Verilog states
- Explicit transition coverage
- Fully deterministic hardware behavior
- ASIC-safe RTL suitable for OpenLane

These rules must be followed exactly in the RTL implementation.

---
