# Hilvan M5.3 (24 September 2026): rapid focal mechanism and Coulomb stress transfer

Reproducibility archive for the rapid study of **USGS event `us6000tx9u`**,
M 5.3 near Hilvan, southeastern Türkiye.

**Manuscript:** *Rapid Source Constraints and Nodal-Plane-Robust Static Stress Transfer of the
24 September 2026 Mw 5.3–5.4 Şanlıurfa Earthquake, Southeastern Türkiye.*

## What is archived

This repository contains the code and exact **derived** data needed to reproduce the focal-mechanism
search, NP1/NP2 Coulomb grids, uncertainty diagnostics, and publication figures.

The raw provider waveform bytes are intentionally not redistributed. They remain available from the
original seismic networks/FDSN data centers; a complete raw-file manifest and download workflow are
included.

## Scientific status

The archived rapid solution is **EXPLORATORY_UNDERCONSTRAINED_AUTO**:
- weighted P polarities used: **5**
- maximum azimuth gap: **207.7°**
- NP1: **118.0 / 66.0 / -50.0°**
- NP2: **233.9 / 45.6 / -145.3°**
- assumed stress drop: **3.0 MPa**
- effective friction: **0.4**

These values reproduce the rapid manuscript analysis. They are **not** a definitive reviewed moment tensor,
and the Coulomb maps are **not earthquake predictions**.

## Repository layout

```text
notebooks/
  01_FDSN_download_event_data.ipynb
  02_focal_mechanism_and_coulomb.ipynb
  03_publication_maps_2D_3D.ipynb

data/
  raw/                         # intentionally empty except instructions
  metadata/
    raw_waveform_manifest.csv
    source_archive_summary.json
  derived/study_snapshot/
    study.json
    channels.csv
    analysis/02_station_metadata/station_geometry.csv
    focal_coulomb_results/     # exact CSV/NPZ/PNG outputs used by the paper

figures/paper/                 # selected manuscript figures
scripts/
docs/
```

## Quick start

### Option A — reproduce figures from archived derived results
```bash
conda env create -f environment.yml
conda activate hilvan-m53-2026
jupyter lab
```

Open `notebooks/03_publication_maps_2D_3D.ipynb`.
It defaults to `data/derived/study_snapshot/`.

### Option B — rerun from waveform data
1. Obtain/re-download the original public waveform/response data.
2. Place the study ZIP in `data/raw/`.
3. Run `notebooks/02_focal_mechanism_and_coulomb.ipynb`.
4. Run notebook 03 for publication graphics.

Notebook 01 provides an FDSN acquisition workflow for event `us6000tx9u`.

## Key derived files

- `FINAL_FOCAL_COULOMB_SUMMARY.csv/json` — machine-readable source/model summary.
- `tables/best_mechanism_polarity_fit.csv` — five weighted observations used by the archived mechanism.
- `tables/near_best_focal_solutions.csv` — non-uniqueness family.
- `coulomb/us6000tx9u_NP1_waveform_CFS.npz`
- `coulomb/us6000tx9u_NP2_auxiliary_CFS.npz`

See `docs/DATA_DICTIONARY.md` and `docs/PROVENANCE.md`.

## Integrity

Run:

```bash
python scripts/verify_release.py
```

`MANIFEST.csv` and `checksums.sha256` provide SHA-256 hashes for the archived files.

## Licenses

- Code and notebooks: **MIT License** (`LICENSE_CODE`)
- Original derived tables/figures in this release: **CC BY 4.0** (`LICENSE_DATA`)
- Raw seismic waveform/response data: **not redistributed**; original provider/network terms apply.

## Citation

A `CITATION.cff` file is included. After Zenodo mints the DOI, update the DOI in the repository release
and in the paper's Data and Resources statement.

## Author

Shaheen Mohammed Saleh Ahmed  
Department of Applied Geology, College of Science, University of Kirkuk, Kirkuk, Iraq  
ORCID: https://orcid.org/0000-0002-9289-128X
