# FAHIMTA Repository Architecture Baseline

**Document version:** 1.0.0  
**Baseline status:** FROZEN — reference snapshot before application-code changes  
**Snapshot date:** 2026-11-14  
**Repository:** `Coolestcoker/FAHIMTA`  
**Branch:** `main`  
**Snapshot commit:** `7839d8413bb0e27092dc5513439cb27a3151df48`  
**Snapshot tree:** `f6535c207303e87187ec2ea8c181362a95d6dbb1`

---

## 1. Baseline declaration and change control

This document freezes the repository architecture represented by the snapshot commit above. It is the reference point against which subsequent application-code changes, architectural decisions, tests, and research claims should be compared.

**Freeze rules**

1. Treat the snapshot commit and tree SHA as the baseline identity. Do not silently redefine this baseline when `main` advances.
2. Preserve this document as a historical reference. Future architecture changes should create a new baseline version or a clearly dated successor document.
3. Before changing application code, describe the intended change, affected modules, expected behaviour, test additions, and compatibility implications.
4. Do not change the existing score scale, rubric semantics, or evaluation methodology as an incidental part of unrelated engineering work.
5. Keep implementation evidence, software-test evidence, model provenance, and linguistic validation distinct.
6. Passing software tests do not establish Hausa semantic validity, target-model accuracy, reviewer agreement, or intervention effectiveness.

This is a documentation baseline. It does not itself modify or certify the application.

## 2. Executive architecture assessment

FAHIMTA is a Python research prototype / MVP scaffold for Hausa–Nigerian AI evaluation and improvement. Its initial target system is N-ATLaS; FAHIMTA complements that system and does not replace or rebuild it.

The repository contains a human-assigned overall-score evaluator, a lightweight evaluation record model, a documented 0–5 rubric, a threshold-based diagnosis utility, a diagnosis-to-recommendation utility, two test modules, one human-reviewed Hausa evaluation case, research documentation, and a GitHub Actions test workflow.

The repository does **not** implement one integrated Evaluate → Diagnose → Improve → Re-evaluate pipeline. The evaluator's reviewer-tag-derived status/action fields are distinct from the standalone threshold diagnosis and recommendation functions. The standalone functions are not orchestrated by `Evaluator.evaluate_case()`.

The direct FAHIMTA–N-ATLaS execution path is not implemented or verified. The adapter declaration is a protocol boundary, not a working model connection.

**Baseline conclusion:** human-scored evaluation-record validation is the most complete component. Diagnosis and recommendation exist as narrow utilities. Intervention execution, a re-evaluation workflow, persistent storage, and verified model integration are not present in the inspected snapshot.

## 3. Snapshot identity and inventory method

The baseline was inspected at repository `Coolestcoker/FAHIMTA`, branch `main`, commit `7839d8413bb0e27092dc5513439cb27a3151df48`, tree `f6535c207303e87187ec2ea8c181362a95d6dbb1`. The Git tree response was not truncated (`truncated=false`).

The source and test inventory is based on the complete Git tree and direct inspection of the listed source and test files. Status labels reflect code at this snapshot, not assumptions about future implementations.

## 4. Complete application source-module inventory

The snapshot contains eight Python source files: four package initializers and four functional modules.

| Path | Responsibility | Status | Notes |
|---|---|---|---|
| `src/__init__.py` | Root package declaration | Implemented | Package docstring |
| `src/evaluation/__init__.py` | Evaluation package declaration | Implemented | Package docstring |
| `src/evaluation/evaluator.py` | Validates and records human-assigned scores | Implemented, narrow scope | Main evaluation entry point |
| `src/evaluation/models.py` | Defines `EvaluationRecord` | Implemented, lightweight | Dataclass; no persistence |
| `src/diagnosis/__init__.py` | Diagnosis package declaration | Implemented | Package docstring |
| `src/diagnosis/diagnose.py` | Threshold-based diagnosis function | Partial | Numerical comparison, not semantic diagnosis |
| `src/improvement/__init__.py` | Improvement package declaration | Implemented | Package docstring |
| `src/improvement/recommend.py` | Diagnosis-to-action recommendation | Partial | Returns a string; does not execute an intervention |

### 4.1 Supporting repository files

