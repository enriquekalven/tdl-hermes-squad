# AlphaEvolve Problem Description: RICE Scorer Hill-Climbing

## Objective
Evolve the Python function `calculate_rice_score()` inside `initial_program.py` to maximize trade-off decision accuracy and 1-in-1-out scope swap precision during Delta TDL engagements.

## Search Space
- **Target File**: `initial_program.py`
- **Evolve Block**: `# EVOLVE-BLOCK START ... # EVOLVE-BLOCK END`
- **Evaluator**: `evaluator.py`

## Fitness Criteria
1. **Accuracy (90%)**: Correctly identifies the lowest-ROI equal-effort feature to eject from sprint scope.
2. **Execution Latency (10%)**: Completes evaluation under 50ms.
