# SmallRamp Analysis — Thesis Analysis

This repository contains the code and notebooks used for my master's thesis analysis of postural responses to small ramp visual stimuli. It documents the processing of experimental recordings, gain estimates and confidence intervals, time- and frequency-domain results, and a comparison between recording sessions.

The aim is to make the analysis understandable and allow the thesis figures to be regenerated from the same input data, quality selections, and software environment.

## Notebooks

| Notebook | Purpose |
| --- | --- |
| `01_getting_started.ipynb` | Introduction to BalancePy. |
| `1a_make_qualitycheck_plots.ipynb` | Recording quality checks. |
| `1b_make_csmi_plots.ipynb` | CSMI model fitting. |
| `1c_Screening.ipynb` | Review plots and assign quality flags. |
| `2a_SmallRampAnalysis.ipynb` | Responses and gains across velocities. |
| `2b_GainAndAmplitudeAnalysis.ipynb` | Gain confidence intervals and amplitudes. |
| `3_TimeAndFrequencyAnalysis.ipynb` | Time signals and frequency spectra. |
| `4_SessionComparison_0p01.ipynb` | Gain comparison between sessions at 0.01°/s. |

## Project structure

```text
SmallRamp_Analysis_Thesis/
├── README.md
├── .gitignore
├── Thesis/
│   └── Thesis_KevinRahy.pdf
├── notebooks/
├── src/
│   ├── __init__.py
│   └── config.py
├── data/
│   └── metadata.xlsx
├── pyproject.toml
└── poetry.lock
```

The GitHub version will include reviewed metadata but exclude raw data and `results/`; notebooks may retain saved figures. Raw data is available upon request.

## Requirements and BalancePy

This project requires **Python 3.12**, **Poetry**, and **BalancePy**. Other Python dependencies are listed in `pyproject.toml`, with exact package versions listed in `poetry.lock`.

[BalancePy](https://github.com/PostureControlLab/balancepy) is a separate Python library used to load and preprocess recordings, work with stimulus-response data, calculate frequency-response gains and spectra, and fit CSMI models. Its source code is not bundled in this repository. The notebooks import it using `import balancepy` and its analysis modules.

### Installation

1. Clone this analysis repository and open its project folder.
2. Clone the BalancePy repository separately:

   ```bash
   git clone https://github.com/PostureControlLab/balancepy.git
   ```

3. Configure the BalancePy location before installing. The current `pyproject.toml` uses the relative path `../../balancepy-dev/balancepy`. Either place the checkout at that location relative to this project, or change that dependency path to your checkout and regenerate the lock file with `poetry lock`.
4. Install the environment and start Jupyter:

   ```bash
   poetry install
   poetry run jupyter notebook
   ```

   In VS Code, select the Python environment created for this project as the notebook kernel.

## Data and reproduction

The full analysis needs the raw experimental recordings as well as `data/metadata.xlsx`. Metadata alone is not sufficient to reproduce the results. Preserve recording names and the directory structure expected by the metadata, and place the recordings in `data/raw/`. Shared paths are defined in `src/config.py`.

Raw data is available upon request. To reproduce the results, use the same data, then run all cells in each analysis notebook from a fresh kernel. Figures and tables are saved in `results/paper_figures/` and `results/tables/`.

## Thesis

[Master's thesis (PDF)](Thesis/Thesis_KevinRahy.pdf)

## Acknowledgements

I would like to thank my supervisor [LAsslaender](https://github.com/LAsslaender) for his guidance and support throughout this work, and for providing the [BalancePy](https://github.com/PostureControlLab/balancepy) repository used for the analysis.
