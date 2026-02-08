"""
01_data_collection.py
Reddit Data Collection Script for COVID-19 Vaccine Sentiment Study

This script collects posts and comments from specified subreddits
containing vaccine-related keywords.

NOTE: API credentials have been removed for publication.
Replace placeholder values with your own credentials.
"""

import praw
import pandas as pd
from datetime import datetime
import time

# =============================================================================
# CONFIGURATION - Replace with your credentials
# =============================================================================

REDDIT_CLIENT_ID = "<YOUR_CLIENT_ID>"
REDDIT_CLIENT_SECRET = "<YOUR_CLIENT_SECRET>"
REDDIT_USER_AGENT = "VaccineSentimentStudy/1.0"

# Study parameters
START_DATE = datetime(2021, 1, 1)
END_DATE = datetime(2021, 12, 31)

KEYWORDS = ["vaccine", "vaccinated", "vaccination", "pfizer", "moderna", "j&j"]

SUBREDDITS = {
    "blue_collar": [
        "Carpentry", "electricians", "Construction", "Welding", "Plumbing",
        "Machinists", "Truckers", "AutoDetailing", "Justrolledintotheshop",
        "KitchenConfidential", "ProtectAndServe", "Firefighting"
    ],
    "white_collar": [
        "consulting", "cscareerquestions", "law", "Accounting", "engineering"
    ]
}

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def contains_keyword(text, keywords):
    """Check if text contains any of the specified keywords."""
    if not text:
        return False
    text_lower = text.lower()
    return any(kw.lower() in text_lower for kw in keywords)


def collect_subreddit_data(reddit, subreddit_name, category, keywords, start_date, end_date):
    """Collect posts and comments from a subreddit containing keywords."""
    results = []
    subreddit = reddit.subreddit(subreddit_name)
    
    # Search for posts
    for keyword in keywords:
        try:
            for post in subreddit.search(keyword, time_filter="year", limit=None):
                post_date = datetime.utcfromtimestamp(post.created_utc)
                
                if start_date <= post_date <= end_date:
                    # Check if post contains keyword
                    post_text = f"{post.title} {post.selftext}"
                    if contains_keyword(post_text, keywords):
                        results.append({
                            "subreddit": subreddit_name,
                            "category": category,
                            "type": "post",
                            "text": post_text,
                            "score": post.score,
                            "created_utc": post.created_utc
                        })
                    
                    # Collect relevant comments
                    post.comments.replace_more(limit=5)
                    for comment in post.comments.list():
                        if hasattr(comment, 'body'):
                            if contains_keyword(comment.body, keywords):
                                results.append({
                                    "subreddit": subreddit_name,
                                    "category": category,
                                    "type": "comment",
                                    "text": comment.body,
                                    "score": comment.score,
                                    "created_utc": comment.created_utc
                                })
            
            time.sleep(1)  # Rate limiting
            
        except Exception as e:
            print(f"Error in {subreddit_name} for keyword '{keyword}': {e}")
    
    return results


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    # Initialize Reddit API
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )
    
    all_data = []
    
    # Collect from all subreddits
    for category, subreddit_list in SUBREDDITS.items():
        for subreddit_name in subreddit_list:
            print(f"Collecting from r/{subreddit_name} ({category})...")
            data = collect_subreddit_data(
                reddit, subreddit_name, category, 
                KEYWORDS, START_DATE, END_DATE
            )
            all_data.extend(data)
            print(f"  Found {len(data)} items")
    
    # Create DataFrame and remove duplicates
    df = pd.DataFrame(all_data)
    df = df.drop_duplicates(subset=['text'])
    
    # Save to CSV
    output_file = "reddit_vaccine_data_raw.csv"
    df.to_csv(output_file, index=False)
    print(f"\nSaved {len(df)} unique records to {output_file}")


if __name__ == "__main__":
    main()
