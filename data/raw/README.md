# Raw waveform data are not bundled

The original analysis used public seismic waveform and response metadata from FDSN/network providers.
To avoid detaching those records from provider attribution and network-specific terms, the raw MiniSEED,
SAC and StationXML bytes are not republished in this repository.

Use:
1. `../metadata/raw_waveform_manifest.csv` for the exact original file manifest.
2. `../../notebooks/01_FDSN_download_event_data.ipynb` to download public data again.
3. Provider/network citations and data-center terms when reusing waveforms.

If you maintain an authorized local copy of the original archive, place it in this folder and set
`DATA_SOURCE` in notebook 02. ZIP files in `data/raw/` are ignored by Git.
