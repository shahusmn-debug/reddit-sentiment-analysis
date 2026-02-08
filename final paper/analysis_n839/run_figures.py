"""
Figure Generation for Filtered Dataset (N=839)
Generates all figures using the 2021-only filtered data
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

# Paths
DATA_DIR = r"c:\Users\Usman\Projects\Autoscholar\IDEPaper\final paper\data"
OUTPUT_DIR = r"c:\Users\Usman\Projects\Autoscholar\IDEPaper\final paper\analysis_n839\figures"

plt.style.use('seaborn-v0_8-whitegrid')

def compute_95_ci(data):
    n = len(data)
    if n < 2:
        return (np.nan, np.nan)
    mean = np.mean(data)
    sem = stats.sem(data)
    ci = stats.t.interval(0.95, n-1, loc=mean, scale=sem)
    return ci

# ==============================================================================
# FIGURE 1: Category Comparison
# ==============================================================================
def fig1_category_comparison(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    
    stats_data = []
    for category in ['blue_collar', 'white_collar']:
        data = df[df['category'] == category]['sentiment_score']
        mean = data.mean()
        ci = compute_95_ci(data)
        stats_data.append({
            'category': category.replace('_', ' ').title(),
            'mean': mean,
            'ci_lower': ci[0],
            'ci_upper': ci[1]
        })
    
    stats_df = pd.DataFrame(stats_data)
    colors = ['#1f77b4', '#ff7f0e']
    bars = ax.bar(stats_df['category'], stats_df['mean'], color=colors, 
                  edgecolor='black', linewidth=1.5)
    
    ax.errorbar(stats_df['category'], stats_df['mean'],
                yerr=[stats_df['mean'] - stats_df['ci_lower'], 
                      stats_df['ci_upper'] - stats_df['mean']],
                fmt='none', color='black', capsize=5, capthick=2)
    
    # Add value labels on bars
    for i, (bar, mean_val) in enumerate(zip(bars, stats_df['mean'])):
        y_offset = 0.08 if mean_val >= 0 else -0.12
        ax.text(bar.get_x() + bar.get_width()/2, mean_val + y_offset, 
                f'M = {mean_val:.3f}', ha='center', va='bottom' if mean_val >= 0 else 'top',
                fontsize=11, fontweight='bold')
    
    ax.axhline(0, color='gray', linestyle='--', alpha=0.7)
    ax.set_ylabel('Mean Sentiment Score', fontsize=12)
    ax.set_xlabel('Occupational Category', fontsize=12)
    ax.set_ylim(-1, 1)
    ax.set_title('Mean Sentiment Score by Occupational Category (N=839)', fontsize=14)
    
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/fig_category_sentiment_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Created Figure 1: Category Comparison")

# ==============================================================================
# FIGURE 2: Stacked Distribution
# ==============================================================================
def fig2_stacked_distribution(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    props = pd.crosstab(df['category'], df['gemini_sentiment'], normalize='index') * 100
    props = props[['positive', 'neutral', 'negative']]
    
    colors = {'positive': '#2ecc71', 'neutral': '#95a5a6', 'negative': '#e74c3c'}
    
    props.plot(kind='bar', stacked=True, ax=ax, 
               color=[colors[c] for c in props.columns],
               edgecolor='black', linewidth=0.5)
    
    # Add percentage labels on each segment
    for i, category in enumerate(props.index):
        cumulative = 0
        for col in props.columns:
            val = props.loc[category, col]
            if val > 5:  # Only show if segment is large enough
                ax.text(i, cumulative + val/2, f'{val:.1f}%', 
                        ha='center', va='center', fontsize=10, fontweight='bold', color='white')
            cumulative += val
    
    ax.set_ylabel('Percentage (%)', fontsize=12)
    ax.set_xlabel('Occupational Category', fontsize=12)
    ax.set_xticklabels(['Blue Collar', 'White Collar'], rotation=0)
    ax.legend(title='Sentiment', loc='upper right')
    ax.set_title('Sentiment Distribution by Category (N=839)', fontsize=14)
    
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/fig_sentiment_distribution_stacked.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Created Figure 2: Stacked Distribution")

# ==============================================================================
# FIGURE 3: White Collar Lollipop
# ==============================================================================
def fig3_white_collar_lollipop(df):
    df_wc = df[df['category'] == 'white_collar'].copy()
    stats_df = df_wc.groupby('subreddit')['sentiment_score'].agg(['mean', 'count']).reset_index()
    stats_df = stats_df.sort_values('count', ascending=True)
    
    fig, ax = plt.subplots(figsize=(10, 7))
    my_range = range(1, len(stats_df) + 1)
    
    ax.hlines(y=my_range, xmin=0, xmax=stats_df['mean'], color='grey', alpha=0.4, linewidth=1)
    
    sizes = stats_df['count']
    size_scaled = ((sizes - sizes.min()) / (sizes.max() - sizes.min()) * 500) + 100 if sizes.max() != sizes.min() else [300]*len(sizes)
    
    ax.scatter(stats_df['mean'], my_range, color='#ff7f0e', s=size_scaled, 
               alpha=0.9, edgecolor='black', linewidth=0.5)
    
    for i, (_, row) in enumerate(stats_df.iterrows()):
        offset = 0.05 if row['mean'] >= 0 else -0.05
        ha = 'left' if row['mean'] >= 0 else 'right'
        ax.text(row['mean'] + offset, i+1, f"N={int(row['count'])}", 
                ha=ha, va='center', fontsize=9)
    
    ax.set_yticks(my_range)
    ax.set_yticklabels(stats_df['subreddit'], fontsize=11, fontweight='medium')
    ax.set_xlabel('Mean Sentiment Score', fontsize=10)
    ax.set_title('White Collar Subreddits: Sentiment vs. Volume (N=839)', fontsize=14, pad=20)
    ax.set_xlim(-1.15, 1.15)
    ax.axvline(0, color='black', linestyle='-', linewidth=0.8, alpha=0.5)
    
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/fig_sentiment_white_collar_lollipop.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Created Figure 3: White Collar Lollipop")

# ==============================================================================
# FIGURE 4: Blue Collar Lollipop
# ==============================================================================
def fig4_blue_collar_lollipop(df):
    df_bc = df[df['category'] == 'blue_collar'].copy()
    stats_df = df_bc.groupby('subreddit')['sentiment_score'].agg(['mean', 'count']).reset_index()
    stats_df = stats_df.sort_values('count', ascending=True)
    
    fig, ax = plt.subplots(figsize=(10, 7))
    my_range = range(1, len(stats_df) + 1)
    
    ax.hlines(y=my_range, xmin=0, xmax=stats_df['mean'], color='grey', alpha=0.4, linewidth=1)
    
    sizes = stats_df['count']
    if sizes.max() != sizes.min():
        size_scaled = ((sizes - sizes.min()) / (sizes.max() - sizes.min()) * 500) + 100
    else:
        size_scaled = [300] * len(sizes)
    
    ax.scatter(stats_df['mean'], my_range, color='#1f77b4', s=size_scaled, 
               alpha=0.9, edgecolor='black', linewidth=0.5)
    
    for i, (_, row) in enumerate(stats_df.iterrows()):
        offset = 0.05 if row['mean'] >= 0 else -0.05
        ha = 'left' if row['mean'] >= 0 else 'right'
        ax.text(row['mean'] + offset, i+1, f"N={int(row['count'])}", 
                ha=ha, va='center', fontsize=9)
    
    ax.set_yticks(my_range)
    ax.set_yticklabels(stats_df['subreddit'], fontsize=11, fontweight='medium')
    ax.set_xlabel('Mean Sentiment Score', fontsize=10)
    ax.set_title('Blue Collar Subreddits: Sentiment vs. Volume (N=839)', fontsize=14, pad=20)
    ax.set_xlim(-1.15, 1.15)
    ax.axvline(0, color='black', linestyle='-', linewidth=0.8, alpha=0.5)
    
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/fig_sentiment_blue_collar_lollipop.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Created Figure 4: Blue Collar Lollipop")

# ==============================================================================
# FIGURE 5: Karma vs Sentiment
# ==============================================================================
def fig5_karma_vs_sentiment(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    order = ['negative', 'neutral', 'positive']
    
    sns.boxplot(x='gemini_sentiment', y='score', data=df, order=order,
                palette='coolwarm', showfliers=False, ax=ax)
    
    sns.stripplot(x='gemini_sentiment', y='score', data=df, order=order,
                  color='black', alpha=0.2, jitter=True, size=1.5, ax=ax)
    
    ax.set_yscale('symlog')
    
    counts = df.groupby('gemini_sentiment').size()
    labels = [f'{s.title()}\n(n={counts.get(s, 0)})' for s in order]
    ax.set_xticklabels(labels)
    
    ax.set_ylabel('Karma Score (SymLog Scale)', fontsize=12)
    ax.set_xlabel('Sentiment Category', fontsize=12)
    ax.set_title('Distribution of Karma Scores by Sentiment (N=839)', fontsize=14)
    
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/fig_karma_vs_sentiment.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Created Figure 5: Karma vs Sentiment")

# ==============================================================================
# MAIN
# ==============================================================================
def main():
    df = pd.read_csv(f"{DATA_DIR}/reddit_data_2021_filtered.csv")
    print(f"Loaded N={len(df)} records (filtered 2021 data)")
    
    fig1_category_comparison(df)
    fig2_stacked_distribution(df)
    fig3_white_collar_lollipop(df)
    fig4_blue_collar_lollipop(df)
    fig5_karma_vs_sentiment(df)
    
    print(f"\nAll figures saved to: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
