Piezoelectric d₃₃ Meter (Python)

🧪📈 A simple but effective Python tool for calculating the piezoelectric coefficient (d₃₃) from butterfly loops.

A lightweight, research‑focused Python workflow designed to standardize how d₃₃ values are extracted from experimental butterfly loop data. The goal is not complexity, but clarity, consistency, and reproducibility in materials characterization.

🔬 Motivation

During experimental research on piezoelectric materials, comparing reported d₃₃ values across different papers can be surprisingly difficult. Even when measurement setups appear similar, the calculation methods often differ, leading to inconsistent or unclear comparisons.

To solve this, this project provides a Python‑based, transparent approach to calculating d₃₃ directly from raw loop data using a consistent methodology.

🐍 Why Python for Materials Science?

Python is increasingly used in experimental and computational materials science because it allows:

Automated analysis of experimental data

Reproducible and transparent calculations

Easy integration with measurement pipelines

Rapid iteration without manual data handling

This project demonstrates how Python can replace ad‑hoc spreadsheet workflows with a clean, auditable analysis pipeline tailored for real laboratory data.

🧰 What the Tool Does

Reads experimental butterfly loop data from Excel files (voltage vs displacement/strain)

Identifies the relevant linear region of the loop

Calculates the slope corresponding to the d₃₃ piezoelectric coefficient (in pC/N)

Plots the butterfly loop. Highlights the linear region used for the calculation.

Supports different material behaviors:

Positively polarized piezoceramics (e.g. PZT)

Negatively polarized piezoelectric polymers (e.g. PVDF)

The focus is on practical post‑processing, not theoretical modeling.

🗂️ Repository Structure
```text
Piezoelectric-coefficient-d33-meter/
│
├── piezoD33_positive_pzt.py  # d33 calculation workflow for piezoceramic materials
│
├── piezoD33_negative_polymer.py  # d33 calculation workflow for piezoelectric polymers
│
├── hyster2.xlsx  # Example butterfly loop datasets
├── hyster4.xlsx  # Example butterfly loop datasets
│
└── README.md

```
⚙️ Requirements

Python 3.7+

Scientific Python stack:

numpy, pandas, matplotlib

Install dependencies:

pip install numpy pandas matplotlib


👤 Author

Developed by Sepide Taleb, focused on applying Python, data analysis, and automation to materials science and experimental research.
If you work on piezoelectric materials and want to collaborate or adapt this tool, feel free to reach out.
