"""
04_visualization.py
Figure Generation Script

This script generates all figures for the manuscript.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

# Set style
plt.style.use('seaborn-v0_8-whitegrid')


def figure_1_category_comparison(df, output_dir):
    """Figure 1: Mean Sentiment Comparison by Category."""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Calculate statistics
    stats_data = []
    for category in ['blue_collar', 'white_collar']:
        data = df[df['category'] == category]['sentiment_score']
        mean = data.mean()
        sem = stats.sem(data)
        ci = stats.t.interval(0.95, len(data)-1, loc=mean, scale=sem)
        stats_data.append({
            'category': category.replace('_', ' ').title(),
            'mean': mean,
            'ci_lower': ci[0],
            'ci_upper': ci[1]
        })
    
    stats_df = pd.DataFrame(stats_data)
    
    # Create bar plot
    colors = ['#1f77b4', '#ff7f0e']
    bars = ax.bar(stats_df['category'], stats_df['mean'], color=colors, 
                  edgecolor='black', linewidth=1.5)
    
    # Add error bars
    ax.errorbar(stats_df['category'], stats_df['mean'],
                yerr=[stats_df['mean'] - stats_df['ci_lower'], 
                      stats_df['ci_upper'] - stats_df['mean']],
                fmt='none', color='black', capsize=5, capthick=2)
    
    ax.axhline(0, color='gray', linestyle='--', alpha=0.7)
    ax.set_ylabel('Mean Sentiment Score', fontsize=12)
    ax.set_xlabel('Occupational Category', fontsize=12)
    ax.set_ylim(-1, 1)
    ax.set_title('Mean Sentiment Score by Occupational Category', fontsize=14)
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/fig_category_sentiment_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Created Figure 1: Category Comparison")


def figure_2_stacked_distribution(df, output_dir):
    """Figure 2: Stacked Sentiment Distribution."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Calculate proportions
    props = pd.crosstab(df['category'], df['gemini_sentiment'], normalize='index') * 100
    props = props[['positive', 'neutral', 'negative']]  # Order
    
    colors = {'positive': '#2ecc71', 'neutral': '#95a5a6', 'negative': '#e74c3c'}
    
    props.plot(kind='bar', stacked=True, ax=ax, 
               color=[colors[c] for c in props.columns],
               edgecolor='black', linewidth=0.5)
    
    ax.set_ylabel('Percentage (%)', fontsize=12)
    ax.set_xlabel('Occupational Category', fontsize=12)
    ax.set_xticklabels(['Blue Collar', 'White Collar'], rotation=0)
    ax.legend(title='Sentiment', loc='upper right')
    ax.set_title('Sentiment Distribution by Category', fontsize=14)
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/fig_sentiment_distribution_stacked.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Created Figure 2: Stacked Distribution")


def figure_lollipop(df, category, color, output_dir):
    """Lollipop chart for subreddit-level sentiment."""
    df_cat = df[df['category'] == category].copy()
    stats_df = df_cat.groupby('subreddit')['sentiment_score'].agg(['mean', 'count']).reset_index()
    stats_df = stats_df.sort_values('count', ascending=True)
    
    fig, ax = plt.subplots(figsize=(10, 7))
    my_range = range(1, len(stats_df) + 1)
    
    # Stems
    ax.hlines(y=my_range, xmin=0, xmax=stats_df['mean'], color='grey', alpha=0.4)
    
    # Points scaled by volume
    sizes = stats_df['count']
    if sizes.max() != sizes.min():
        size_scaled = ((sizes - sizes.min()) / (sizes.max() - sizes.min()) * 500) + 100
    else:
        size_scaled = [300] * len(sizes)
    
    ax.scatter(stats_df['mean'], my_range, color=color, s=size_scaled, 
               alpha=0.9, edgecolor='black', linewidth=0.5)
    
    # Labels
    for i, (_, row) in enumerate(stats_df.iterrows()):
        offset = 0.05 if row['mean'] >= 0 else -0.05
        ha = 'left' if row['mean'] >= 0 else 'right'
        ax.text(row['mean'] + offset, i+1, f"N={int(row['count'])}", 
                ha=ha, va='center', fontsize=9)
    
    ax.set_yticks(my_range)
    ax.set_yticklabels(stats_df['subreddit'], fontsize=11)
    ax.set_xlabel('Mean Sentiment Score', fontsize=12)
    ax.set_xlim(-1.15, 1.15)
    ax.axvline(0, color='black', linestyle='-', linewidth=0.8, alpha=0.5)
    
    title_cat = category.replace('_', ' ').title()
    ax.set_title(f'{title_cat} Subreddits: Sentiment vs. Volume', fontsize=14)
    
    plt.tight_layout()
    filename = f'fig_sentiment_{category}_lollipop.png'
    plt.savefig(f'{output_dir}/{filename}', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Created Lollipop: {category}")


def figure_karma_boxplot(df, output_dir):
    """Karma vs Sentiment box plot."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    order = ['negative', 'neutral', 'positive']
    
    sns.boxplot(x='gemini_sentiment', y='score', data=df, order=order,
                palette='coolwarm', showfliers=False, ax=ax)
    
    sns.stripplot(x='gemini_sentiment', y='score', data=df, order=order,
                  color='black', alpha=0.2, jitter=True, size=1.5, ax=ax)
    
    ax.set_yscale('symlog')
    
    # Add sample sizes to labels
    counts = df.groupby('gemini_sentiment').size()
    labels = [f'{s.title()}\n(n={counts.get(s, 0)})' for s in order]
    ax.set_xticklabels(labels)
    
    ax.set_ylabel('Karma Score (SymLog Scale)', fontsize=12)
    ax.set_xlabel('Sentiment Category', fontsize=12)
    ax.set_title('Distribution of Karma Scores by Sentiment', fontsize=14)
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/fig_karma_vs_sentiment.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Created Karma vs Sentiment")


# =============================================================================
# MAIN
# =============================================================================

def main():
    # Load data
    df = pd.read_csv("reddit_data_with_gemini_sentiment.csv")
    output_dir = "figures"
    
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate all figures
    figure_1_category_comparison(df, output_dir)
    figure_2_stacked_distribution(df, output_dir)
    figure_lollipop(df, 'white_collar', '#ff7f0e', output_dir)
    figure_lollipop(df, 'blue_collar', '#1f77b4', output_dir)
    figure_karma_boxplot(df, output_dir)
    
    print("\nAll figures generated successfully!")


if __name__ == "__main__":
    main()
