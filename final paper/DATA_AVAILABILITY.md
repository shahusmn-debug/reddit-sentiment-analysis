# Data Availability Statement

## Dataset

The anonymized dataset used in this study is available in the `data/` directory:

**File:** `reddit_data_2021_filtered.csv`

## Data Description

The dataset contains 839 records of Reddit posts and comments collected from 17 profession-specific subreddits during the period January 1, 2021 to December 31, 2021.

### Variables

| Variable | Type | Description |
|----------|------|-------------|
| `subreddit` | String | Name of the subreddit where content was posted |
| `category` | String | Occupational category: "blue_collar" or "white_collar" |
| `type` | String | Content type: "post" or "comment" |
| `text` | String | Text content of the post/comment |
| `score` | Integer | Reddit karma score (upvotes - downvotes) |
| `created_utc` | Timestamp | UTC timestamp of content creation |
| `gemini_sentiment` | String | LLM-classified sentiment: "positive", "neutral", or "negative" |
| `sentiment_score` | Integer | Numeric sentiment: +1 (positive), 0 (neutral), -1 (negative) |

### Privacy and Anonymization

- All Reddit usernames have been removed from the dataset
- Post/comment IDs have been anonymized
- Only publicly available content was collected
- No personally identifiable information (PII) is present

## Access

The complete dataset is provided with this submission in the `data/` folder. For questions regarding the data, please contact the corresponding author.

## Licensing

This dataset is derived from publicly available Reddit content and is provided for academic research purposes only.
