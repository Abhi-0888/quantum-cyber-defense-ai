import streamlit as st
import sys
import os
import time
import pandas as pd
import plotly.express as px

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from quantum_threat_model.model import QuantumThreatModel
from ai_detection.detector import AIDetector
from risk_engine.scorer import RiskScorer
from utils.simulator import generate_network_features

st.set_page_config(
    page_title="Quantum AI Cyber Defense",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for glassmorphism effect
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stMetric {
        background: rgba(255, 255, 255, 0.05);
        padding: 15px;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔐 Quantum-Inspired AI Cybersecurity Engine")
st.markdown("---")

# Initialize Session State
if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=['Time', 'Score', 'Level'])
if 'running' not in st.session_state:
    st.session_state.running = False

# Sidebar
with st.sidebar:
    st.header("⚡ Control Panel")
    if st.button("🚀 Start Monitoring"):
        st.session_state.running = True
    if st.button("🛑 Stop Monitoring"):
        st.session_state.running = False
    
    st.markdown("---")
    st.subheader("Engine Stats")
    st.write(f"Quantum States: 4")
    st.write(f"AI Model: IsolationForest (Simulated)")

# Initialize Components
qtm = QuantumThreatModel()
ai = AIDetector()
scorer = RiskScorer()

# Main Layout
col1, col2, col3 = st.columns(3)

# Real-time Simulation Loop
if st.session_state.running:
    # Get simulated features
    features = generate_network_features()
    
    # Engine Logic
    probs = qtm.evaluate(features)
    conf = ai.predict(features)
    score, level = scorer.calculate_score(probs, conf)
    
    # Update History
    new_data = pd.DataFrame({
        'Time': [time.strftime("%H:%M:%S")], 
        'Score': [score], 
        'Level': [level]
    })
    st.session_state.history = pd.concat([st.session_state.history, new_data]).tail(20)

    # Metrics
    with col1:
        color = "red" if level == "High" else "orange" if level == "Medium" else "green"
        st.metric("Final Risk Score", f"{score:.2f}", delta=level, delta_color="inverse")
    
    with col2:
        st.metric("Network Load", f"{features['packet_rate']:.0f} pkts/s")
        
    with col3:
        st.metric("AI Confidence", f"{conf:.2%}")

    st.markdown("---")
    
    # Visualizations
    vcol1, vcol2 = st.columns([2, 1])
    
    with vcol1:
        st.subheader("📈 Risk Score History")
        fig_line = px.line(st.session_state.history, x='Time', y='Score', 
                           title="Real-time Risk Progression",
                           template="plotly_dark",
                           color_discrete_sequence=['#00ffcc'])
        st.plotly_chart(fig_line, use_container_width=True)
        
    with vcol2:
        st.subheader("🎯 Threat Distribution")
        prob_df = pd.DataFrame(list(probs.items()), columns=['Threat', 'Probability'])
        fig_pie = px.pie(prob_df, values='Probability', names='Threat', 
                         title="Quantum Probability States",
                         hole=0.4,
                         template="plotly_dark")
        st.plotly_chart(fig_pie, use_container_width=True)

    time.sleep(1)
    st.rerun()

else:
    st.info("👈 Use the Sidebar to start monitoring network traffic.")
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=800&q=80", caption="Quantum Defensive Shield")

