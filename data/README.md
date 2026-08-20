# Data

Nothing in this directory is committed. Two external sources are required.

## 1. SigmaHQ rule repository

    git clone https://github.com/SigmaHQ/sigma.git ../sigma

Full history is required — do not use `--depth 1`.

## 2. Prepared pipeline outputs from Long & Evans

From the artefact accompanying arXiv:2605.05383:

    https://github.com/Elena6918/Evolution-of-Log-Based-Detection-Rules

Download `build_data/`, `ir_data/`, `align_data/`, `llm_data/` from the Google Drive
link in their README into `../Evolution-of-Log-Based-Detection-Rules/data_prep/`.

Approximately 1.9 GB. Snapshot date 10 April 2026.