| Path | Purpose |
|---|---|
| `README.md` | Project purpose, status, limitations, CI evidence |
| `docs/research-spec.md` | Research purpose, scope, evidence discipline |
| `docs/evaluation-method.md` | Human-assigned 0–5 scoring method and rubric |
| `docs/reproducibility.md` | Software-test and model reproducibility guidance |
| `docs/evaluator-architecture-audit.md` | Earlier evaluator-focused architecture audit |
| `tests/test_evaluator.py` | Evaluator behaviour tests |
| `tests/test_smoke.py` | Diagnosis and recommendation smoke tests |
| `examples/evaluation_record.json` | Example record template |
| `results/FAHIMTA-NATLAS-TEST-001.md` | Human-reviewed Hausa evaluation record |
| `results/github-actions-verification-2026-11-14.md` | GitHub Actions verification evidence |
| `.github/workflows/tests.yml` | GitHub Actions test workflow |
| `requirements-test.txt` | Pinned dependency: `pytest==9.0.2` |
| `.gitignore` | Git ignore configuration |
| `LICENSE` | Repository license |

This is the relevant source, test, research, evidence, and CI inventory for this baseline. Supporting files are not necessarily executable application components.

## 5. Functional module assessment

### 5.1 Evaluation — `src/evaluation/evaluator.py`

The entry point is `Evaluator.evaluate_case(...)`. Inputs include evaluation ID, input text, expected behaviour, captured N-ATLaS output, explicit overall score, reviewer tags, reviewer rationale, evaluation method, and optional timestamp/system version.

The implementation rejects blank required text, requires an explicit human score, rejects booleans/non-integers/out-of-range values, maps the score to a fixed label and description, derives generic diagnosis/action fields from the presence of reviewer tags, and returns an `EvaluationRecord`.

| Score | Label |
|---:|---|
| 0 | Unusable |
| 1 | Poor |
| 2 | Weak |
| 3 | Adequate |
| 4 | Strong |
| 5 | Excellent |

The score is a reviewer judgement. It is not inferred from input/output text, is not a probability, and is not a statistically validated benchmark measure.

**Boundary:** this module validates and records a human judgement. It does not automatically determine Hausa semantic accuracy, infer linguistic root causes, or establish model improvement.

### 5.2 Record model — `src/evaluation/models.py`

`EvaluationRecord` contains `evaluation_id`, `input`, `expected_behavior`, `n_atlas_output`, `evaluation_method`, `score`, `error_category`, `diagnosis`, `improvement_action`, `re_evaluation_result`, `timestamp`, and `version`.

It is a lightweight in-memory dataclass. The inspected implementation does not establish durable storage, database constraints, record lifecycle management, or a complete provenance chain. The `re_evaluation_result` field does not mean a re-evaluation workflow exists.

### 5.3 Diagnosis — `src/diagnosis/diagnose.py`

The function compares an explicit score to a threshold and returns `no_failure_detected` or `evaluation_failure`.

It does not inspect Hausa text, model output, reviewer rationale, or semantic dimensions. It does not classify linguistic errors or establish root causes. The inspected function does not validate the score or threshold domain.

**Boundary:** a minimal threshold utility exists; an evidence-based semantic diagnostic engine does not.

### 5.4 Improvement recommendation — `src/improvement/recommend.py`

The function maps `no_failure_detected` to `no_intervention`; other diagnosis strings map to `review_case_and_define_targeted_intervention`.

It does not modify a model, change a prompt, execute an intervention, orchestrate an experiment, preserve intervention provenance, or compare before-and-after outputs.

**Boundary:** a deterministic recommendation utility exists; an intervention engine does not.

### 5.5 N-ATLaS adapter boundary

`src/evaluation/evaluator.py` declares an `NAtlasAdapter` protocol with an `evaluate(input_text)` method. The inspected code does not instantiate an adapter, call a verified endpoint, authenticate to a target model, or establish a model ID/revision and generation configuration.

**Boundary:** interface declaration only; direct FAHIMTA–N-ATLaS execution is not implemented or verified.

## 6. Actual data flow versus intended research loop

The intended loop is **Evaluate → Diagnose → Improve → Re-evaluate**. Actual snapshot behaviour is narrower:

1. `Evaluator.evaluate_case()` validates reviewer-provided input, reference behaviour, captured output, method, and score.
2. The evaluator creates generic diagnosis/action fields based on the presence or absence of reviewer-supplied tags.
3. Separately, `diagnose()` compares a numerical score against a threshold.
4. Separately, `recommend()` maps a diagnosis string to a recommendation string.
5. No inspected orchestrator connects these standalone functions into one complete workflow.
6. No intervention is executed and no comparable re-evaluation is orchestrated.

The evaluator's tag-derived fields and the standalone diagnosis/recommendation functions must not be described as one integrated autonomous pipeline.

