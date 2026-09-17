"""nDTW's DTW is ``benchmarks/env/dtw.py`` — a numba transcription of the
fastdtw package's Cython build. The fixture holds that build's own outputs
(distance and path, euclidean float64), generated 2026-09-17 from fastdtw
0.3.4 compiled with Cython; the transcription must reproduce them bit for bit."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest
from embodiedscore_envs.benchmarks.env.dtw import dtw, fastdtw

FIXTURE = Path(__file__).parent / "fixtures" / "dtw_cython_reference.json"
CASES = json.loads(FIXTURE.read_text())


@pytest.mark.parametrize("case", CASES, ids=[c["name"] for c in CASES])
def test_matches_the_cython_build_bit_for_bit(case):
    x, y = np.asarray(case["x"]), np.asarray(case["y"])
    c, p = fastdtw(x, y)
    assert c == case["fastdtw"]                       # ==, not approx: same bits
    assert p == [tuple(q) for q in case["fastdtw_path"]]
    ce, pe = dtw(x, y)
    assert ce == case["dtw"]
    assert pe == [tuple(q) for q in case["dtw_path"]]


def test_doc_example_of_the_package():
    c, p = fastdtw(np.array([1, 2, 3, 4, 5.0]), np.array([2, 3, 4.0]))
    assert (c, p) == (2.0, [(0, 0), (1, 0), (2, 1), (3, 2), (4, 2)])


def test_ties_break_corner_last_like_the_cython_build():
    # up, left and corner all cost the same into (1, 1): the Cython build takes the corner
    x = np.array([[0.0], [0.0]])
    y = np.array([[0.0], [0.0]])
    assert dtw(x, y)[1] == [(0, 0), (1, 1)]


def test_metrics_wrapper_uses_it():
    from embodiedscore_envs.benchmarks.env import metrics
    assert metrics._fastdtw() is fastdtw
