# **AITL Silicon Pathway**  
### *AI × Control × Digital Circuits × Semiconductor Education Project*

---

## 🔗 Official Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/aitl-silicon-pathway/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/aitl-silicon-pathway/tree/main) |

---

## 🧑‍🚀 Getting Started

If you are new to this project, start here:

1. 📖 **Project Overview** — Read this README
2. 📘 **Chapter 1 Documentation** — Python Baseline Model  
   👉 https://samizo-aitl.github.io/aitl-silicon-pathway/docs/chapter1/
3. 🧠 **Source Code** — Python implementation  
   👉 https://github.com/Samizo-AITL/aitl-silicon-pathway/tree/main/chapter1_python_model

---

# 🧭 **Project Map — Full Pathway Overview**

This project builds an *end-to-end* education & development pipeline from **Python control model → Silicon**.

```
AITL Control Architecture
│
▼
Python Baseline Model (Chapter 1)
│
▼
FSM → Verilog RTL (Chapter 2)
│
▼
OpenLane — Logic Synthesis → P&R → GDSII (Chapter 3)
│
▼
Magic — RC Extraction → SPICE Netlist (Chapter 4)
│
▼
ngspice Waveform / Timing / Power Analysis (Chapter 5)
```

---

# 📚 **Chapter Structure**

Each chapter has its own documentation and code structure.

| Chapter | Description | Documentation | Source Code |
|--------|-------------|---------------|--------------|
| **Chapter 1** | Python Baseline FSM Model (PID × FSM × LLM reference) | [docs/chapter1](docs/chapter1/index.md) | [`chapter1_python_model`](chapter1_python_model) |
| **Chapter 2** | Formal FSM Specification → Verilog RTL Design | [docs/chapter2](docs/chapter2/index.md) | *none* |
| **Chapter 3** | RTL Simulation & ASIC-Flow Feasibility (OpenLane, concept level) | [docs/chapter3](docs/chapter3/index.md) | *none* |
| **Chapter 4** | FSM Formal & Structural Correctness (Invariants, Safety, Equivalence) | [docs/chapter4](docs/chapter4/index.md) | *none* |
| **Chapter 5** | Executable FSM Verification (Assertions, Simulation, Equivalence Checks) | [docs/chapter5](docs/chapter5/index.md) | *none* |

---

# 📘 **Overview**

**AITL Silicon Pathway** systematically studies how the AITL control architecture  
(**PID × FSM × LLM**) can be realized all the way down to silicon.

Pipeline:

**Python → Verilog (RTL) → OpenLane → GDSII → SPICE (ngspice)**

This connects:

- Control engineering  
- Digital logic design  
- ASIC physical design  
- Semiconductor device behavior  
- AI-based controller adaptation  

---

# 🚀 **Goals**

- Build a reproducible “Python → Silicon” educational pathway  
- Provide reusable baseline models (PID/FSM/LLM)  
- Convert behavioral FSM → RTL → Layout  
- Extract real RC parasitics and evaluate timing/waveforms  
- Combine hardware engineering × control × AI into one framework  

---

# 📂 **Repository Structure**

```
aitl-silicon-pathway/
├─ chapter1_python_model/ # Python implementation of AITL baseline
│ ├─ src/ # PID, FSM, Controller code
│ ├─ sim/ # Step response / fault scenario
│ ├─ plots/ # Auto-generated plots
│ └─ example/ # Jupyter demos
│
├─ docs/ # GitHub Pages documentation
│ ├─ chapter1/
│ ├─ chapter2/
│ ├─ chapter3/
│ ├─ chapter4/
│ └─ chapter5/
│
├─ assets/ # Shared images, CSS, includes
└─ README.md # (this file)
```

---

# 📈 **Progress Tracking**

- [x] Repository initialized  
- [x] Chapter 1 baseline (Python model)  
- [x] Chapter 1 documentation + diagrams  
- [ ] Chapter 2 FSM → Verilog RTL  
- [ ] Chapter 3 OpenLane build  
- [ ] Chapter 4 Magic extraction  
- [ ] Chapter 5 SPICE timing/power analysis  

---

## 👤 Author

| 📌 Item | Details |
|--------|---------|
| **Name** | Shinichi Samizo |
| **Expertise** | Semiconductor devices (logic, memory, high-voltage mixed-signal)<br>Thin-film piezo actuators for inkjet systems<br>PrecisionCore printhead productization, BOM management, ISO training |
| **GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |

---

# 📄 License

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](https://samizo-aitl.github.io/SemiDevKit/#-license)

| 📌 Item | License | Description |
|--------|---------|-------------|
| **Source Code** | [**MIT License**](https://opensource.org/licenses/MIT) | Free to use, modify, and redistribute |
| **Text Materials** | [**CC BY 4.0**](https://creativecommons.org/licenses/by/4.0/) or [**CC BY-SA 4.0**](https://creativecommons.org/licenses/by-sa/4.0/) | Attribution required; share-alike applies for BY-SA |
| **Figures & Diagrams** | [**CC BY-NC 4.0**](https://creativecommons.org/licenses/by-nc/4.0/) | Non-commercial use only |
| **External References** | Follow the original license | Cite the original source properly |

---

# 💬 Feedback

> Feedback, ideas, and discussions are welcome.

[![💬 GitHub Discussions](https://img.shields.io/badge/💬%20GitHub-Discussions-brightgreen?logo=github)](https://github.com/Samizo-AITL/aitl-silicon-pathway/discussions)


