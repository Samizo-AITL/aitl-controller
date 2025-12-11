---
title: "FSM Specification — AITL Supervisory Controller"
layout: default
nav_order: 4
description: "Formal and canonical definition of the AITL state machine used in the Python model, RTL model, and all downstream hardware flows."
---

# 🧭 FSM Specification — AITL Supervisory State Machine  
## *Canonical definition for Python → RTL → ASIC*

This document defines the **official AITL finite state machine (FSM)** used in Chapter 1.  
It is the *authoritative specification* that must be reproduced exactly in:

- Python baseline (this chapter)  
- Verilog RTL (Chapter 2)  
- Gate-level netlists (Chapter 3)  
- Extracted netlists and SPICE simulations (Chapter 4–5)  

FSM correctness is the core requirement for hardware functional equivalence.

---

# 🔒 1. State Definitions (Canonical)

The AITL controller uses **exactly four states**, no more, no less:

| State | Description |
|-------|-------------|
| **IDLE** | Default inactive state; system waiting for start condition |
| **STARTUP** | Initialization state; system performing controlled startup logic |
| **RUN** | Normal closed-loop control operation; PID enabled |
| **FAULT** | Error detected; system halts until reset |

There are **no intermediate, hidden, or auxiliary states**.

These four states must map directly to RTL state encodings (binary or one-hot) in Chapter 2.

---

# 🔀 2. Inputs to the FSM

The FSM reacts to the following **boolean control signals**:

| Signal | Meaning |
|--------|---------|
| `start_cmd` | User/system command to begin operation |
| `startup_done` | Internal flag indicating startup sequence finished |
| `error_detected` | Error flag from sensor, safety checker, or controller |
| `reset_cmd` | Command to leave FAULT state and return to IDLE |

These inputs **must not** be overloaded or repurposed in RTL.

---

# 🔁 3. Official Transition Rules

Below is the **canonical transition table**. RTL must match it exactly.

## From IDLE

```
IF start_cmd == True → STARTUP
ELSE remain in IDLE
```

---

## From STARTUP

```
IF error_detected == True → FAULT
ELSE IF startup_done == True → RUN
ELSE remain in STARTUP
```

---

## From RUN

```
IF error_detected == True → FAULT
ELSE remain in RUN
```

---

## From FAULT

```
IF reset_cmd == True → IDLE
ELSE remain in FAULT
```

---

# 📊 4. State Transition Diagram (ASCII)

```
       +--------+
       |  IDLE  |
       +--------+
           |
           | start_cmd
           v
      +-----------+
      |  STARTUP  |
      +-----------+
       |         |
       |startup_ | error_detected
       | done    v
       v      +--------+
    +-------> | FAULT  |
    |         +--------+
    | reset_cmd   ^
    |             |
    v             |
   +--------+     |
   |  RUN   |-----+
   +--------+ error_detected
```

This diagram MUST match the RTL state machine exactly.

---

# 📌 5. FSM Behavioral Guarantees

### ✦ Guarantee 1 — No implicit resets  
FSM must not reset internal states except where explicitly defined.

### ✦ Guarantee 2 — Deterministic outputs  
Given the same sequence of inputs, FSM must produce identical state sequences in:

- Python  
- RTL  
- ASIC  
- SPICE simulations (via extracted netlists)

### ✦ Guarantee 3 — No time-dependent transitions  
FSM behavior depends *only* on boolean inputs, not on elapsed time.

### ✦ Guarantee 4 — Persistent FAULT  
The FAULT state is absorbing **until reset_cmd is asserted**.

### ✦ Guarantee 5 — PID enable logic tied to FSM  
PID is **enabled only in STARTUP and RUN**.  
This rule is part of the FSM behavior.

---

# 🔧 6. Output Conditions (Supervisory Behavior)

| State | PID Enabled? | control_output |
|--------|--------------|----------------|
| IDLE | No | `0` |
| STARTUP | Yes | PID output |
| RUN | Yes | PID output |
| FAULT | No | `0` |

These must become **explicit control signals** in RTL.

---

# 🏗 7. RTL Encoding Requirements (for Chapter 2)

Although encoding is implementation-defined, the following must hold:

- FSM must have **4 distinct states**  
- RTL must preserve **all transitions exactly as defined**  
- No extra reset or default behavior may be added  
- Output control signals must reflect FSM state exactly  
- FAULT state must suppress PID entirely  

Recommended encodings:

```
Binary:
IDLE    = 00
STARTUP = 01
RUN     = 10
FAULT   = 11
```

or one-hot:

```
IDLE    = 0001
STARTUP = 0010
RUN     = 0100
FAULT   = 1000
```

Either encoding is acceptable so long as behavior matches Python.

---

# 📦 8. Golden Vector Examples (for RTL verification)

## Example 1 — Normal Startup → Run

```
Inputs: start_cmd=1, startup_done=1, error_detected=0
States: IDLE → STARTUP → RUN
```

## Example 2 — Fault During Startup

```
Inputs: error_detected=1 during STARTUP
States: IDLE → STARTUP → FAULT
```

## Example 3 — Fault During Run

```
Inputs: error_detected=1 during RUN
States: IDLE → STARTUP → RUN → FAULT
```

## Example 4 — Reset From Fault

```
Inputs: reset_cmd=1
States: FAULT → IDLE
```

These patterns must be used in RTL simulation.

---

# 📘 Summary

This FSM is the supervisory backbone of the AITL architecture.  
It defines **when** control is allowed, **how** faults are handled, and **what** behavior downstream hardware must follow.

This specification is the **canonical reference** for:

- Python baseline model  
- Verilog RTL  
- Testbench behavior  
- Gate-level simulations  
- ASIC verification  

Nothing in the FSM may be changed without revising the entire hardware pathway.

---

# ⏭ Next Document

Proceed to:

👉 **api.md** — Full API specification for PID, FSM, and AITL Controller  
👉 **getting_started.md** — How to run and simulate the model

---

# © AITL Silicon Pathway Project

