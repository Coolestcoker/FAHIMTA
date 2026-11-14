# FAHIMTA Evaluator Architecture Audit

**Audit date:** 2026-11-14  
**Repository:** `Coolestcoker/FAHIMTA`  
**Branch:** `main`  
**Purpose:** Source-based audit of the current MVP evaluator and its documented workflow.  
**Change boundary:** Documentation only. No application code, scoring rules, or test methodology changed.

## 1. Executive assessment

FAHIMTA currently implements a narrow human-review record path. The evaluator validates required text fields and a reviewer-assigned integer score from 0 to 5, then creates an `EvaluationRecord`. Reviewer-supplied tags and rationale are stored as diagnostic context, and the record receives a simple follow-up action string.

This is a useful transparent MVP foundation, but it is not an automated Hausa semantic evaluator, an autonomous diagnostic engine, an implemented improvement engine, or a verified N-ATLaS integration.

**Assessment:** suitable to continue as a controlled research prototype. Claims should remain limited to the implemented record-validation behaviour, documented rubric, one human-reviewed case, and verified software test evidence.

## 2. Sources inspected

The audit inspected the current repository versions of:

- `README.md`
- `src/evaluation/evaluator.py`
- `src/evaluation/models.py`
- `tests/test_evaluator.py`
- `docs/evaluation-method.md`
- `docs/research-spec.md`
- `results/FAHIMTA-NATLAS-TEST-001.md`
- `.github/workflows/tests.yml`
- `requirements-test.txt`

The audit also considered the supplied FAHIMTA readiness audit dated 2026-10-23, project technical development brief dated 2026-10-09, N-ATLaS TEST-001 standard evaluation report, and supplied test-execution report. Earlier findings from those documents are treated as historical context where newer repository evidence supersedes them.

## 3. Implemented evaluator behaviour

### 3.1 Evaluator entry point

`Evaluator.evaluate_case(...)` accepts:

- `evaluation_id`
- `input_text`
- `expected_behavior`
- `n_atlas_output`
- `overall_score`
- `diagnostic_tags`
- `reviewer_rationale`
- `evaluation_method`
- optional `timestamp`
- optional `system_version`

It rejects blank required text, a missing score, booleans, non-integers, and integers outside 0–5. The explicit boolean rejection is important in Python because `bool` is a subclass of `int`.

The evaluator maps the selected score to a fixed label and description, and returns an `EvaluationRecord`. The score is converted to a float in the record.

### 3.2 Score semantics

The current six-level rubric is:

| Score | Label |
|---:|---|
| 0 | Unusable |
| 1 | Poor |
| 2 | Weak |
| 3 | Adequate |
| 4 | Strong |
| 5 | Excellent |

The score is a human judgement. It is not inferred from the input/output text, a probability, an automated semantic score, or a statistically validated measure.

### 3.3 Record model

The inspected `EvaluationRecord` dataclass contains evaluation ID, input, optional expected behaviour and output, evaluation method, score, error category, diagnosis, improvement action, re-evaluation result, timestamp, and a default version string.

The model is a lightweight data structure. The inspected implementation does not establish persistent storage, database constraints, record lifecycle management, or a complete provenance chain.

## 4. Diagnosis boundary

Diagnostic tags are supplied by the reviewer. If tags exist, the evaluator records the generic diagnosis `reviewer_flagged_limitations`; otherwise it records `no_issue_tagged_by_reviewer`.

The evaluator does not independently inspect language semantics, classify errors, infer causal root causes, or validate whether a tag is correct. A tag is a reviewer annotation, not proof of a root cause.

The current tests verify that supplied tags are carried into the record and that a tagged case receives the expected generic diagnosis state.

## 5. Improvement and re-evaluation boundary

The evaluator assigns one of two simple follow-up action strings:

- With tags: `review_tagged_issues_and_re_evaluate`.
- Without tags: `retain_record_and_monitor`.

This is a recommendation label, not an executed intervention. The inspected code does not implement a model-editing process, prompt intervention runner, experiment orchestration, or an automatic before/after comparison.

Although the record model has a `re_evaluation_result` field, the inspected evaluator does not populate it. No claim of measured improvement is supported by this code path.

## 6. N-ATLaS integration boundary

