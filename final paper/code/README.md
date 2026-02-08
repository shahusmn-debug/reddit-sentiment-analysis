# Analysis Code Repository

This folder contains the sanitized Python code used for data analysis in the study:

**"Computational Based Comparison of COVID-19 Vaccine Sentiment Between Occupational Groups on Reddit in 2021"**

---

## Files

| File | Description |
|------|-------------|
| `01_data_collection.py` | Reddit API data collection script |
| `02_sentiment_classification.py` | LLM-based sentiment analysis |
| `03_statistical_analysis.py` | Statistical tests and descriptive statistics |
| `04_visualization.py` | Figure generation code |
| `requirements.txt` | Python dependencies |

---

## Requirements

```
pandas>=2.0.0
numpy>=1.24.0
scipy>=1.10.0
matplotlib>=3.7.0
seaborn>=0.12.0
google-genai>=0.3.0
praw>=7.7.0
```

---

## Usage

1. Install dependencies: `pip install -r requirements.txt`
2. Configure API credentials (see individual scripts)
3. Run scripts in numerical order

---

## Notes

- API keys and credentials have been removed for publication
- Placeholder values marked with `<YOUR_API_KEY>` must be replaced
- Data collection dates were January 1, 2021 to December 31, 2021