## 7. Source-to-test traceability

The repository contains two test modules.

| Source module | Corresponding test | Coverage | Assessment |
|---|---|---|---|
| `src/evaluation/evaluator.py` | `tests/test_evaluator.py` | Direct | Main functional test coverage |
| `src/evaluation/models.py` | `tests/test_evaluator.py` | Indirect | Record fields exercised through evaluator output; no dedicated model tests |
| `src/diagnosis/diagnose.py` | `tests/test_smoke.py` | Smoke | Both threshold outcomes exercised |
| `src/improvement/recommend.py` | `tests/test_smoke.py` | Smoke | Both expected recommendation paths exercised |
| Package initializers | None directly | None | Not separately tested |

### 7.1 Evaluator test cases

`tests/test_evaluator.py` covers all six score labels, recording the TEST-001 human judgement and reviewer tags, requiring an explicit score, rejecting invalid scores (negative, above 5, float, boolean, string), and rejecting blank required input text. Parametrization results in 14 executed cases in this module.

### 7.2 Diagnosis and recommendation tests

`tests/test_smoke.py` contains two tests: a score above threshold leads to `no_failure_detected` and `no_intervention`; a score below threshold leads to `evaluation_failure` and `review_case_and_define_targeted_intervention`.

These are smoke tests for simple functions, not validation of semantic diagnosis or intervention effectiveness.

### 7.3 Identified test gaps

The inspected tests do not independently verify:

1. Blank evaluation IDs.
2. Blank expected behaviour.
3. Blank captured target-system output.
4. Blank evaluation method.
5. Diagnosis threshold boundary conditions and invalid input domains.
6. Unknown diagnosis values and recommendation behaviour.
7. Record serialization, persistence, or lifecycle.
8. Re-evaluation workflow and comparison.
9. Actual N-ATLaS adapter execution.
10. End-to-end orchestration across all four research stages.

These are coverage gaps, not proof that every related behaviour is defective.

## 8. Implementation status register

Status definitions: **Implemented** means code or an artefact exists and its narrow behaviour is supported by inspection; **Partial** means a limited building block exists but the broader component is incomplete; **Missing** means no implementation was found in this complete repository snapshot; **Unverified** means evidence is insufficient to establish the claim or capability.

| Component | Status | Evidence and boundary |
|---|---|---|
| Human evaluation record validation | Implemented | `Evaluator.evaluate_case()` |
| Human-assigned overall 0–5 score | Implemented | Explicit score validation and recording |
| Six-level rubric | Implemented as documented method | Code and evaluation-method documentation; linguistic validation remains separate |
| Evaluation record structure | Implemented | `EvaluationRecord` dataclass |
| Reviewer-supplied diagnostic tags | Implemented | Stored as record context |
| Generic tag-derived diagnosis/action fields | Implemented, narrow | Assigned based on supplied tags |
| Threshold diagnosis utility | Partial | Numerical comparison only |
| Semantic/Hausa error diagnosis | Missing | No such engine found |
| Recommendation utility | Partial | Returns a string only |
| Intervention execution | Missing | No intervention runner found |
| Re-evaluation result field | Implemented | Dataclass field only |
| Re-evaluation workflow/comparison | Missing | No orchestration found |
| N-ATLaS adapter protocol | Partial | Interface declaration only |
| Verified N-ATLaS endpoint integration | Missing | No working adapter call found |
| Model ID/revision and settings verification | Unverified | TEST-001 records provenance limitations |
| Durable evaluation storage | Missing | No persistence layer found |
| Hausa reference/rubric expert validation | Unverified | One human-reviewed case; broader validation not established |
| Automated software tests | Implemented | Two test modules |
| GitHub Actions test workflow | Implemented | Python 3.11 and pinned pytest |
| Integrated four-stage research loop | Missing | No end-to-end orchestrator found |

## 9. Evaluation evidence and limits

The repository contains one documented human-reviewed Hausa case:

- **Record:** `FAHIMTA-NATLAS-TEST-001`
- **Input:** `Menene ake nufi da gwagwarmaya?`
- **Recorded score:** 3/5 — Adequate
- **Determination:** PASS WITH LIMITATIONS
- **Observed source:** public N-ATLaS-branded demonstration interface

The report describes the captured response as broadly correct but semantically narrow, with insufficient coverage of collective struggle, rights, freedom, justice, and social change.

The screenshot does not verify the exact backend model ID/revision, generation settings, or direct execution through FAHIMTA. The reference answer is a project-established human-review reference; further Hausa-language reviewer validation is recommended before formal benchmark use.

