# dynamo/log-report (Harbor / Terminal-Bench 2)

Ground-up repair of the broken Project Dynamo `log-report` task.

## Task layout

```
log-report/
├── task.toml
├── instruction.md
├── environment/
│   ├── Dockerfile
│   └── access.log
├── solution/
│   ├── solve.sh
│   └── solve.py
└── tests/
    ├── test.sh
    └── test_outputs.py
```

Removed from the agent image build context: `environment/solution_hint.py`
(leaked reference implementation).

## Local checks

```bash
harbor run -p log-report -a oracle      # expect reward 1.0
harbor run -p log-report --agent nop    # expect reward 0.0
```

Keep this repository public until the assessment is marked passed, then make it private.
