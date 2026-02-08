import sys
import os

from quantum_threat_model.model import QuantumThreatModel
from ai_detection.detector import AIDetector
from risk_engine.scorer import RiskScorer
from config import settings

def main():
    print(f"Starting Quantum-Inspired AI Cybersecurity Engine on port {settings.SERVER_PORT}...")
    
    # Initialize components
    qtm = QuantumThreatModel()
    ai = AIDetector()
    scorer = RiskScorer()
    
    # Simulate a single run
    print("Running initial diagnostics...")
    probs = qtm.evaluate(None)
    conf = ai.predict(None)
    score, level = scorer.calculate_score(probs, conf)
    
    print(f"Diagnostics complete. Risk Level: {level} (Score: {score:.2f})")
    print("System ready.")

if __name__ == "__main__":
    main()
