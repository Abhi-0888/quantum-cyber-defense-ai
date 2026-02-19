import numpy as np
import pandas as pd
import time

def generate_network_features():
    """
    Simulates network flow features.
    Returns:
        dict: A dictionary of features (e.g., packet_rate, bytes_sent, etc.)
    """
    # Simulate some features that might correlate with attacks
    is_attack = np.random.choice([0, 1], p=[0.8, 0.2])
    
    if is_attack:
        packet_rate = np.random.uniform(500, 2000)
        bytes_sent = np.random.uniform(10000, 50000)
    else:
        packet_rate = np.random.uniform(10, 100)
        bytes_sent = np.random.uniform(100, 2000)
        
    return {
        "timestamp": time.time(),
        "packet_rate": packet_rate,
        "bytes_sent": bytes_sent,
        "is_attack_sim": is_attack
    }

def get_threat_history(n=10):
    """
    Generates a history of simulated threats for visualization.
    """
    history = []
    for _ in range(n):
        history.append(generate_network_features())
    return pd.DataFrame(history)
