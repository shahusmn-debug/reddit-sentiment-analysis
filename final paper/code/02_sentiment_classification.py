"""
02_sentiment_classification.py
LLM-based Sentiment Classification Script

This script classifies Reddit posts/comments for COVID-19 vaccine sentiment
using Google's Gemini 2.5 Flash model.

NOTE: API key has been removed for publication.
Replace placeholder with your own API key.
"""

import pandas as pd
from google import genai
from google.genai import types
import time

# =============================================================================
# CONFIGURATION - Replace with your API key
# =============================================================================

GEMINI_API_KEY = "<YOUR_GEMINI_API_KEY>"

# Model settings for deterministic output
MODEL_NAME = "gemini-2.5-flash"
TEMPERATURE = 0
THINKING_BUDGET = 0

# =============================================================================
# SENTIMENT CLASSIFICATION
# =============================================================================

def create_sentiment_prompt(text):
    """Create the prompt for sentiment classification."""
    return f"""Analyze the sentiment of the following text, determining the text's opinion on COVID vaccinations, as to whether it has a positive sentiment towards COVID vaccines, a negative sentiment towards COVID vaccines, or a neutral sentiment towards COVID vaccines. Return only a single word: 'positive', 'neutral', or 'negative'.

Text: "{text}"
"""


def classify_sentiment(client, text):
    """Classify sentiment of a single text using Gemini."""
    try:
        prompt = create_sentiment_prompt(text)
        
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=TEMPERATURE,
                thinking_config=types.ThinkingConfig(thinking_budget=THINKING_BUDGET)
            )
        )
        
        # Extract and validate response
        sentiment = response.text.strip().lower()
        if sentiment in ['positive', 'neutral', 'negative']:
            return sentiment
        else:
            return 'neutral'  # Default for unclear responses
            
    except Exception as e:
        print(f"Classification error: {e}")
        return None


def sentiment_to_score(sentiment):
    """Convert sentiment label to numeric score."""
    mapping = {
        'positive': 1,
        'neutral': 0,
        'negative': -1
    }
    return mapping.get(sentiment, 0)


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    # Initialize Gemini client
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    # Load raw data
    input_file = "reddit_vaccine_data_raw.csv"
    df = pd.read_csv(input_file)
    print(f"Loaded {len(df)} records")
    
    # Classify each record
    sentiments = []
    for idx, row in df.iterrows():
        if idx % 50 == 0:
            print(f"Processing {idx}/{len(df)}...")
        
        sentiment = classify_sentiment(client, row['text'])
        sentiments.append(sentiment)
        
        time.sleep(0.5)  # Rate limiting
    
    # Add sentiment columns
    df['gemini_sentiment'] = sentiments
    df['sentiment_score'] = df['gemini_sentiment'].apply(sentiment_to_score)
    
    # Save classified data
    output_file = "reddit_data_with_gemini_sentiment.csv"
    df.to_csv(output_file, index=False)
    print(f"\nSaved classified data to {output_file}")
    
    # Summary statistics
    print("\nSentiment Distribution:")
    print(df['gemini_sentiment'].value_counts())


if __name__ == "__main__":
    main()
