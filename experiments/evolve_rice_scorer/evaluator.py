"""
AlphaEvolve Evaluator for RICE Scorer Experiment
Evaluates candidate RICE scoring functions against ground-truth trade-off benchmarks.
"""

import json
import sys
import os
import argparse
import time
from initial_program import calculate_rice_score, evaluate_feature_swap

BENCHMARK_SCENARIOS = [
    {
        "new_feature": {"reach": 1000, "impact": 3.0, "confidence": 0.8, "effort": 5},
        "backlog": [
            {"id": "feat_a", "reach": 500, "impact": 1.0, "confidence": 0.5, "effort": 5},
            {"id": "feat_b", "reach": 2000, "impact": 3.0, "confidence": 0.9, "effort": 10},
            {"id": "feat_c", "reach": 800, "impact": 2.0, "confidence": 0.7, "effort": 5}
        ],
        "expected_swap": "feat_a"
    },
    {
        "new_feature": {"reach": 5000, "impact": 2.0, "confidence": 0.9, "effort": 8},
        "backlog": [
            {"id": "feat_x", "reach": 100, "impact": 1.0, "confidence": 0.3, "effort": 8},
            {"id": "feat_y", "reach": 4000, "impact": 3.0, "confidence": 0.9, "effort": 8}
        ],
        "expected_swap": "feat_x"
    }
]

def run_evaluation(output_file=None):
    start_time = time.time()
    correct = 0

    for scenario in BENCHMARK_SCENARIOS:
        res = evaluate_feature_swap(scenario["new_feature"], scenario["backlog"])
        swap = res.get("recommended_swap_out")
        if swap and swap["id"] == scenario["expected_swap"]:
            correct += 1

    accuracy = correct / len(BENCHMARK_SCENARIOS)
    elapsed_ms = (time.time() - start_time) * 1000

    fitness_score = accuracy * 0.9 + (1.0 if elapsed_ms < 50 else 0.5) * 0.1

    metrics = {
        "score": round(fitness_score, 4),
        "accuracy": round(accuracy, 4),
        "latency_ms": round(elapsed_ms, 2)
    }

    if output_file:
        with open(output_file, "w") as f:
            json.dump(metrics, f, indent=2)

    print(json.dumps(metrics))
    return metrics

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-file", type=str, help="Path to output JSON file")
    parser.add_argument("--program", type=str, help="Path to program file")
    args, unknown = parser.parse_known_args()

    run_evaluation(output_file=args.output_file)