This is one qualitative, case-specific human judgement. It does not establish aggregate benchmark performance, overall Hausa-language model accuracy, statistical significance, model superiority, or improvement.

## 10. CI and software-test baseline

The workflow at `.github/workflows/tests.yml`:

- Runs on pushes and pull requests to `main`, and manual dispatch.
- Uses `ubuntu-latest` and Python 3.11.
- Installs `requirements-test.txt` (`pytest==9.0.2`).
- Runs `python -m pytest -q`.
- Uses `actions/checkout@v7` and `actions/setup-python@v7`.

Recorded evidence:

| Run | Evidence | Result |
|---|---|---|
| #13 | Preserved original workflow baseline | 16 tests passed in 0.03 seconds |
| #16 | Updated workflow; tested commit `e23bc55d9e10999719337d8dd00e3c2bbdb7717e` | 16 tests passed in 0.02 seconds |
| #17 | Documentation-triggered CI | Test job and listed steps completed successfully |

- [Run #16](https://github.com/Coolestcoker/FAHIMTA/actions/runs/43587660901)
- [Run #17](https://github.com/Coolestcoker/FAHIMTA/actions/runs/43589292260)
- [Verification record](https://github.com/Coolestcoker/FAHIMTA/blob/main/results/github-actions-verification-2026-11-14.md)

The source modules, test files, requirements file, and workflow in the frozen snapshot were checked against the run #17 tested tree and had matching Git blob hashes.

This supports continuity of the tested software snapshot. It does not establish linguistic validation, model provenance, or production readiness. No new local test execution is claimed by this document.

## 11. Architecture risks and constraints to preserve

1. **Human judgement versus automation:** reviewer-assigned scores/tags are not automated semantic evaluation.
2. **Diagnosis versus root cause:** a threshold result or reviewer tag does not prove a causal explanation.
3. **Recommendation versus intervention:** an action string is not an executed change.
4. **Re-evaluation field versus workflow:** a dataclass field is not a before/after experiment.
5. **Protocol versus integration:** an adapter protocol is not a verified N-ATLaS connection.
6. **Software tests versus research validity:** passing tests do not validate the Hausa rubric, reference answer, benchmark, or model.
7. **Single case versus benchmark:** TEST-001 remains a case-specific qualitative result.
8. **Snapshot versus current branch:** this baseline remains tied to its recorded commit even after `main` advances.

## 12. Recommended sequence for future architecture work

These are proposals, not implemented features or authorization to change application code.

1. **Interface and data-flow specification:** define module responsibilities, data contracts, diagnosis ownership, and the boundary between reviewer decisions and automated functions.
2. **Diagnostic taxonomy:** define observable error categories, inclusion/exclusion guidance, examples, reviewer attribution, and uncertainty.
3. **Intervention record:** distinguish recommended actions from actions actually performed; define intervention provenance.
4. **Re-evaluation protocol:** specify comparable inputs, references, rubric version, model configuration, output capture, and reporting rules.
5. **Verified model adapter:** implement only after an authorized endpoint and reproducible model/configuration identifiers are available.
6. **Persistence design:** specify record identity, versioning, storage, validation, and audit history before adding a database.
7. **Research validation:** expand the reviewed Hausa case set, validate references and rubric wording with qualified reviewers, and study reviewer consistency.

For each proposed change, identify affected modules, data contracts, tests, evidence requirements, and effect on the frozen baseline.

## 13. Baseline acceptance checklist

Use this checklist before authorizing the first application-code change:

- [ ] The proposed change cites this baseline version and snapshot commit.
- [ ] The target capability and its current status are stated accurately.
- [ ] Affected source modules and dependent modules are identified.
- [ ] Existing score scale and evaluation methodology are preserved unless separately approved.
- [ ] New or changed behaviours have explicit test cases.
- [ ] Model execution and provenance requirements are stated where applicable.
- [ ] Research validity claims are separated from software implementation claims.
- [ ] A new CI result is obtained for changed source.
- [ ] A successor architecture record is prepared if the architecture materially changes.

## 14. Version history

| Version | Date | Status | Description |
|---|---|---|---|
| 1.0.0 | 2026-11-14 | Frozen baseline | Initial repository-wide inventory, source-to-test map, implementation status register, evidence boundaries, and change-control declaration at commit `7839d8413bb0e27092dc5513439cb27a3151df48`. |

**End of baseline — version 1.0.0.**