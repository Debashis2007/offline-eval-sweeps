# Design: Offline Eval Sweeps

**Project:** `offline-eval-sweeps`  
**Parent system design:** `03-distributed-training-orchestration.md / 05 / 08`

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

Narrated with **ElevenLabs Debpro voice** and Debpro still image (via [GitaProject](/Users/deb/Development/GenAI/GitaProject)):

- Video: [`video/design-overview.mp4`](./video/design-overview.mp4)
- Script: [`video/narration.txt`](./video/narration.txt)

