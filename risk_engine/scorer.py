class RiskScorer:
    def __init__(self):
        print("RiskScorer initialized")

    def calculate_score(self, quantum_probs, ai_confidence):
        """
        Combine Quantum probabilities and AI confidence into a final risk score.
        """
        # Weighted threat: higher weight to non-normal states
        threat_score = 1.0 - quantum_probs.get("Normal", 1.0)
        
        # Combine with AI confidence
        final_score = (threat_score * 0.7) + (ai_confidence * 0.3)
        
        if final_score < 0.3:
            level = "Low"
        elif final_score < 0.7:
            level = "Medium"
        else:
            level = "High"
            
        return final_score, level
