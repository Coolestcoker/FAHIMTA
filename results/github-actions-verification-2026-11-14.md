# GitHub Actions Verification Record — 2026-11-14

## Purpose

Preserve confirmed GitHub-hosted Actions executions on the destination repository account after the FAHIMTA repository migration. This record documents the original CI baseline (run #13) and the subsequent workflow-maintenance verification (run #16).

## Verification history

| Run | Trigger | Workflow configuration | Result |
|---|---|---|---|
| [#13](https://github.com/Coolestcoker/FAHIMTA/actions/runs/43579108509) | `workflow_dispatch` | Original actions versions (`checkout@v4`, `setup-python@v5`) | Success; 16 passed |
| #16 | `workflow_dispatch` | Updated actions versions (`checkout@v7`, `setup-python@v7`) | Success; 16 passed |

Run #13 remains the historical baseline. Run #16 verifies the updated workflow and does not replace or rewrite the baseline evidence.

---

## Run #13 — Original CI baseline

### Run identity

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

### Execution environment

- GitHub-hosted runner version: `2.338.2`
- Runner image: `ubuntu-26.04` (resolved from the workflow's `ubuntu-latest` label at run time)
- Python: `3.11`
- Test dependency: `pytest==9.0.2`, installed from `requirements-test.txt`

### Test command and actual output

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

### Non-blocking warnings

The captured job log reported:

1. A Node.js 20 deprecation warning affecting `actions/checkout@v4` and `actions/setup-python@v5`, with GitHub indicating that these actions were being forced to run under Node.js 24.
2. A Node.js `punycode` module deprecation warning during cleanup.
3. An `ubuntu-latest` runner-image migration notice concerning Ubuntu 26.

These warnings did not prevent the job from completing successfully.

---

## Run #16 — Updated workflow verification

### Run identity

- Repository: [Coolestcoker/FAHIMTA](https://github.com/Coolestcoker/FAHIMTA)
- Workflow: `FAHIMTA tests`
- Run number: **#16**
- Run URL: Not recorded in the supplied run evidence; see the [repository Actions page](https://github.com/Coolestcoker/FAHIMTA/actions).
- Event: `workflow_dispatch` (manual request)
- Triggering account: `Coolestcoker`
- Branch: `main`
- Tested commit: `e23bc55d9e10999719337d8dd00e3c2bbdb7717e`
- Workflow conclusion: **success**
- Duration shown on the run list: approximately **11 seconds**
- Job result shown in the job view: **successful in 7 seconds**
- Runner version: `2.338.2`

### Workflow maintenance applied

Only the two action references were updated:

```yaml
- name: Check out repository
  uses: actions/checkout@v7
- name: Set up Python
  uses: actions/setup-python@v7
```

The remaining workflow configuration was retained:

- Triggers: `push` to `main`, `pull_request` to `main`, and `workflow_dispatch`
- Permissions: `contents: read`
- Runner label: `ubuntu-latest`
- Python version: `3.11`
- Dependency installation: `python -m pip install -r requirements-test.txt`
- Test command: `python -m pytest -q`

### Resolved action revisions observed in the run log

- `actions/checkout@v7` — `3d3c42e5aac5ba805825da76410c181273ba90b1`
- `actions/setup-python@v7` — `6d4fd22b20465ccc0f7354476588e8df7c9ca0e0`

### Execution evidence

The job completed all listed steps successfully:

1. Set up job
2. Check out repository
3. Set up Python
4. Install pinned test dependency
5. Run test suite
6. Post Set up Python
7. Post Check out repository
8. Complete job

The log confirms:

- Runner version: `2.338.2`
- Python setup completed.
- `pytest==9.0.2` installed successfully from `requirements-test.txt`.
- Checkout resolved the tested commit to `e23bc55d9e10999719337d8dd00e3c2bbdb7717e`.

Test command:

```bash
python -m pytest -q
```

Captured output:

```text
................                                                         [100%]
16 passed in 0.02s
```

**Run #16 result: SUCCESS — all 16 existing tests passed.**

### Interpretation

Run #16 confirms that the existing test suite passes after updating the workflow action references to `actions/checkout@v7` and `actions/setup-python@v7`, using the recorded runner and Python environment.

This is a CI maintenance verification. It does not establish independent semantic benchmark validity, automated Hausa semantic accuracy, broad linguistic or cultural coverage, or production readiness.

The result must not be interpreted as proof that 16 tests validate Hausa semantic accuracy.

---

## Scope and limitations

The current FAHIMTA MVP remains reviewer-led:

1. Evaluate
2. Diagnose
3. Improve
4. Re-evaluate

Reviewers assign an overall score (0–5), provide written rationale and diagnostic tags, recommend improvements, and document re-evaluation.

The CI results establish that the existing automated test suite completed successfully under the recorded workflow configurations. They do not independently validate the quality or correctness of reviewer judgments, linguistic coverage, or benchmark validity.

## Baseline and change control

- Preserve run #13 and commit `aa65ae80b37d253defd5b1122bfdae2d2d82e40f` as the original CI baseline.
- Preserve run #16 and commit `e23bc55d9e10999719337d8dd00e3c2bbdb7717e` as the updated-workflow verification.
- The workflow maintenance was limited to the two action-version references described above.
- The Python version, dependency pin, test command, workflow triggers, and permissions remained unchanged.
- No application code, evaluation logic, scoring methodology, or test methodology was changed as part of this workflow maintenance.
- Do not rewrite historical commits or replace the baseline record.

## Evidence links

- Original baseline run #13: https://github.com/Coolestcoker/FAHIMTA/actions/runs/43579108509
- Repository Actions page (locate run #16): https://github.com/Coolestcoker/FAHIMTA/actions
- Repository workflow file: https://github.com/Coolestcoker/FAHIMTA/blob/main/.github/workflows/tests.yml
