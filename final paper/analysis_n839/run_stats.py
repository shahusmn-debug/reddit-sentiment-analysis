"""
Statistics Computation for Filtered Dataset (N=839)
Uses filtered 2021-only data
"""

import pandas as pd
import numpy as np
from scipy import stats

# Paths
DATA_DIR = r"c:\Users\Usman\Projects\Autoscholar\IDEPaper\final paper\data"
OUTPUT_DIR = r"c:\Users\Usman\Projects\Autoscholar\IDEPaper\final paper\analysis_n839"

def compute_95_ci(data):
    """Compute 95% confidence interval."""
    n = len(data)
    if n < 2:
        return (np.nan, np.nan)
    mean = np.mean(data)
    sem = stats.sem(data, nan_policy='omit')
    ci = stats.t.interval(0.95, n-1, loc=mean, scale=sem)
    return ci

def main():
    # Load filtered data
    df = pd.read_csv(f"{DATA_DIR}/reddit_data_2021_filtered.csv")
    print(f"Loaded N={len(df)} records (filtered 2021 data)")
    
    output_file = f"{OUTPUT_DIR}/computed_stats_n839.md"
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Statistical Analysis - Filtered Dataset (N=839)\n\n")
        f.write("**Data Source:** `reddit_data_2021_filtered.csv`\n")
        f.write(f"**Total Records:** N={len(df)}\n")
        f.write("**Date Range:** January 1, 2021 - December 31, 2021\n\n")
        f.write("---\n\n")
        
        # 1. Category breakdown
        f.write("## 1. Data Overview\n\n")
        blue_n = len(df[df['category'] == 'blue_collar'])
        white_n = len(df[df['category'] == 'white_collar'])
        f.write(f"- **Blue Collar:** n={blue_n} ({blue_n/len(df)*100:.1f}%)\n")
        f.write(f"- **White Collar:** n={white_n} ({white_n/len(df)*100:.1f}%)\n\n")
        
        posts_n = len(df[df['type'] == 'post'])
        comments_n = len(df[df['type'] == 'comment'])
        f.write(f"- **Posts:** n={posts_n} ({posts_n/len(df)*100:.1f}%)\n")
        f.write(f"- **Comments:** n={comments_n} ({comments_n/len(df)*100:.1f}%)\n\n")
        
        # 2. Descriptive stats by category
        f.write("## 2. Sentiment by Category\n\n")
        f.write("| Category | N | Mean | Std Dev | 95% CI Lower | 95% CI Upper |\n")
        f.write("|----------|---|------|---------|--------------|---------------|\n")
        
        for category in ['blue_collar', 'white_collar']:
            cat_data = df[df['category'] == category]['sentiment_score']
            ci = compute_95_ci(cat_data)
            f.write(f"| {category} | {len(cat_data)} | {cat_data.mean():.4f} | {cat_data.std():.4f} | {ci[0]:.4f} | {ci[1]:.4f} |\n")
        
        # 3. T-test
        f.write("\n## 3. T-Test (Blue vs White Collar)\n\n")
        blue_collar = df[df['category'] == 'blue_collar']['sentiment_score']
        white_collar = df[df['category'] == 'white_collar']['sentiment_score']
        t_stat, p_val = stats.ttest_ind(blue_collar, white_collar, equal_var=False)
        f.write(f"- **T-statistic:** {t_stat:.4f}\n")
        f.write(f"- **P-value:** {p_val:.4e}\n")
        f.write(f"- **Result:** {'Significant' if p_val < 0.05 else 'Not Significant'} (α = 0.05)\n\n")
        
        # 4. Chi-square
        f.write("## 4. Chi-Square (Category vs Sentiment Label)\n\n")
        contingency = pd.crosstab(df['category'], df['gemini_sentiment'])
        f.write("**Contingency Table:**\n")
        f.write(contingency.to_markdown())
        f.write("\n\n")
        
        chi2, p, dof, expected = stats.chi2_contingency(contingency)
        f.write(f"- **χ² Statistic:** {chi2:.4f}\n")
        f.write(f"- **P-value:** {p:.4e}\n")
        f.write(f"- **Result:** {'Significant' if p < 0.05 else 'Not Significant'}\n\n")
        
        # 5. Correlation
        f.write("## 5. Correlation (Karma vs Sentiment)\n\n")
        pearson_r, pearson_p = stats.pearsonr(df['sentiment_score'], df['score'])
        spearman_r, spearman_p = stats.spearmanr(df['sentiment_score'], df['score'])
        
        f.write("| Method | r | P-value |\n")
        f.write("|--------|---|----------|\n")
        f.write(f"| Pearson | {pearson_r:.4f} | {pearson_p:.4e} |\n")
        f.write(f"| Spearman | {spearman_r:.4f} | {spearman_p:.4e} |\n\n")
        
        # 6. Subreddit stats
        f.write("## 6. Subreddit-Level Statistics\n\n")
        f.write("| Category | Subreddit | N | Mean | Std Dev | 95% CI Lower | 95% CI Upper |\n")
        f.write("|----------|-----------|---|------|---------|--------------|---------------|\n")
        
        sub_stats = df.groupby(['category', 'subreddit']).agg({
            'sentiment_score': ['count', 'mean', 'std']
        }).reset_index()
        sub_stats.columns = ['category', 'subreddit', 'count', 'mean', 'std']
        sub_stats = sub_stats.sort_values(['category', 'count'], ascending=[True, False])
        
        for _, row in sub_stats.iterrows():
            sub_data = df[(df['category'] == row['category']) & (df['subreddit'] == row['subreddit'])]['sentiment_score']
            ci = compute_95_ci(sub_data)
            f.write(f"| {row['category']} | {row['subreddit']} | {int(row['count'])} | {row['mean']:.4f} | {row['std']:.4f} | {ci[0]:.4f} | {ci[1]:.4f} |\n")
    
    print(f"Stats saved to: {output_file}")

if __name__ == "__main__":
    main()
