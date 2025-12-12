---
layout: default
title: "4.5 Guarantee Boundary: Connecting PID / FSM / LLM"
---

# 4.5 Guarantee Boundary: Connecting PID / FSM / LLM

Formal/structural guarantees are only meaningful when we define the boundary:
- what the FSM assumes about its environment
- what it guarantees to other layers

This file defines a contract using **Assume/Guarantee** style.

---

## Layers and responsibilities (AITL)

- PID layer (inner loop):
  - ensures continuous-time stability/performance within a mode
- FSM layer (supervisor):
  - selects mode, enforces safety interlocks, handles faults
- LLM layer (outermost):
  - diagnosis, recovery plan, redesign (gain retuning, rule edits)

The FSM must be the “deterministic spine” of the control stack.

---

## Contract format

### Assumptions (A)
Constraints the environment must satisfy for FSM guarantees to hold.
Examples:
- A1: inputs are synchronous to clk (no metastability at boundary)
- A2: reset is asserted long enough and deasserted cleanly
- A3: command encoding is valid (e.g., one-hot or enumerated)

### Guarantees (G)
Properties the FSM provides if assumptions hold.
Examples:
- G1: illegal states never occur
- G2: safe outputs asserted on fault within N cycles
- G3: mode outputs correspond to state meaning

---

## PID ↔ FSM boundary (control-plane vs data-plane)

### What FSM guarantees to PID
- G-PID1: `mode` is always a legal mode (enum-safe)
- G-PID2: `mode` changes only at clock edge (no glitch)
- G-PID3: `safe_en==0` in SAFE/ERROR states (actuation disabled)
- G-PID4: If `fault==1`, FSM enters SAFE/ERROR within N cycles (as specified)

### What FSM assumes from PID/sensors
- A-PID1: `fault` is asserted when plant safety requires it (fault semantics)
- A-PID2: PID respects `safe_en` gating (no actuation when disabled)

---

## LLM ↔ FSM boundary (change authority and safety)

LLM may propose:
- PID retuning
- FSM transition rule edits
- new invariants or monitors

But runtime authority must be constrained.

### What FSM guarantees to LLM (observability)
- G-LLM1: state and key events are observable (status interface)
- G-LLM2: fault reason codes are consistent and latched as specified

### What FSM assumes about LLM actions
- A-LLM1: LLM updates are applied only in a safe maintenance window
- A-LLM2: Any update is validated against invariants before activation

### “Guarded update” rule (recommended)
- Updates must not:
  - weaken safety invariants
  - remove fault paths
  - create illegal transitions
This can be enforced by re-running the Chapter 4 checklist on every update.

---

## Result (deliverable boundary statement)

Produce a short contract:
- Assumptions A1..Ak
- Guarantees G1..Gm
- Clear mapping:
  - which signals cross PID boundary
  - which signals cross LLM boundary
  - what is required to safely update rules
