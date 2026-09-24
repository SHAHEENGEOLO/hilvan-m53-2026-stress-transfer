# Zenodo upload guide

## Recommended record type
**Dataset** (the archive contains both derived data and reproducibility code).

## Upload
Upload `Hilvan_M53_2026_Zenodo_Release_v1.0.0.zip` as the main file.

## Metadata
Use the values in `metadata/zenodo_metadata.json`.

## Suggested title
Hilvan M5.3 (24 September 2026): rapid focal mechanism and Coulomb stress-transfer reproducibility archive

## Version
1.0.0

## License
CC BY 4.0 for the release/derived data. Code files additionally carry an MIT license.

## After DOI minting
1. Add the DOI to the paper's Data and Resources statement.
2. Add the DOI to `README.md` and `CITATION.cff`.
3. Create/update GitHub release `v1.0.0`.
4. Cite both the paper and the Zenodo DOI in subsequent reuse.

## Data statement suggested for TSR
"Processed station metadata, P-wave polarity measurements, focal-mechanism search grids, NP1/NP2
Coulomb-stress grids, figure-generation notebooks, and reproducibility metadata are archived at Zenodo
(DOI: [INSERT DOI]). Raw waveform and response data remain available from the original public
FDSN/network providers and are not redistributed in the archive."
