import pytest

from src.orchestration import HumanEvaluationResult, run_human_evaluation


def _run(**overrides):
    values = {
        "evaluation_id": "TEST-ORCHESTRATION-001",
        "input_text": "Menene ake nufi da gwagwarmaya?",
        "expected_behavior": "Explain the broad meaning in context.",
        "n_atlas_output": "A captured sample response.",
        "overall_score": 3,
    }
    values.update(overrides)
    return run_human_evaluation(**values)


def test_orchestration_records_human_evaluation_and_annotations():
    tags = ["semantic-narrowing", "omitted-collective-scope"]
    result = _run(
        diagnostic_tags=tags,
        reviewer_rationale="Broadly correct but narrow.",
        timestamp="2026-11-14",
    )

    assert isinstance(result, HumanEvaluationResult)
    assert result.status == "human_evaluation_recorded"
    assert result.evaluation_record.evaluation_id == "TEST-ORCHESTRATION-001"
    assert result.evaluation_record.score == 3.0
    assert result.reviewer_diagnostic_tags == tuple(tags)
    assert result.reviewer_rationale == "Broadly correct but narrow."
    assert result.evaluation_record.error_category == ",".join(tags)


def test_orchestration_preserves_empty_annotations_without_inventing_them():
    result = _run()

    assert result.reviewer_diagnostic_tags == ()
    assert result.reviewer_rationale is None
    assert result.evaluation_record.diagnosis == "no_issue_tagged_by_reviewer"


def test_orchestration_delegates_score_validation_to_existing_evaluator():
    with pytest.raises(ValueError, match="integer from 0 to 5"):
        _run(overall_score=6)


def test_orchestration_does_not_mutate_or_replace_evaluator_record_fields():
    result = _run(
        diagnostic_tags=["reviewer-observation"],
        reviewer_rationale="Reviewer supplied rationale.",
        system_version="unverified-demo",
    )

    assert result.evaluation_record.score == 3.0
    assert "unverified-demo" in result.evaluation_record.evaluation_method
    assert "Reviewer supplied rationale." in result.evaluation_record.evaluation_method
