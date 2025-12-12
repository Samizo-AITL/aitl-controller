---
layout: default
title: Documentation Index
nav_order: 1
---

# 📚 AITL Silicon Pathway — Documentation Index
Welcome to the official documentation site for **AITL Silicon Pathway**.  
This page serves as the root index for all chapters, diagrams, and reference materials.

---

# 🧭 Full System Pathway

<p align="center">
  <img src="https://raw.githubusercontent.com/Samizo-AITL/aitl-silicon-pathway/main/docs/chapter1/images/controller_data_flow.png" width="80%">
</p>

The project explores the complete engineering pipeline:

**Python → Verilog (RTL) → OpenLane → GDSII → Magic RC Extraction → SPICE Simulation**

---

# 📘 Chapter Index

| Chapter | GitHub Pages | GitHub Source | Description |
|--------|--------------|---------------|-------------|
| **Chapter 1** | [docs/chapter1](./chapter1/index.md) | [/chapter1_python_model](../chapter1_python_model) | Python baseline model (PID × FSM × LLM) |
| **Chapter 2** | [docs/chapter2](./chapter2/README.md) | *(coming soon)* | RTL design of FSM (Verilog) |
| **Chapter 3** | [docs/chapter3](./chapter3/README.md) | *(coming soon)* | OpenLane ASIC flow (RTL → GDSII) |
| **Chapter 4** | [docs/chapter4](./chapter4/README.md) | *(coming soon)* | Magic extraction → SPICE netlist |
| **Chapter 5** | [docs/chapter5](./chapter5/README.md) | *(coming soon)* | Timing & waveform analysis using ngspice |

---

# 🧩 AITL Architecture Overview

<p align="center">
  <img src="https://raw.githubusercontent.com/Samizo-AITL/aitl-silicon-pathway/main/docs/chapter1/images/aitl_3layer.png" width="80%">
</p>

The AITL architecture consists of:

- **PID Layer** — Numerical real-time control  
- **FSM Layer** — Supervisory logic (canonical model for RTL)  
- **LLM Layer** — Adaptive meta-controller  

---

# 📄 Detailed Documentation Structure

```
docs/
├─ index.md 
├─ chapter1/
│ ├─ index.md
│ ├─ overview.md
│ ├─ python_model.md
│ ├─ fsm.md
│ ├─ api.md
│ ├─ getting_started.md
│ └─ images/
│ ├─ aitl_3layer.png
│ ├─ fsm_state_diagram.png
│ ├─ controller_data_flow.png
│ └─ step_response_timeline.png
├─ chapter2/
├─ chapter3/
├─ chapter4/
├─ chapter5/
└─ README.md
```

---

# 🔗 Quick Navigation

- 👉 [Chapter 1 — Python Baseline](./chapter1/index.md)  
- 👉 [Chapter 2 — FSM to Verilog](./chapter2/README.md)  
- 👉 [Chapter 3 — OpenLane Flow](./chapter3/README.md)  
- 👉 [Chapter 4 — Extraction & SPICE](./chapter4/README.md)  
- 👉 [Chapter 5 — Timing Analysis](./chapter5/README.md)

---

# 📬 Feedback

Discussion & feedback:  
https://github.com/Samizo-AITL/aitl-silicon-pathway/discussions

