# Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.
# Unauthorized copying, modification, or distribution is prohibited.
# https://github.com/Debashis2007

"""Offline Eval Sweeps — thin self-contained FastAPI POC."""

from __future__ import annotations

from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from poc_core import MockLLM, TokenBucket, health_payload
from poc_core.safety import SafetyPlane
from poc_core.stores import InMemoryStore, MockVectorIndex

USE_CASE = "Offline Eval Sweeps"
app = FastAPI(title=USE_CASE)
llm = MockLLM()
store = InMemoryStore()
safety = SafetyPlane()

@app.get("/health")
def health():
    return health_payload(USE_CASE)


import random, uuid

results: dict[str, dict] = {}

class SweepIn(BaseModel):
    suite: str
    model: str

@app.post("/sweeps")
def sweep(body: SweepIn):
    sid = f"s_{uuid.uuid4().hex[:6]}"
    score = round(random.uniform(0.7, 0.99), 3)
    gate = score >= 0.8
    results[sid] = {"id": sid, "suite": body.suite, "model": body.model, "score": score, "pass": gate}
    return results[sid]

@app.get("/sweeps/{sid}")
def get(sid: str):
    if sid not in results:
        raise HTTPException(404)
    return results[sid]
