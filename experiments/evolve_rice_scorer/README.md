# 🧬 AlphaEvolve Experiment: RICE Scorer Hill-Climbing

This experiment uses **AlphaEvolve (AE)** to hill-climb the RICE feature prioritization and scope swap algorithm.

## 📂 Files

- `initial_program.py`: Contains the target function wrapped in `# EVOLVE-BLOCK START` / `# EVOLVE-BLOCK END`.
- `evaluator.py`: Evaluates candidate programs against ground-truth trade-off scenarios and outputs JSON fitness metrics.
- `problem_description.md`: Explains the search space and fitness criteria.

## 🚀 Running the Experiment with AlphaEvolve CLI (`ae`)

```bash
cd experiments/evolve_rice_scorer

# 1. Test evaluator locally
python3 evaluator.py

# 2. Launch evolutionary search via AlphaEvolve CLI
ae experiment create --config .evolve/experiment_description.json
ae experiment launch
```
