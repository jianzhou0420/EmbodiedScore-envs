# Changelog

The version number of this package is a statement about scores. Every entry says whether it
changes the numbers an existing benchmark produces: `scores: unchanged` or
`scores: changed (which)`. MAJOR = old scores are no longer comparable; MINOR = a new benchmark,
engine, body or API, old scores unchanged; PATCH = bit-identical scores. The version lives only in
`pyproject.toml`; a tag is `v` + that string, cut on `main`.

## v0.0.1 — 2026-09-17

The first tagged release. The working numbers before it (0.1.0, 0.2.0) were never published.

- nDTW's FastDTW is a numba transcription of the fastdtw 0.3.4 *Cython* build
  (`benchmarks/env/dtw.py`); the `fastdtw` dependency is gone. `scores: unchanged` — 33 recorded
  cases match the Cython build bit for bit (`tests/test_dtw.py`).
- Engines in the tree at this tag: habitat-sim 0.3.3 for the habitat lines (R2R-CE, RxR-CE,
  HM-EQA and the other VLN-CE-derived boards), Isaac Sim for VLNverse, robosuite / MuJoCo for
  LIBERO and LIBERO-PRO / Plus, SAPIEN for RoboTwin 2.0, RoboCasa / RoboCasa365, CALVIN, and
  OmniGibson for BEHAVIOR-1K. No simulator is a pip dependency; the habitat wheels come from
  EmbodiedScore-habitat `v0.3.3-es.1`.
- The habitat lines replay against the habitat-lab 0.1.7 evaluator (`PARITY.md`).

## Before v0.0.1 — unreleased, 2026-09-06 to 2026-09-16

- 0.1.0: VLN-CE on Gymnasium — SimWorld, VLNCEEnv, metrics, wrappers, parity replay.
- 0.2.0: every habitat benchmark on one package (`benchmarks/ → env/ → sim/`), presets and a
  standard / upstream variant per line, then the six manipulation engines and VLNverse.
