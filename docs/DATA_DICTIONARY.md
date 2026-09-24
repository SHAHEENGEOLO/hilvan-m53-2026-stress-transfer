# Data dictionary

This file documents the machine-readable derived tables archived with the release.

## `POLARITY_REVIEW.csv`

Rows: **13**

Columns:

- `record_index`
- `record_key`
- `provider_folder`
- `id`
- `network`
- `station`
- `location`
- `channel`
- `sample_rate_hz`
- `latitude`
- `longitude`
- `epicentral_km`
- `distance_deg`
- `azimuth_deg`
- `takeoff_angle_deg`
- `channel_dip_deg`
- `predicted_p_time`
- `refined_p_time`
- `pick_method`
- `auto_polarity`
- `snr`
- `confidence`
- `response_status`
- `accepted_auto`
- `source_file`
- `site_cluster`
- `use`
- `reviewed_polarity`
- `reviewed`
- `comment`

## `all_vertical_P_polarity_candidates.csv`

Rows: **24**

Columns:

- `record_index`
- `record_key`
- `provider_folder`
- `id`
- `network`
- `station`
- `location`
- `channel`
- `sample_rate_hz`
- `latitude`
- `longitude`
- `epicentral_km`
- `distance_deg`
- `azimuth_deg`
- `takeoff_angle_deg`
- `channel_dip_deg`
- `predicted_p_time`
- `refined_p_time`
- `pick_method`
- `auto_polarity`
- `snr`
- `confidence`
- `response_status`
- `accepted_auto`
- `source_file`

## `best_mechanism_polarity_fit.csv`

Rows: **5**

Columns:

- `record_index`
- `record_key`
- `provider_folder`
- `id`
- `network`
- `station`
- `location`
- `channel`
- `sample_rate_hz`
- `latitude`
- `longitude`
- `epicentral_km`
- `distance_deg`
- `azimuth_deg`
- `takeoff_angle_deg`
- `channel_dip_deg`
- `predicted_p_time`
- `refined_p_time`
- `pick_method`
- `auto_polarity`
- `snr`
- `confidence`
- `response_status`
- `accepted_auto`
- `source_file`
- `site_cluster`
- `use`
- `reviewed_polarity`
- `reviewed`
- `comment`
- `reviewed_bool`
- `selection_source`
- `polarity`
- `weight`
- `predicted_polarity`
- `radiation_amplitude`
- `correct`

## `best_vertical_record_per_physical_site.csv`

Rows: **13**

Columns:

- `record_index`
- `record_key`
- `provider_folder`
- `id`
- `network`
- `station`
- `location`
- `channel`
- `sample_rate_hz`
- `latitude`
- `longitude`
- `epicentral_km`
- `distance_deg`
- `azimuth_deg`
- `takeoff_angle_deg`
- `channel_dip_deg`
- `predicted_p_time`
- `refined_p_time`
- `pick_method`
- `auto_polarity`
- `snr`
- `confidence`
- `response_status`
- `accepted_auto`
- `source_file`
- `site_cluster`

## `focal_coarse_10deg.csv`

Rows: **11664**

Columns:

- `strike`
- `dip`
- `rake`
- `weighted_misfit`
- `misfit_fraction`
- `polarity_errors`

## `focal_refined_2deg.csv`

Rows: **11614**

Columns:

- `strike`
- `dip`
- `rake`
- `weighted_misfit`
- `misfit_fraction`
- `polarity_errors`

## `near_best_focal_solutions.csv`

Rows: **1588**

Columns:

- `strike`
- `dip`
- `rake`
- `weighted_misfit`
- `misfit_fraction`
- `polarity_errors`

## `nodal_planes.csv`

Rows: **2**

Columns:

- `plane`
- `strike`
- `dip`
- `rake`
- `solution_status`