The evaluator defines an `NAtlasAdapter` protocol with an `evaluate(input_text)` method. This defines an interface shape only. The inspected evaluator does not instantiate an adapter, make a network request, authenticate to a model endpoint, or verify a model identifier/revision or generation settings.

The TEST-001 evidence is a human review of a response seen in a public N-ATLaS-branded demonstration interface. Its report explicitly says the backend model revision, generation settings, and direct FAHIMTA execution path are not independently verified.

## 7. Test evidence

The inspected `tests/test_evaluator.py` covers:

- All six score labels and score recording.
- Recording the TEST-001 human judgement and its supplied tags.
- Requiring an explicit human score.
- Rejecting invalid scores, including `True`.
- Rejecting blank required text.

The repository's current GitHub Actions workflow uses Python 3.11, installs `requirements-test.txt` (which pins `pytest==9.0.2`), and runs `python -m pytest -q`.

Run #16's supplied execution log reports **16 passed in 0.02s** on commit `e23bc55d9e10999719337d8dd00e3c2bbdb7717e`. Run #17's GitHub job record reports the test job and all listed steps completed successfully. The original run #13 baseline is preserved separately.

These results establish that the current automated test suite passed in the recorded CI runs. They do not validate the linguistic quality of the reference answer, inter-rater reliability, multi-case benchmark performance, or the efficacy of interventions.

## 8. Findings and gaps

| Area | Current evidence | Gap / boundary |
|---|---|---|
| Evaluation | Human-assigned 0–5 overall score validated and recorded | No automatic semantic evaluation; no dimension-level inputs |
| Rubric | Six score labels/descriptions documented in code and method | Hausa expert validation and reviewer calibration remain necessary |
| Diagnosis | Reviewer tags stored; generic diagnosis state selected | No automated classification or root-cause validation |
| Improvement | Generic follow-up action string recorded | No intervention execution or intervention provenance |
| Re-evaluation | Record has a result field | Evaluator does not populate or compare it |
| Model integration | Adapter protocol declared | No verified endpoint call, model revision, or settings |
| Evidence | One human-reviewed TEST-001 case | No broad benchmark, statistical analysis, or inter-rater study |
| Persistence | Dataclass record returned | Durable storage and lifecycle not established by inspected files |

The audit did not find source files at the anticipated paths `src/diagnosis/diagnoser.py` or `src/improvement/recommender.py`. This is not proof that no related code exists elsewhere; it means those assumed paths were not available for inspection during this audit. The repository tree should be inventoried before making module-level claims about other diagnosis or improvement files.

## 9. Recommended next steps (proposals, not implemented)

1. **Repository inventory:** enumerate the complete current tree and map every module, test, example, and documentation file to its actual path.
2. **Evaluation-record specification:** define required provenance fields (reviewer identity/role where appropriate, rubric version, source evidence reference, model ID/revision, settings, capture time, and language variety) before changing the schema.
3. **Hausa review protocol:** have qualified Hausa reviewers assess the reference answer, rubric wording, dialect/context assumptions, and examples. Record disagreements rather than hiding them.
4. **Reviewer consistency study:** design a multi-reviewer pilot and report agreement transparently. Select an appropriate agreement statistic only after the study design and data are defined.
5. **Diagnostic taxonomy:** define observable error categories with inclusion/exclusion guidance and examples; retain reviewer attribution and uncertainty.
6. **Intervention record:** distinguish recommendation from action taken. Record intervention description, owner, date, target configuration, and evidence.
7. **Re-evaluation protocol:** preserve comparable input, reference, rubric version, target model/configuration, and output. Report differences without claiming causality unless the design supports it.
8. **Verified model execution:** implement an adapter only after an authorized, documented endpoint and reproducible model/configuration identifiers are available.
9. **Broader validation:** assemble a reviewed, versioned case set before claiming benchmark-level results.

These are proposals for future work. They do not authorize changes to the score scale, evaluation methodology, or application implementation.

## 10. Scope and limitations of this audit

This is a source-based architecture audit of the files listed in Section 2, not a security audit, independent Hausa linguistic validation, full repository test execution, or production-readiness assessment. The CI results are cited as separate execution evidence. Uninspected paths and unverified integrations remain open questions.

**Change-control statement:** This audit and the corresponding README reconciliation are documentation updates only. No application source, score definitions, rubric, test code, or test methodology was modified.