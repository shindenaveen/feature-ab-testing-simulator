# Feature A/B Testing Simulator

A Python-based simulation of A/B testing using synthetic data. Applies statistical methods such as t-tests and visualizes the results with histograms.

## Features
- Simulates A/B groups with different conversion means
- Performs t-test to check statistical significance
- Saves dataset, result summary, and visualizations

## Output
- `ab_test_data.csv` – Simulated dataset
- `ab_test_plot.png` – Conversion rate distribution
- `ab_test_summary.txt` – Test statistics and conclusion

## Requirements
- Python 3.8+
- numpy, pandas, matplotlib, seaborn, scipy

## Run
```bash
python ab_test_simulator.py
