"""Orchestrate FAHIMTA's existing human-scored evaluation path.

This module coordinates the current evaluator and preserves reviewer
annotations as first-class workflow output. It deliberately does not invoke
the threshold diagnosis or recommendation utilities: those operations need
separately approved policies before they can be part of this workflow.
"""
from dataclasses import dataclass
from typing import Optional, Sequence

from src.evaluation.evaluator import Evaluator
from src.evaluation.models import EvaluationRecord


@dataclass(frozen=True)
class HumanEvaluationResult:
    """Result of one completed human evaluation and its reviewer annotations."""

    evaluation_record: EvaluationRecord
    reviewer_diagnostic_tags: tuple[str, ...]
    reviewer_rationale: Optional[str]
    status: str = "human_evaluation_recorded"


def run_human_evaluation(
    *,
    evaluation_id: str,
    input_text: str,
    expected_behavior: str,
    n_atlas_output: str,
    overall_score: int,
    diagnostic_tags: Optional[Sequence[str]] = None,
    reviewer_rationale: Optional[str] = None,
    evaluation_method: str = "human_rubric_v1",
    timestamp: Optional[str] = None,
    system_version: Optional[str] = None,
    evaluator: Optional[Evaluator] = None,
) -> HumanEvaluationResult:
    """Record a reviewer-assigned score and preserve its annotations.

    Validation and score interpretation remain the responsibility of the
    existing :class:`Evaluator`. No diagnosis threshold or recommendation is
    selected or executed here.
    """
    selected_evaluator = evaluator if evaluator is not None else Evaluator()
    tags = tuple(diagnostic_tags or ())

    record = selected_evaluator.evaluate_case(
        evaluation_id=evaluation_id,
        input_text=input_text,
        expected_behavior=expected_behavior,
        n_atlas_output=n_atlas_output,
        overall_score=overall_score,
        diagnostic_tags=tags,
        reviewer_rationale=reviewer_rationale,
        evaluation_method=evaluation_method,
        timestamp=timestamp,
        system_version=system_version,
    )

    return HumanEvaluationResult(
        evaluation_record=record,
        reviewer_diagnostic_tags=tags,
        reviewer_rationale=reviewer_rationale,
    )
