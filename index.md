---
layout: default
title: aitl-silicon-pathway
---

# **AITL Silicon Pathway**  
### *AI × Control × Digital Circuits × Semiconductor Education Project*

---

## 🔗 Official Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/aitl-silicon-pathway/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/aitl-silicon-pathway/tree/main) |

---

## 📘 **Overview**

**AITL Silicon Pathway** is an educational project that systematically explores how the AITL control architecture  
(**PID × FSM × LLM**) can be implemented and studied along a complete “pathway to silicon”:

**Python → Verilog (RTL) → OpenLane → GDSII → SPICE (ngspice)**

The objective is to connect control engineering, digital circuit design, semiconductor physical design,  
and AI-driven modeling into one coherent learning framework.

---

## 📚 **Chapter Structure**

### **Chapter 1: AITL Control Architecture in Python**  
Implement the three-layer AITL architecture—PID, FSM, and LLM—in Python to build a foundation for hybrid control systems.

### **Chapter 2: RTL Conversion of the FSM (Verilog)**  
Translate the Python-based FSM into synthesizable Verilog RTL and learn practical principles of hardware state machine design.

### **Chapter 3: From RTL to ASIC (OpenLane)**  
Use OpenLane for logic synthesis, floorplanning, placement & routing, and generate a GDSII layout suitable for fabrication.

### **Chapter 4: Layout Extraction (Magic)**  
Perform parasitic (RC) extraction and generate an extracted SPICE netlist directly from the physical layout.

### **Chapter 5: Waveform & Timing Analysis (ngspice)**  
Simulate the extracted netlist in ngspice to analyze real physical effects such as delay, waveform behavior, and power consumption.

---

## 🚀 **Goals**

- Understand how a Python control model is realized in silicon  
- Experience a full digital/ASIC design workflow end-to-end  
- Deepen system-level understanding of the AITL architecture from a hardware perspective  

---

## 📂 **Progress**

- [x] Repository initialized  
- [ ] Chapter 1 content implementation  
- [ ] Chapter 2: FSM → Verilog RTL  
- [ ] Chapter 3: OpenLane workflow  
- [ ] Chapter 4: Magic parasitic extraction  
- [ ] Chapter 5: ngspice timing/power analysis  

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

## 📄 License

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](https://samizo-aitl.github.io/SemiDevKit/#-license)

> SemiDevKit adopts a hybrid licensing approach tailored to the nature of each component—source code, text materials, and graphical content.

| 📌 Item | License | Description |
|--------|---------|-------------|
| **Source Code** | [**MIT License**](https://opensource.org/licenses/MIT) | Free to use, modify, and redistribute |
| **Text Materials** | [**CC BY 4.0**](https://creativecommons.org/licenses/by/4.0/) or [**CC BY-SA 4.0**](https://creativecommons.org/licenses/by-sa/4.0/) | Attribution required; share-alike applies for BY-SA |
| **Figures & Diagrams** | [**CC BY-NC 4.0**](https://creativecommons.org/licenses/by-nc/4.0/) | Non-commercial use only |
| **External References** | Follow the original license | Cite the original source properly |

---

## 💬 Feedback

> Suggestions, improvements, and discussions are welcome via GitHub Discussions.

[![💬 GitHub Discussions](https://img.shields.io/badge/💬%20GitHub-Discussions-brightgreen?logo=github)](https://github.com/Samizo-AITL/aitl-silicon-pathway/discussions)

