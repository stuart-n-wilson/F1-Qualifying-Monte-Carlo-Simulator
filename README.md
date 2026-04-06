# 🏎️ F1 Qualifying Simulator Application

![Python](https://img.shields.io/badge/Python-blue)

An app that uses Monte Carlo Simulation to simulate F1 Qualifying sessions. Try it out [**here**](https://f1-qualifying-monte-carlo-simulator.streamlit.app/Qualifying_simulator).

---

## 🚀 Overview

This application uses Monte Carlo simulation and real F1 data to simulate Formula 1 Qualifying sessions. 

Key features: 
- each qualifying session simulates Q1, Q2 and Q3, with drivers being eliminated at each stage
- automatically generated heatmap and probability distributions plots for drivers and positions
- live deployment, with support for Grand Prix from 2018 to present day and beyond

---

## ⚙️ Technical aspects

---

## 📂 Application Structure

```
F1-Qualifying-Monte-Carlo-Simulator/
├── pages/
│   ├── Qualifying_simulator.py   # Application simulator page
├── Homepage.py                   # Application homepage
├── plotting.py                   # Visualisation functions
├── requirements.txt              # Package requirements
├── simulator.py                  # Qualifying simulation functions
└── README.md
```

---

## 📝 Limitations/assumptions

- Lap times are normally distributed.
- Limited to 2018 onwards as previous data is unavailable.

---

## ▶️ How to Run

Try the application live [**here**](https://f1-qualifying-monte-carlo-simulator.streamlit.app/Qualifying_simulator), or

1. Download all the files and keep the same folder structure.
2. Open a terminal and type `streamlit run Homepage.py` to run the app locally.
