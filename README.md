# Use Case: Large Offline Eval Sweeps

**Design doc:** [docs/DESIGN.md](./docs/DESIGN.md) — architecture, patterns, and why.


**Parent system design:** [03 — Distributed Training & Job Orchestration](../03-distributed-training-orchestration.md)  
**Also references:** [05 — Model monitoring](../05-model-monitoring-observability.md), [08 — Data pipelines](../08-finetuning-eval-data-pipelines.md)

## Users & problem

Quality/safety teams run thousands of short inference jobs across models and suites (nightly or pre-release). Throughput and fairness matter more than gang topology.

## Requirements & SLOs

| Requirement | Target |
|-------------|--------|
| Throughput | Maximize evals/hour on spare capacity |
| Packing | Fill GPU fragments left by big jobs |
| Determinism | Pin model + suite versions |
| Reporting | Aggregate scores to release gates |

## Design (from parent)

```
Eval suite registry → sweep controller
  → many small jobs on packed GPUs / inference pool
  → results DB → gate (pass/fail) → notify release
```

Prefer **inference-style workers** over heavy training gangs when possible; still use **03** for scheduling/quotas.

## Specializations

| Concern | Eval sweep choice |
|---------|-------------------|
| Priority | Below interactive; can use spot/preemptible |
| Isolation | Don’t steal chat capacity—separate pool |
| Data | Golden sets; leakage firewall ([08](../08-finetuning-eval-data-pipelines.md)) |
| Compare | Paired A/B against control revision |

## Failure modes

- Sweep starves training → quotas + time windows.
- Flaky scores → retries with seed control; quarantine flakes.
- Silent suite drift → content-address suite version in reports.




## Design walkthrough (opens on GitHub)

![Design overview](docs/video/design-overview.gif)

Full narrated video (download): [docs/video/design-overview.mp4](docs/video/design-overview.mp4)

## Run (self-contained POC)

This folder is a **standalone** project (safe to split into its own GitHub repo).

```bash
cd offline-eval-sweeps
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
PYTHONPATH=. python -m uvicorn app.main:app --reload --port 8000
```

```bash
curl -s http://127.0.0.1:8000/health | jq
```

curl -s -X POST http://127.0.0.1:8000/sweeps -H 'Content-Type: application/json' -d '{"suite":"safety@v3","model":"mock-mid"}' | jq
