# 🔐 Quantum-Inspired AI Cybersecurity Engine

## 📌 Overview

**Quantum-Inspired AI Cybersecurity Engine** is a real-world, intelligent threat-detection system that combines **artificial intelligence** with **quantum-inspired probabilistic modeling** to detect cyber attacks efficiently on classical computing systems.

Instead of making simple binary decisions (safe or unsafe), the system evaluates **multiple possible attack scenarios in parallel** using probability-based reasoning inspired by quantum concepts. This approach improves detection accuracy, reduces false positives, and enables adaptive, future-ready cybersecurity defense.

> ⚠️ This project does **not** require real quantum hardware. It applies **quantum-inspired ideas** using classical computation.

---

## 🎯 Project Objectives

* Build an **end-to-end cybersecurity detection engine**
* Detect **known and unknown network attacks**
* Apply **quantum-inspired probability models** for threat evaluation
* Use **AI/ML models** for anomaly detection
* Generate **risk-based security decisions**
* Design a **real-world, deployable architecture**
* Demonstrate **future-oriented cybersecurity expertise**

---

## 🧠 Why Quantum-Inspired Cybersecurity?

Traditional Intrusion Detection Systems (IDS):

* Use static rules
* Generate high false positives
* Fail against evolving threats

Quantum-inspired systems:

* Evaluate **multiple threat possibilities at once**
* Work with **probabilities instead of fixed rules**
* Make smarter, adaptive decisions
* Are suitable for **post-quantum cybersecurity thinking**

This project bridges **Cybersecurity + AI + Quantum Computing concepts**, making it highly relevant for modern security roles.

---

## 🏗️ System Architecture

```
┌──────────────────┐
│ Data Ingestion   │
│ (Network Logs)   │
└─────────┬────────┘
          ↓
┌──────────────────┐
│ Feature          │
│ Engineering      │
└─────────┬────────┘
          ↓
┌──────────────────┐
│ Quantum-Inspired │
│ Threat Modeling  │
└─────────┬────────┘
          ↓
┌──────────────────┐
│ AI Detection     │
│ Engine           │
└─────────┬────────┘
          ↓
┌──────────────────┐
│ Risk Scoring &   │
│ Decision Engine  │
└─────────┬────────┘
          ↓
┌──────────────────┐
│ Alerts &         │
│ Response System  │
└──────────────────┘
```

---

## ⚙️ How the System Works

### 1️⃣ Data Ingestion & Simulation
* **Live Simulator:** Generates synthetic network features (packet rate, bytes sent) to simulate real-world traffic patterns and attack scenarios.

### 2️⃣ Quantum-Inspired Threat Modeling
* **Probabilistic States:** Each network flow is modeled as a superposition of threat states (Normal, Brute Force, DDoS, Port Scan).
* **Quantum Evaluation:** Uses `numpy` Dirichlet distributions to evaluate multiple possibilities simultaneously.

### 3️⃣ AI Detection Engine
* **Anomaly Detection:** Refined confidence scoring based on simulated feature vectors, providing a second layer of validation.

### 4️⃣ Risk Scoring & Decision Engine
* **Weighted Integration:** Combines Quantum probabilities (70% weight) and AI confidence (30% weight) to produce a final risk score.
* **Dynamic Thresholds:** Categorizes risk into Low, Medium, and High based on the combined score.

### 5️⃣ Interactive Dashboard
* **Real-time Monitoring:** Built with Streamlit, providing live metrics and history.
* **Visualizations:**
  * **Risk Score History:** Trace the progression of risk over time.
  * **Quantum State Distribution:** Pie charts showing the breakdown of probable threats.

---

## 🧪 Technology Stack

| Category               | Technology                               |
| ---------------------- | ---------------------------------------- |
| Language               | Python 3.14+                             |
| AI / ML Confidence     | Custom Probabilistic Logic               |
| Quantum-Inspired Logic | NumPy (Dirichlet Distributions)          |
| Data Handling          | Pandas                                   |
| Visualization          | Plotly, Streamlit                        |
| Deployment             | Ready for Cloud/On-Prem                  |

---

## 🚀 How to Run

1. **Install Dependencies:**
   ```bash
   py -m pip install numpy pandas plotly streamlit
   ```

2. **Run Diagnostics (CLI):**
   ```bash
   py main.py
   ```

3. **Launch Dashboard:**
   ```bash
   streamlit run dashboard/app.py
   ```

---

## 🧠 Key Highlights for Recruiters

✅ Combines **Cybersecurity + AI + Quantum Concepts**
✅ Real-world problem solving
✅ No fake quantum claims
✅ Production-oriented design
✅ Future-ready security thinking

---

## 🎤 Interview Explanation (Short Pitch)

> “This project is a Quantum-Inspired AI Cybersecurity Engine that detects cyber attacks by evaluating multiple threat probabilities in parallel. It combines AI-based anomaly detection with quantum-inspired probabilistic reasoning to reduce false positives and improve real-time security decisions, all running on classical hardware.”

---

## 📌 Future Enhancements

* Real-time packet capture integration
* Post-quantum cryptography integration
* SOAR automation support
* Cloud deployment (AWS / Azure)
* SIEM integration

---

## 🏆 Final Note

This project demonstrates **advanced cybersecurity thinking**, strong **AI fundamentals**, and **quantum-inspired innovation**, making it ideal as a **core project for cybersecurity placements**.

---