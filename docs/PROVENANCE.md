# Data provenance

## Event
- USGS event ID: `us6000tx9u`
- Origin time: 2026-09-24T07:40:58.138Z
- Latitude / longitude: 37.4736, 38.8612
- Depth: 10 km
- Magnitude in study archive: 5.3
- Original acquisition radius: 200 km
- Acquisition window: 2026-09-24T07:35:58.138Z to 2026-09-24T08:40:58.138Z

## Raw seismic data
The original study archive contains public waveform/response material retrieved from participating
FDSN/network providers. Those raw waveform bytes are **not redistributed in this release**.
`data/metadata/raw_waveform_manifest.csv` records the original archive paths, sizes, and CRC32
identifiers. Use `notebooks/01_FDSN_download_event_data.ipynb` to reacquire public data and cite the
originating networks/data centers.

## Derived data archived here
The release includes the exact derived CSV tables and NPZ Coulomb grids used by the manuscript:
- P-polarity candidates and selected observations
- focal-mechanism coarse/refined search grids
- 1,588 near-best focal solutions from the archived run
- NP1 / NP2 solution table
- NP1 and NP2 Coulomb grids
- focal/Coulomb summary metadata
- data-derived QC and Coulomb figures

## Scientific status
The archived source solution is `EXPLORATORY_UNDERCONSTRAINED_AUTO` with
5 weighted polarities and a 207.7° azimuth gap.
The archive therefore reproduces the paper's **rapid exploratory** analysis; it must not be relabeled
as a fully resolved focal mechanism.
