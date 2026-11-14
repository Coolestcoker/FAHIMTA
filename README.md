# FAHIMTA

**Hausa–Nigerian AI Evaluation & Improvement Framework**

FAHIMTA is a research and engineering framework for evaluating, diagnosing, and supporting improvement of Hausa/Nigerian-language AI systems.

The initial target system is **N-ATLaS**. FAHIMTA complements N-ATLaS; it does not replace or rebuild it.

## MVP research loop

**Evaluate → Diagnose → Improve → Re-evaluate**

The MVP focuses on a narrow, documented evaluation path rather than a broad platform.

## Current status (2026-11-14)

FAHIMTA remains a **research prototype / MVP scaffold**. The repository contains a reviewer-assigned overall-score evaluator, a documented 0–5 rubric, one human-reviewed Hausa case, and an automated test suite.

The evaluator validates and records a score explicitly assigned by a human reviewer. It does **not** automatically determine Hausa semantic accuracy, infer root causes, or generate evidence that an intervention improved a model. Diagnostic tags and follow-up actions are reviewer-supplied.

The direct FAHIMTA–N-ATLaS execution path is **not implemented or verified**. The available adapter is a protocol boundary, not a working connection to a verified N-ATLaS endpoint or model revision.

## CI verification

GitHub Actions now runs on pushes and pull requests to `main`, as well as manual dispatch. The workflow uses:

- Ubuntu-hosted GitHub Actions runner.
- Python 3.11.
- `pytest==9.0.2`, installed from `requirements-test.txt`.
- `python -m pytest -q`.
- `actions/checkout@v7` and `actions/setup-python@v7`.

**Verified evidence:**

- **Run #13 — preserved baseline:** 16 tests passed in 0.03 seconds on the original workflow.
- **Run #16 — updated workflow:** 16 tests passed in 0.02 seconds; tested commit `e23bc55d9e10999719337d8dd00e3c2bbdb7717e`. [View run #16](https://github.com/Coolestcoker/FAHIMTA/actions/runs/43587660901).
- **Run #17 — documentation-triggered CI:** GitHub reports the test job and all listed steps completed successfully. [View run #17](https://github.com/Coolestcoker/FAHIMTA/actions/runs/43589292260).

The current evidence supports successful execution of the existing 16-test suite in GitHub Actions using Python 3.11. It does not establish benchmark validity, broad linguistic accuracy, statistical reliability, or production readiness. See [the verification record](results/github-actions-verification-2026-11-14.md).

## Repository structure

```text
FAHIMTA/
├── README.md
├── docs/
│   ├── research-spec.md
│   ├── evaluation-method.md
│   ├── reproducibility.md
│   └── evaluator-architecture-audit.md
├── src/
│   ├── evaluation/
│   ├── diagnosis/
│   └── improvement/
├── tests/
├── examples/
└── .github/workflows/tests.yml
```

## Latest evaluation result

**Test record:** [FAHIMTA-NATLAS-TEST-001](results/FAHIMTA-NATLAS-TEST-001.md)

- **Input:** “Menene ake nufi da gwagwarmaya?”
- **Review:** Human evaluation against the project-established Hausa standard reference.
- **Result:** **3/5 — Adequate; PASS WITH LIMITATIONS.**
- **Finding:** The captured response broadly explains effort and overcoming difficulty, but narrows *gwagwarmaya* toward confrontation and omits important rights-based, collective, and social-change meanings.
- **Evidence limitation:** The response was captured from a public N-ATLaS-branded demo. Exact backend revision/settings and direct FAHIMTA integration remain unverified.

This is one qualitative human-reviewed case, not an aggregate benchmark result.

## Evaluator implementation boundary

The evaluator in `src/evaluation/evaluator.py` validates and records:

- Required evaluation ID, input, expected behaviour, captured output, and method fields.
- One human-assigned integer overall score from **0 to 5**.
- Reviewer-supplied diagnostic tags and rationale.
- Optional timestamp and system-version context.

The implementation does not accept dimension-level ratings, calculate a mean across dimensions, or score semantic content automatically. The adapter protocol does not itself perform an N-ATLaS call. See [the evaluation method](docs/evaluation-method.md) and [the evaluator architecture audit](docs/evaluator-architecture-audit.md).

## Evidence discipline and limitations

No benchmark scores, statistical significance, model superiority, automated semantic-accuracy, or production-readiness claims are made without supporting evidence. One reviewed case cannot establish general Hausa or Nigerian-language model performance.

Further work is required on Hausa reference validation, multi-case evaluation, reviewer consistency, verified model provenance and execution, documented interventions, comparable re-evaluation, and external validation.