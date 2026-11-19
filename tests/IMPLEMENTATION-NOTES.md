# FAHIMTA Gate 1 — implementation package

**Scope:** human evaluation orchestration and preservation of reviewer annotations only.

## Files to add

- `src/orchestration/__init__.py`
- `src/orchestration/human_evaluation.py`
- `tests/test_human_evaluation_orchestration.py`

No existing application, rubric, diagnosis, recommendation, CI, or research-method files are changed.

## Public interface

```python
from src.orchestration import run_human_evaluation

result = run_human_evaluation(
    evaluation_id="TEST-001",
    input_text="Menene ake nufi da gwagwarmaya?",
    expected_behavior="Explain the broad meaning in context.",
    n_atlas_output="Captured response text",
    overall_score=3,  # explicit human-assigned score
    diagnostic_tags=["semantic-narrowing"],
    reviewer_rationale="Broadly correct but narrow.",
)

record = result.evaluation_record
reviewer_tags = result.reviewer_diagnostic_tags
reviewer_rationale = result.reviewer_rationale
```

`HumanEvaluationResult.status` is `human_evaluation_recorded` when the existing evaluator successfully returns a record. Validation errors from that evaluator are allowed to propagate unchanged.

## Deliberate exclusions

This function does not call `diagnose()` or `recommend()`, select a threshold, infer a diagnosis, execute an intervention, re-evaluate a model, persist data, or contact N-ATLaS.

## Verification

The implementation was tested in a reconstructed local snapshot with the existing 16 tests plus four new tests: **20 passed**. Re-run `python -m pytest -q` in the actual repository after adding the files, then confirm GitHub Actions succeeds on the resulting commit.

## Apply

Copy the three files into the matching paths in the repository. No existing files need replacement.
