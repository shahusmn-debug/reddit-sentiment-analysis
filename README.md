# Comparative Analysis of COVID-19 Vaccine Sentiment on Reddit

This project utilizes a computational pipeline to analyze and compare COVID-19 vaccine sentiment between
## Project Poster

![Project Poster](MARCOEM%20Poster%2025_005b.jpg)

[Download Original Poster (PPTX)](MARCOEM%20Poster%2025_005b.pptx)

## Key Findings the Reddit API for data collection and Large Language Models (LLMs) for sentiment classification, this study quantifies the divergence in public discourse between "blue-collar" (e.g., r/Construction, r/Truckers) and "white-collar" (e.g., r/programming, r/marketing) communities.

## Repository Structure

*   **`01_data_collection.py`**: Script to fetch historical posts and comments from specified subreddits using the PRAW library.
*   **`02_sentiment_classification.py`**: Uses Gemini Pro to classify text into Positive, Negative, or Neutral sentiment categories.
*   **`03_statistical_analysis.py`**: Performs Chi-Square tests and t-tests to identify statistically significant differences in sentiment distributions.
*   **`04_visualization.py`**: Generates bar charts and time-series plots to visualize sentiment trends.
*   **`data/`**: Contains the processed CSV datasets used in the analysis.
*   **`figures/`**: Stores the generated charts and visualizations.
*   **`paper/`**: Includes the full research paper and reference documents.

## Usage

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Pipeline**:
    The scripts are designed to be run sequentially:
    ```bash
    python 01_data_collection.py
    python 02_sentiment_classification.py
    python 03_statistical_analysis.py
    python 04_visualization.py
    ```


