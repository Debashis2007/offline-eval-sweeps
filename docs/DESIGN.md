# Design: Offline Eval Sweeps

**Project:** `offline-eval-sweeps`  
**Parent system design:** [03 — Distributed Training & Job Orchestration](https://github.com/Debashis2007/offline-eval-sweeps/blob/main/03-distributed-training-orchestration.md) · [05 — Model Monitoring & Behavior Observability](https://github.com/Debashis2007/offline-eval-sweeps/blob/main/05-model-monitoring-observability.md) · [08 — Fine-Tuning / Eval Data Pipelines](https://github.com/Debashis2007/offline-eval-sweeps/blob/main/08-finetuning-eval-data-pipelines.md)

## 1. What this POC demonstrates

Pack many short eval jobs; gate promote on suite score threshold.

## 2. Architecture (POC)

```text
POST /sweeps → score + pass/fail gate
GET /sweeps/{id}
```

## 3. Patterns used (and why)

| Pattern | Why used | Where in code |
|---------|----------|---------------|
| Suite version pin | Scores are meaningless without suite identity. | `suite` string in result. |
| Release gate boolean | Automate promote/block. | `pass` vs threshold. |
| Ephemeral packing model | Evals should use spare/batch capacity. | Documented in response semantics. |

## 4. Key endpoints

`GET /health`, `POST /sweeps`, `GET /sweeps/{id}`

## 5. Tradeoffs / POC limits

Scores are random for demo — replace with real harness later.

## 6. How to run

See the **Run (self-contained POC)** section in [`../README.md`](../README.md).

This folder is self-contained and can be published as its own GitHub repository.

## 7. Design walkthrough video

> **Watch on YouTube:** [Offline Eval Sweeps — System Design #Shorts](https://youtu.be/NsyLa3BvTA0)
>
> Direct link: **https://youtu.be/NsyLa3BvTA0**

Also available in-repo:
- GIF preview: [`video/design-overview.gif`](./video/design-overview.gif)
- MP4 download: [`video/design-overview.mp4`](./video/design-overview.mp4)
- Narration script: [`video/narration.txt`](./video/narration.txt)

---

**Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.**  
Unauthorized copying or redistribution of this material is prohibited.  
GitHub: [Debashis2007](https://github.com/Debashis2007)

