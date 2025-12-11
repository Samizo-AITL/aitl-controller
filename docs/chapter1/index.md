---
title: "Chapter 1 — Python Baseline Model"
layout: default
nav_order: 1
description: "AITL Silicon Pathway Chapter 1: Python baseline implementation of PID × FSM × LLM hybrid control architecture"
---

# 🧩 Chapter 1 — Python Baseline Model  
## *AITL Architecture: PID × FSM × LLM*

This chapter introduces the foundational Python model of the AITL control architecture  
and provides links to all Chapter 1 documentation pages.

---

# 🖼️ AITL Architecture Overview

<p align="center">
  <img src="/aitl-silicon-pathway/docs/chapter1/images/aitl_3layer.svg" width="80%">
</p>

---

# 📂 Documentation Index

| File | Description |
|------|-------------|
| [README.md](README.md) | Folder-level introduction |
| [overview.md](overview.md) | Conceptual explanation of the architecture |
| [python_model.md](python_model.md) | Code-level explanation of PID / FSM / controller |
| [fsm.md](fsm.md) | Canonical state machine rules (RTL input) |
| [api.md](api.md) | Programmatic API reference |
| [getting_started.md](getting_started.md) | How to install and run Chapter1 code |

---

# 🎯 Objectives of Chapter 1

- Understand the three-layer AITL architecture  
- Implement the Python baseline model  
- Learn canonical FSM rules → later used for RTL Verilog  
- Run simulations:  
  - Step response  
  - Fault scenario  
- Establish the **behavioral golden model** for hardware translation

---

# 🧭 FSM Overview

<p align="center">
  <img src="/aitl-silicon-pathway/docs/chapter1/images/fsm_state_diagram.svg" width="80%">
</p>

---

# 🔧 Controller Data Flow

<p align="center">
  <img src="/aitl-silicon-pathway/docs/chapter1/images/controller_data_flow.svg" width="80%">
</p>

---

# 📈 Step Response Simulation

<p align="center">
  <img src="/aitl-silicon-pathway/docs/chapter1/images/step_response_timeline.svg" width="80%">
</p>

---

# ⚠️ Fault Scenario Simulation

<p align="center">
  <img src="/aitl-silicon-pathway/docs/chapter1/images/fault_timeline.svg" width="80%">
</p>

---

# 🔗 Next Steps

Proceed to:

👉 **[overview.md](overview.md)**  
or  
👉 **[python_model.md](python_model.md)**

---

# © AITL Silicon Pathway Project
