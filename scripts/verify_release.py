#!/usr/bin/env python3
from pathlib import Path
import json, hashlib, pandas as pd, numpy as np, sys

root = Path(__file__).resolve().parents[1]
errors = []

summary = root / "data/derived/study_snapshot/focal_coulomb_results/FINAL_FOCAL_COULOMB_SUMMARY.json"
if not summary.exists():
    errors.append("Missing FINAL_FOCAL_COULOMB_SUMMARY.json")
else:
    s = json.loads(summary.read_text(encoding="utf-8"))
    if str(s.get("event_id")) != "us6000tx9u":
        errors.append("Unexpected event_id")
    if int(s.get("n_polarities", -1)) != 5:
        errors.append("Unexpected number of archived polarities")
    if abs(float(s.get("azimuth_gap_deg", 0)) - 207.6501276734167) > 0.1:
        errors.append("Unexpected archived azimuth gap")

tables = root / "data/derived/study_snapshot/focal_coulomb_results/tables"
expected_rows = {
    "best_mechanism_polarity_fit.csv": 5,
    "near_best_focal_solutions.csv": 1588,
    "nodal_planes.csv": 2,
}
for name, n in expected_rows.items():
    p = tables / name
    if not p.exists():
        errors.append(f"Missing {name}")
        continue
    df = pd.read_csv(p)
    if len(df) != n:
        errors.append(f"{name}: expected {n} rows, found {len(df)}")

cfs = root / "data/derived/study_snapshot/focal_coulomb_results/coulomb"
for name in ["us6000tx9u_NP1_waveform_CFS.npz", "us6000tx9u_NP2_auxiliary_CFS.npz"]:
    p = cfs / name
    if not p.exists():
        errors.append(f"Missing {name}")
        continue
    z = np.load(p)
    if "cfs_mpa" not in z.files:
        errors.append(f"{name}: missing cfs_mpa array")

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print("VALIDATION PASSED")
print("Event: us6000tx9u")
print("Selected polarities: 5")
print("Near-best solutions: 1588")
print("NP1/NP2 Coulomb grids: present")
