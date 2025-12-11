---
title: "Python Model — Chapter 1 Reference Implementation"
layout: default
nav_order: 3
description: "Detailed explanation of the Python baseline implementation of the PID × FSM × LLM hybrid control architecture."
---

# 🧪 Python Model — Reference Implementation for AITL Architecture  
## *PID × FSM × LLM baseline model used across all downstream hardware flows*

This document explains the **Python implementation** of the AITL architecture as built in Chapter 1.  
It describes the structure, design rationale, and execution flow of each component, forming the **behavioral golden model** for RTL, ASIC, and SPICE verification.

---

# 🎯 Purpose of This Document

- Explain *how* the Python model is structured  
- Provide detailed behavior definitions for each module  
- Define internal state handling, update timing, and execution rules  
- Serve as the code-level specification for RTL (Chapter 2)  
- Enable reproducible simulation and testing  

---

# 🧱 Python Model Structure

```
chapter1_python_model/
├── src/
│   ├── pid.py
│   ├── fsm.py
│   ├── aitl_controller.py
│   └── llm_placeholder.py
├── sim/
│   ├── run_step_response.py
│   └── run_fault_scenario.py
├── plots/
├── tests/
└── main.py
```

Each file has a strict role, matching the separation of concerns used later in RTL and ASIC design.

---

# 1️⃣ PID Controller (`pid.py`)

The PID controller is implemented as a class maintaining its own internal memory:

```python
class PID:
    def __init__(self, kp, ki, kd, dt):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.dt = dt
        self._integral = 0
        self._prev = 0
```

## 🔍 Key Behavioral Rules

### 1. Error computation  
`e = setpoint - measured`

### 2. Integral accumulation  
`_integral += e * dt`  
- Never resets automatically  
- Reset only when FSM directs (controller in IDLE/FAULT)

### 3. Derivative term  
`d = (e - _prev) / dt`

### 4. Output  
`u = kp*e + ki*integral + kd*d`

### 5. Memory update  
`_prev = e`

### 6. Execution Timing  
PID runs **only when FSM state is STARTUP or RUN**.

### 7. Disabled Output  
In IDLE and FAULT:  
→ PID output must be **0**, internal memory preserved unless explicitly reset.

These rules must be preserved 1:1 in Verilog.

---

# 2️⃣ FSM — Supervisory Logic (`fsm.py`)

The FSM defines four stable states:

```python
class AITLState(Enum):
    IDLE = auto()
    STARTUP = auto()
    RUN = auto()
    FAULT = auto()
```

## 🔄 Canonical Transition Logic

The FSM transition function:

```python
def update_fsm(self):
    if state == IDLE:
        if start_cmd: → STARTUP

    if state == STARTUP:
        if error_detected: → FAULT
        elif startup_done: → RUN

    if state == RUN:
        if error_detected: → FAULT

    if state == FAULT:
        if reset_cmd: → IDLE
```

### These transitions are *canonical*  
Meaning:

- Must match in RTL  
- Must match in ASIC  
- Must produce identical state sequences for the same input vectors

No additional transitions are permitted.

---

# 3️⃣ AITL Controller Integration (`aitl_controller.py`)

This module binds PID + FSM into a single executable control unit.

```python
class AITLControllerA:
    def __init__(self, pid):
        self.pid = pid
        self.state = AITLState.IDLE
```

## 🧩 Responsibilities

1. Manage command inputs:
   - `start_cmd`
   - `reset_cmd`
   - `error_detected`
   - `startup_done`

2. Handle setpoint and measurement

3. Call FSM update function

4. Enable/disable PID

5. Produce control output

---

## Execution Logic (`step()` function)

```python
def step(self, measured):
    self.measured = measured
    self._update_fsm()
    
    if self.state in (STARTUP, RUN):
        self.control_output = self.pid.update(self.setpoint, measured)
    else:
        self.control_output = 0

    return self.control_output
```

### Step Execution Timeline

1. Inputs latched  
2. FSM transition executed  
3. PID enabled or disabled  
4. Control output computed  
5. Return output for simulation or logging

This execution order MUST remain unchanged in RTL.

---

# 4️⃣ LLM Layer (Placeholder) (`llm_placeholder.py`)

This module is intentionally minimal:

- No adaptive behavior  
- No real-time action  
- Reserved for future intelligent tuning  

Purpose:

- Define the interface for future work  
- Avoid affecting deterministic behavior in Ch.1  

RTL implementation simply ignores this module.

---

# 5️⃣ Simulation Scripts (`sim/`)

Two simulation scenarios validate controller behavior.

---

## 📈 Step Response (`run_step_response.py`)

Simulates plant response to a setpoint step input.

Verifies:

- PID dynamics  
- Rising response  
- Stability  
- Proper execution timing  
- Correct enabling/disabling of PID  

Plot saved into:

```
plots/step_response_YYYYMMDD_HHMMSS.png
```

---

## ⚠️ Fault Scenario (`run_fault_scenario.py`)

Injects faults during execution:

- FSM must enter FAULT  
- PID output must drop to zero  
- FAULT must persist  
- Reset command must return to IDLE  

This scenario validates supervisory logic under failure.

---

# 6️⃣ Testing (`tests/`)

Provides Python unit tests:

- FSM correctness  
- PID output stability  
- Controller-level integration  

These tests prevent regressions before RTL development begins.

---

# 🧩 Alignment With Downstream Hardware Design

This Python model acts as the **behavioral golden model** for:

| Stage | Relation |
|-------|----------|
| RTL (Ch.2) | Must replicate PID + FSM behavior cycle-by-cycle |
| OpenLane (Ch.3) | Controller logic becomes hardware blocks |
| Magic (Ch.4) | Extracted parasitics must not break function |
| SPICE (Ch.5) | Waveforms must match Python baseline |

If Python behavior changes, **all downstream verification must restart**.

---

# 📦 Summary of Guarantees

The Python model provides:

- Deterministic outputs  
- Canonical FSM rules  
- Exact PID formula and timing  
- Clear enable/disable behavior  
- Isolated test cases  
- Documented internal states  

This ensures a stable pathway from software to silicon.

---

# 🚀 Next

Continue to:

👉 **fsm.md** — Formal state transition rules and canonical table (for RTL)  
👉 **api.md** — Programmatic interface specification  

---

# © AITL Silicon Pathway Project

