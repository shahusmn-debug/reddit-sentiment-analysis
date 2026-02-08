"""
03_statistical_analysis.py
Statistical Analysis Script

This script performs statistical tests comparing sentiment between
blue-collar and white-collar occupational groups.
"""

import pandas as pd
import numpy as np
from scipy import stats

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def compute_95_ci(data):
    """Compute 95% confidence interval for a data series."""
    n = len(data)
    if n < 2:
        return (np.nan, np.nan)
    
    mean = np.mean(data)
    sem = stats.sem(data, nan_policy='omit')
    ci = stats.t.interval(0.95, n-1, loc=mean, scale=sem)
    return ci


# =============================================================================
# MAIN ANALYSIS
# =============================================================================

def main():
    # Load data
    input_file = "reddit_data_with_gemini_sentiment.csv"
    df = pd.read_csv(input_file)
    print(f"Loaded {len(df)} records")
    
    # ==========================================================================
    # 1. Descriptive Statistics by Category
    # ==========================================================================
    print("\n" + "="*60)
    print("1. DESCRIPTIVE STATISTICS BY CATEGORY")
    print("="*60)
    
    for category in ['blue_collar', 'white_collar']:
        cat_data = df[df['category'] == category]['sentiment_score']
        ci = compute_95_ci(cat_data)
        print(f"\n{category.upper()}:")
        print(f"  N = {len(cat_data)}")
        print(f"  Mean = {cat_data.mean():.4f}")
        print(f"  Median = {cat_data.median():.4f}")
        print(f"  Std Dev = {cat_data.std():.4f}")
        print(f"  95% CI = [{ci[0]:.4f}, {ci[1]:.4f}]")
    
    # ==========================================================================
    # 2. Independent Samples T-Test
    # ==========================================================================
    print("\n" + "="*60)
    print("2. INDEPENDENT SAMPLES T-TEST")
    print("="*60)
    
    blue_collar = df[df['category'] == 'blue_collar']['sentiment_score']
    white_collar = df[df['category'] == 'white_collar']['sentiment_score']
    
    t_stat, p_value = stats.ttest_ind(blue_collar, white_collar, equal_var=False)
    print(f"\nWelch's T-Test:")
    print(f"  t-statistic = {t_stat:.4f}")
    print(f"  p-value = {p_value:.4e}")
    print(f"  Result: {'Significant' if p_value < 0.05 else 'Not Significant'} (α = 0.05)")
    
    # ==========================================================================
    # 3. Chi-Square Test of Independence
    # ==========================================================================
    print("\n" + "="*60)
    print("3. CHI-SQUARE TEST OF INDEPENDENCE")
    print("="*60)
    
    contingency = pd.crosstab(df['category'], df['gemini_sentiment'])
    print("\nContingency Table:")
    print(contingency)
    
    chi2, p, dof, expected = stats.chi2_contingency(contingency)
    print(f"\nChi-Square Test:")
    print(f"  χ² statistic = {chi2:.4f}")
    print(f"  Degrees of freedom = {dof}")
    print(f"  p-value = {p:.4e}")
    print(f"  Result: {'Significant' if p < 0.05 else 'Not Significant'} (α = 0.05)")
    
    # ==========================================================================
    # 4. Correlation Analysis (Karma vs Sentiment)
    # ==========================================================================
    print("\n" + "="*60)
    print("4. CORRELATION ANALYSIS (KARMA VS SENTIMENT)")
    print("="*60)
    
    # Pearson correlation
    pearson_r, pearson_p = stats.pearsonr(df['sentiment_score'], df['score'])
    print(f"\nPearson Correlation:")
    print(f"  r = {pearson_r:.4f}")
    print(f"  p-value = {pearson_p:.4e}")
    
    # Spearman correlation
    spearman_r, spearman_p = stats.spearmanr(df['sentiment_score'], df['score'])
    print(f"\nSpearman Correlation:")
    print(f"  ρ = {spearman_r:.4f}")
    print(f"  p-value = {spearman_p:.4e}")
    
    # ==========================================================================
    # 5. Subreddit-Level Analysis
    # ==========================================================================
    print("\n" + "="*60)
    print("5. SUBREDDIT-LEVEL STATISTICS")
    print("="*60)
    
    subreddit_stats = df.groupby(['category', 'subreddit']).agg({
        'sentiment_score': ['count', 'mean', 'std']
    }).round(4)
    subreddit_stats.columns = ['N', 'Mean', 'Std']
    print(subreddit_stats.to_string())


if __name__ == "__main__":
    main()
