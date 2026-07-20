# dynamo/log-report — fixed Terminal-Bench 2 (Harbor) task

Repaired Harbor task for the Project Dynamo "Fix the Broken Terminal-Bench Task" exercise.

## Layout

```
log-report/
├── task.toml
├── instruction.md
├── environment/
│   ├── Dockerfile          # digest-pinned base; no leaked solution
│   └── access.log
├── solution/
│   ├── solve.sh
│   └── solve.py
└── tests/
    ├── test.sh             # writes /logs/verifier/reward.txt + ctrf.json
    └── test_outputs.py     # 5 tests ↔ 5 instruction.md success criteria
```

## Defects fixed

1. `task.toml` — `artifacts` is an array pointing at `/app/report.json`
2. `environment/Dockerfile` — base image pinned by `@sha256` digest
3. Removed `environment/solution_hint.py` (leaked reference solution)
4. Verifier checks real report values (not just file existence)
5. `tests/test.sh` writes reward/ctrf under `/logs/verifier/`
6. `instruction.md` has numbered success criteria matching the verifier

## Verify locally

```bash
harbor run -p log-report -a oracle      # expect reward 1.0
harbor run -p log-report --agent nop    # expect reward 0.0
```

## Note

Keep this repository **public** until the assessment is marked passed, then set it to **private**.
