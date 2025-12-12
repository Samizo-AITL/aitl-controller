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

> ⚠ **Diagram Rendering Notice**  
>  
> The system pathway diagram above is written in **Mermaid**.  
> Due to current limitations of **GitHub Pages**, Mermaid diagrams are **not rendered** on this site.  
>  
> Please refer to the **GitHub repository view** (linked above) to see the diagram correctly rendered.

---

# 🧭 Full System Pathway

```mermaid
flowchart TD
    PY[Python Baseline Model]
    SPEC[FSM Specification]
    RTL[Verilog RTL]
    OL[OpenLane Flow]
    GDS[GDSII Layout]
    EXT[RC Extraction]
    SPICE[SPICE Simulation]

    PY --> SPEC
    SPEC --> RTL
    RTL --> OL
    OL --> GDS
    GDS --> EXT
    EXT --> SPICE
```

The project explores the complete engineering pipeline:

**Python → Verilog (RTL) → OpenLane → GDSII → Magic RC Extraction → SPICE Simulation**

---

# 📘 Chapter Index

| Chapter | GitHub Pages | GitHub Source | Description |
|--------|--------------|---------------|-------------|
| **Chapter 1** | [docs/chapter1](/docs/chapter1/index.md) | [/chapter1_python_model](/chapter1_python_model/index.md) | Python baseline model (PID × FSM × LLM) |
| **Chapter 2** | *(coming soon)*  | *(coming soon)* | RTL design of FSM (Verilog) |
| **Chapter 3** | *(coming soon)*  | *(coming soon)* | OpenLane ASIC flow (RTL → GDSII) |
| **Chapter 4** | *(coming soon)*  | *(coming soon)* | Magic extraction → SPICE netlist |
| **Chapter 5** | *(coming soon)*  | *(coming soon)* | Timing & waveform analysis using ngspice |

---

# 🧩 AITL Architecture Overview

```mermaid
flowchart TD
    R[Reference]
    E[Error]
    PID[PID Controller]
    FSM[FSM Supervisor]
    PLANT[Plant]
    Y[Output]
    LLM[LLM Meta Control]

    R --> E
    Y --> E
    E --> PID
    PID --> PLANT
    PLANT --> Y

    FSM --> PID
    FSM --> PLANT

    LLM -. tuning .-> PID
    LLM -. policy .-> FSM
```

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
│  ├─ index.md
│  ├─ overview.md
│  ├─ python_model.md
│  ├─ fsm.md
│  ├─ api.md
│  ├─ getting_started.md
│  └─ images/
│     ├─ aitl_3layer.png
│     ├─ fsm_state_diagram.png
│     ├─ controller_data_flow.png
│     └─ step_response_timeline.png
├─ chapter2/
├─ chapter3/
├─ chapter4/
├─ chapter5/
└─ README.md
```

---

# 🔗 Quick Navigation

- 👉 [Chapter 1 — Python Baseline](/docs/chapter1/index.md)  
- 👉 [Chapter 2 — FSM to Verilog](/docs/chapter2/index.md)  
- 👉 [Chapter 3 — OpenLane Flow](/docs/chapter3/index.md)  
- 👉 [Chapter 4 — Extraction & SPICE](/docs/chapter4/index.md)  
- 👉 [Chapter 5 — Timing Analysis](/docs/chapter5/index.md)

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
