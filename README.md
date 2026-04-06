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

## ⚙️ How it works

- With each session of qualifying (Q1, Q2, Q3), a normal distribution is modelled from the driver's real lap times.
- If a driver did not take part in a session, and infite lap time is generated for them.
- The average number of laps (n) for that session is then calculated, and a Monte Carlo simulation run with n samples from the driver's lap distribution.
- For Q1, the top 15 (or 16 in 2026, it automatically adjust) drivers progress into Q2, with the eliminated drivers' positions fixed.
- Q2 lap times are generated in the same was as Q1.
- For drivers who did not make it into that session in real life but did in the simulation, an average time delta between sessions is calculated (only using the real times), and then applied to their previous session lap time.
- 

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
