---
title: "API Reference — AITL Python Baseline Model"
layout: default
nav_order: 5
description: "Complete API documentation for PID, FSM, and AITL Controller used in the Chapter 1 Python baseline model."
---

# 📘 API Reference — AITL Python Baseline Model  
## *PID × FSM × Controller interface documentation*

This API reference defines the public interfaces, attributes, methods, and behavioral
contracts for the Python implementation of the AITL hybrid control architecture.

These APIs are the **canonical reference** for RTL designers, testbench writers,
and anyone extending the AITL system.

---

# 🧩 Modules Overview

The Python model consists of the following modules:

| File | Contains |
|------|----------|
| `pid.py` | PID controller class |
| `fsm.py` | State enum + finite state machine logic |
| `aitl_controller.py` | Top-level controller combining PID + FSM |
| `llm_placeholder.py` | Stubs for future adaptation layer |

Only documented functions and fields below should be considered “public API.”

---

# 1️⃣ PID Class (`pid.py`)

```
PID(kp, ki, kd, dt)
```

Initializes a discrete-time PID controller.

---

## 📌 Attributes

| Attribute | Type | Description |
|-----------|-------|-------------|
| `kp` | float | Proportional gain |
| `ki` | float | Integral gain |
| `kd` | float | Derivative gain |
| `dt` | float | Sampling interval |
| `_integral` | float | Accumulated integral term |
| `_prev` | float | Previous error (for derivative term) |

`_integral` and `_prev` must persist across control steps unless explicitly reset.

---

## 📌 Methods

### `update(setpoint, measured) → float`

Compute control output for the current timestep.

Steps:

1. `e = setpoint - measured`  
2. Accumulate integral: `_integral += e * dt`  
3. Compute derivative: `d = (e - _prev) / dt`  
4. Output:  
   ```
   u = kp*e + ki*_integral + kd*d
   ```
5. Update memory: `_prev = e`  

### 🔒 Behavioral Contract

- Must run only when the FSM allows (STARTUP, RUN).  
- Output must be exactly zero in IDLE and FAULT (handled by controller).  
- Internal memory must never reset unless FSM or controller performs a reset.  
- Arithmetic behavior must be preserved in RTL (Chapter 2).

---

# 2️⃣ FSM Logic (`fsm.py`)

```
AITLState(Enum)
```

Defines the four supervisory states:

```
IDLE, STARTUP, RUN, FAULT
```

---

## 📌 Transition Function

FSM transitions are implemented inside the controller, but rules are as follows:

### From `IDLE`
```
if start_cmd → STARTUP
else remain in IDLE
```

### From `STARTUP`
```
if error_detected → FAULT
elif startup_done → RUN
else remain in STARTUP
```

### From `RUN`
```
if error_detected → FAULT
else remain in RUN
```

### From `FAULT`
```
if reset_cmd → IDLE
else remain in FAULT
```

These rules are **canonical** and must not be changed in downstream implementations.

---

# 3️⃣ AITLControllerA (`aitl_controller.py`)

The top-level controller orchestrating FSM + PID.

```
AITLControllerA(pid: PID)
```

---

## 📌 Attributes

| Attribute | Description |
|-----------|-------------|
| `pid` | PID instance used for control |
| `state` | Current FSM state |
| `setpoint` | Target value for PID |
| `measured` | Latest measurement |
| `control_output` | Current control output |
| `start_cmd` | Boolean command to start system |
| `reset_cmd` | Boolean command to clear FAULT |
| `startup_done` | Boolean flag signaling adequate initialization |
| `error_detected` | Boolean fault input |

All these fields may be toggled externally by simulation or higher-level logic.

---

## 📌 Methods

### `step(measured) → float`

Runs a single cycle of controller logic:

1. Latch measurement: `self.measured = measured`  
2. Update FSM state  
3. If `state ∈ {STARTUP, RUN}` → compute PID output  
4. Otherwise → output = 0  
5. Return control output  

This function is the **core behavioral loop** and must be preserved exactly in RTL.

---

### `_update_fsm()`

Internal helper implementing transition logic.  
Not intended for external use.

---

### `reset()`

Resets controller to safe IDLE configuration.  
Internal PID memory is *not* cleared unless explicitly desired.

---

# 4️⃣ LLM Placeholder (`llm_placeholder.py`)

Current implementation is intentionally empty:

```
class LLMModule:
    def update(self, controller_state):
        pass
```

Purpose:

- Reserve interface for future intelligent behavior  
- Avoid influence on deterministic baseline model  
- Allow future PID tuning / FSM rewriting modules to hook in  

NOT translated to RTL.

---

# 5️⃣ Module Interactions

```
External Inputs → FSM → PID → Control Output
                      ↑
                      └──── LLM (future)
```

### Behavioral Summary

| Component | Role |
|-----------|------|
| PID | Computes control output |
| FSM | Determines whether PID may run |
| Controller | Coordinates timing and safety |
| LLM | Placeholder |

---

# 6️⃣ Error & Reset Behavior

| Condition | Result |
|-----------|--------|
| `error_detected = True` | FSM → FAULT, PID disabled |
| `reset_cmd = True` | FSM → IDLE, output = 0 |
| `start_cmd = True` | FSM → STARTUP |
| `startup_done = True` | FSM → RUN |

No side effects or hidden transitions permitted.

---

# 📘 Summary

This API defines the official behavioral contract for the AITL Python model.  
Downstream RTL must replicate:

- methods  
- internal memory behavior  
- enable/disable logic  
- FSM transitions  
- PID computations  

This ensures **functional equivalence across Python → RTL → ASIC → SPICE**.

---

# ⏭ Next Document

👉 **getting_started.md** — Installation, execution, simulation usage

---

# © AITL Silicon Pathway Project

