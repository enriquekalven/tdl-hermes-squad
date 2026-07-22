"""
Initial Seed Program for AlphaEvolve RICE Scorer Hill-Climbing
"""

# EVOLVE-BLOCK START
def calculate_rice_score(reach: float, impact: float, confidence: float, effort: float) -> float:
    """
    RICE Scoring function to rank backlog features and calculate trade-off value.
    Formula: (Reach * Impact * Confidence) / Effort
    """
    if effort <= 0:
        effort = 0.1
    return (reach * impact * confidence) / effort
# EVOLVE-BLOCK END

def evaluate_feature_swap(new_feature: dict, current_backlog: list) -> dict:
    """
    Evaluates 1-In, 1-Out scope swaps using the RICE score algorithm.
    """
    new_score = calculate_rice_score(
        new_feature["reach"], new_feature["impact"], new_feature["confidence"], new_feature["effort"]
    )
    
    candidates = []
    for item in current_backlog:
        score = calculate_rice_score(item["reach"], item["impact"], item["confidence"], item["effort"])
        diff = abs(item["effort"] - new_feature["effort"])
        candidates.append((diff, score, item))

    # Find equal-effort item with lowest score to swap out (1-Out)
    candidates.sort(key=lambda x: (x[0], x[1]))
    best_swap = candidates[0][2] if candidates else None

    return {
        "new_feature_score": new_score,
        "recommended_swap_out": best_swap
    }
