# 🧩 Chapter 1 — Python Baseline Model  
## *AITL Architecture: PID × FSM × LLM*

This chapter introduces the foundational Python model of the AITL control architecture.  
It also links to all detailed documentation pages of Chapter 1.

---

## 🔗 Official Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/aitl-silicon-pathway/docs/chapter1/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/aitl-silicon-pathway/tree/main/docs/chapter1) |

> ⚠ **Diagram Rendering Notice**  
>  
> The system pathway diagram above is written in **Mermaid**.  
> Due to current limitations of **GitHub Pages**, Mermaid diagrams are **not rendered** on this site.  
>  
> Please refer to the **GitHub repository view** (linked above) to see the diagram correctly rendered.

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
- Learn the canonical FSM rules (later used for RTL)  
- Run simulations:  
  - Step response  
  - Fault scenario  
- Establish the behavioral golden model for hardware translation  

---

# 🧭 FSM Overview

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

---

# 🔧 Controller Data Flow

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

---

# 📈 Step Response Simulation

<img src="https://raw.githubusercontent.com/Samizo-AITL/aitl-silicon-pathway/main/docs/chapter1/images/step_response_timeline.svg" width="80%" />

---

# ⚠ Fault Scenario Simulation

<img src="https://raw.githubusercontent.com/Samizo-AITL/aitl-silicon-pathway/main/docs/chapter1/images/fault_timeline.svg" width="80%" />

---

# 🚀 Next Steps

Continue to:

👉 **[overview.md](overview.md)**  
or  
👉 **[python_model.md](python_model.md)**  

---

# © AITL Silicon Pathway Project
