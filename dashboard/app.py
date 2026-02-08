import streamlit as st
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from quantum_threat_model.model import QuantumThreatModel
from ai_detection.detector import AIDetector
from risk_engine.scorer import RiskScorer

st.set_page_config(page_title="Quantum-Inspired AI Cybersecurity Engine", layout="wide")

st.title("🔐 Quantum-Inspired AI Cybersecurity Engine")
st.markdown("---")

# Sidebar
st.sidebar.header("Control Panel")
st.sidebar.button("Run Diagnostics")

# Main Content
col1, col2 = st.columns(2)

with col1:
    st.subheader("System Status")
    st.info("System is Online")

with col2:
    st.subheader("Recent Alerts")
    st.warning("No recent critical alerts")

st.markdown("---")
st.subheader("Live Threat Analysis")
st.write("Initializing components...")

# Initialize components
if st.button("Start Analysis"):
    qtm = QuantumThreatModel()
    ai = AIDetector()
    scorer = RiskScorer()
    
    st.write("Simulating analysis...")
    probs = qtm.evaluate(None)
    conf = ai.predict(None)
    score, level = scorer.calculate_score(probs, conf)
    
    st.write(f"Quantum Probabilities: {probs}")
    st.write(f"AI Confidence: {conf}")
    st.metric(label="Risk Level", value=level, delta=f"{score:.2f}")

