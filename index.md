---
layout: default
title: Documentation Index
nav_order: 1
---

# 📚 AITL Silicon Pathway — Documentation Index
Welcome to the official documentation site for **AITL Silicon Pathway**.  
This page serves as the root index for all chapters, diagrams, and reference materials.

---

## 🔗 Official Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/aitl-silicon-pathway/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/aitl-silicon-pathway/tree/main) |

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
| **Chapter 1** | [docs/chapter1](/docs/chapter1/index.md) | [/chapter1_python_model](/chapter1_python_model) | Python baseline model (PID × FSM × LLM) |
| **Chapter 2** | [docs/chapter2](/docs/chapter2/index.md) | *(coming soon)* | RTL design of FSM (Verilog) |
| **Chapter 3** | [docs/chapter3](/docs/chapter3/index.md) | *(coming soon)* | OpenLane ASIC flow (RTL → GDSII) |
| **Chapter 4** | [docs/chapter4](/docs/chapter4/index.md) | *(coming soon)* | Magic extraction → SPICE netlist |
| **Chapter 5** | [docs/chapter5](/docs/chapter5/index.md) | *(coming soon)* | Timing & waveform analysis using ngspice |

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

## 👤 Author

| 📌 Item | Details |
|--------|---------|
| **Name** | Shinichi Samizo |
| **Education** | M.S. in Electrical and Electronic Engineering, Shinshu University |
| **Career** | Former Engineer at Seiko Epson Corporation (since 1997) |
| **Expertise** | Semiconductor devices (logic, memory, high-voltage mixed-signal)<br>Thin-film piezo actuators for inkjet systems<br>PrecisionCore printhead productization, BOM management, ISO training |
| **Email** | [![Email](https://img.shields.io/badge/Email-shin3t72%40gmail.com-red?style=for-the-badge&logo=gmail)](mailto:shin3t72@gmail.com) |
| **X (Twitter)** | [![X](https://img.shields.io/badge/X-@shin3t72-black?style=for-the-badge&logo=x)](https://x.com/shin3t72) |
| **GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |

---

# 📄 License

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](https://samizo-aitl.github.io/aitl-silicon-pathway/#-license)

| Item | License | Description |
|------|---------|-------------|
| **Source Code** | MIT | Free to use, modify, redistribute |
| **Text Materials** | CC BY 4.0 / CC BY-SA 4.0 | Attribution & share-alike rules |
| **Figures & Diagrams** | CC BY-NC 4.0 | Non-commercial use |
| **External References** | Original license applies | Cite properly |

---

# 💬 Feedback

> Feedback, ideas, and discussions are welcome.

[![💬 GitHub Discussions](https://img.shields.io/badge/💬%20GitHub-Discussions-brightgreen?logo=github)](https://github.com/Samizo-AITL/aitl-silicon-pathway/discussions)

