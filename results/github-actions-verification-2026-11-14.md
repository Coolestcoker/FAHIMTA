# GitHub Actions Verification Record — 2026-11-14

## Purpose

Preserve the first confirmed successful GitHub-hosted Actions execution on the destination repository account after the FAHIMTA repository migration. This record documents the CI result without changing the tested commit, workflow, application code, evaluation logic, test methodology, or scoring.

## Run identity

- Repository: [Coolestcoker/FAHIMTA](https://github.com/Coolestcoker/FAHIMTA)
- Workflow: `FAHIMTA tests`
- Run number: **#13**
- Run ID: `43579108509`
- Run URL: https://github.com/Coolestcoker/FAHIMTA/actions/runs/43579108509
- Event: `workflow_dispatch`
- Triggering account: `Coolestcoker`
- Branch: `main`
- Commit: `aa65ae80b37d253defd5b1122bfdae2d2d82e40f`
- Run attempt: `1`
- Started: 2026-11-14 09:08:19 UTC
- Completed: 2026-11-14 09:08:32 UTC
- Observed duration: approximately **13 seconds**
- Workflow conclusion: **success**

## Execution environment

- GitHub-hosted runner version: `2.338.2`
- Runner image: `ubuntu-26.04` (resolved from the workflow's `ubuntu-latest` label at run time)
- Python: `3.11`
- Test dependency: `pytest==9.0.2`, installed from `requirements-test.txt`

## Test command and actual output

Command:

```bash
python -m pytest -q
```

Captured output:

```text
................                                                         [100%]
16 passed in 0.03s
```

The job's checkout, Python setup, dependency installation, and test execution steps all completed successfully.

## Non-blocking warnings

The captured job log reported:

1. A Node.js 20 deprecation warning affecting `actions/checkout@v4` and `actions/setup-python@v5`, with GitHub indicating that these actions were being forced to run under Node.js 24.
2. A Node.js `punycode` module deprecation warning during cleanup.
3. An `ubuntu-latest` runner-image migration notice concerning Ubuntu 26.

These warnings did not prevent the job from completing successfully.

## Scope and limitations

This record establishes that the existing test suite, as invoked by this workflow, completed successfully on the recorded commit and hosted runner.

It does **not** establish independent semantic benchmark validity, automated Hausa semantic accuracy, broad linguistic or cultural coverage, or production readiness. The current MVP remains reviewer-led: reviewers assign an overall score (0–5), provide written rationale and diagnostic tags, recommend improvements, and document re-evaluation.

The result must not be interpreted as proof that 16 tests validate Hausa semantic accuracy.

## Baseline and change control

Run #13 and commit `aa65ae80b37d253defd5b1122bfdae2d2d82e40f` are the CI maintenance baseline. Preserve this run and its commit as historical evidence. Any later workflow maintenance should be a separate, minimal change, reviewed and approved before implementation, then compared against this baseline.

No application code, evaluation logic, scoring methodology, test methodology, historical branches, or repository history was changed to produce this record.
