# GitHub publishing guide

Recommended repository name:

`hilvan-m53-2026-stress-transfer`

## Upload
1. Create a new public GitHub repository.
2. Extract the GitHub ZIP and upload/push its **contents**, not the outer folder.
3. Replace `REPLACE_WITH_USERNAME` in `CITATION.cff`.
4. Check that notebooks and CSV/NPZ files render/download correctly.
5. Create release `v1.0.0`.

## Suggested repository description
Rapid reproducibility archive for the 24 Sep 2026 Hilvan/Şanlıurfa M5.3 earthquake:
P-wave first motions, provisional focal mechanism, NP1/NP2 Coulomb stress, uncertainty, and publication figures.

## Suggested GitHub topics
`seismology`, `earthquake`, `focal-mechanism`, `coulomb-stress`, `obspy`,
`pyrocko`, `turkiye`, `reproducible-research`

## Large files
Do not commit raw MiniSEED/SAC archives directly. If you later decide to host authorized waveform copies,
use a dedicated data repository or Git LFS and preserve provider/network attribution.
