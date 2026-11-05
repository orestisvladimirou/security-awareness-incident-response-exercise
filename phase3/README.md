# Phase 3 — Awareness learning design and independent follow-up

**Version 0.3. Constructed example responses are not people, enrolled staff, actual training sessions or measured workforce performance.**

Four microlearning modules are linked to the original eight-question bank. The follow-up includes **24 fabricated answer choices across three named model profiles**, eight safe-action feedback mappings, four proposed delivery plans, ten open response actions and six improvement themes. This lets a reviewer verify the arithmetic without presenting artificial learner pass rates as genuine results.

- [Illustrative answer choices](data/illustrative_training_responses.csv)
- [Model-only scoring summaries](data/illustrative_training_scorecards.csv)
- [Question-to-feedback mapping](data/learning_feedback_map.csv)
- [Rollout design](data/awareness_rollout_plan.csv)
- [Response-action effectiveness gates](data/action_effectiveness_gates.csv)
- [Lessons linked to original actions](data/lessons_tracker.csv)
- [Employee learning methods](docs/11-learning-evaluation.md)
- [Corrective-action and privacy safeguards](docs/12-action-closure-and-privacy.md)

The actual v0.1 learning-metric baselines **remain `NOT MEASURED`**. All ten response actions remain **OPEN**; no worker or manager has attended or signed off anything.

Run `python scripts/score_training.py` to reproduce the model scores, not employee scores.
