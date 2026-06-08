'''
Noah Walton
IS303-A06

Movie Ratings Analysis
Analyzes movie_ratings: average rating by genre, rating vs. would_recommend, and ratings over time.

Inputs:
- movie_ratings.csv: Movie ratings dataset with columns: movie_title, genre, release_year, reviewer_id, rating_1_5, times_watched, would_recommend, platform

Processes:
- load_data(): reads the CSV file into a DataFrame.
- clean_data(): handles missing values and ensures correct data types and standardizes columns to be uniform.
- validate_data(): checks for duplicates, outliers, and consistency in the data.
- analyze_data(): performs analysis to find average ratings by genre, correlation between budget and ratings, and trends in ratings over time.
- visualize_data(): creates visualizations such as bar charts for average ratings by genre, scatter plots for budget vs. ratings, and line charts for ratings over time.

Outputs:
- Summary statistics of the dataset.
- Visualizations of the analysis results.
'''
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        print("Data loaded: success")
        print(f"Loaded {len(df)} rows and {len(df.columns)} columns.")
        return df
    except:
        print("Data loaded: failed")
        exit()

def clean_data(df):
    """Clean the data: missing values, data types, and standardization."""
    # Handle missing values
    print(f"Number of rows before cleaning: {len(df)}")
    df['times_watched'] = df['times_watched'].fillna(1)  # Assume 1 if missing, won't affect rating analysis in this case
    df['would_recommend'] = df['would_recommend'].str.strip().str.lower().map({'yes': 1, 'no': 0}) # Convert to binary
    df = df.dropna(subset=['rating_1_5'])  # Drop rows where rating is missing, as it's crucial for analysis
    print(f"Number of rows after cleaning: {len(df)}")

    # Ensure correct data types, for release_year: convert words to numbers if needed, for ratings: ensure they are numeric
    df['release_year'] = df['release_year'].replace({'two thousand twelve': 2012}).astype(int)
    
    df['rating_1_5'] = df['rating_1_5'].astype(float)
    
    # Standardize genre names
    df['genre'] = df['genre'].str.strip().str.lower()
    print("Data cleaned: success")
    return df

def validate_data(df):
    """Run assert statements to validate the data."""
    # check for duplicates
    assert df.duplicated().sum() == 0, "Data validation failed: duplicates found"
    
    # check for outliers in ratings
    assert df['rating_1_5'].between(1, 5).all(), "Data validation failed: ratings out of bounds"
    
    # check for consistency in release years
    assert df['release_year'].between(1900, 2024).all(), "Data validation failed: release years out of bounds"
    
    print("Data validation: success")

def analyze_data(df):
    """Perform analysis on the Movie Ratings dataset."""
    # Average rating by genre
    avg_rating_by_genre = df.groupby('genre')['rating_1_5'].mean()
    print("Average rating by genre:")
    print(avg_rating_by_genre)
    print("Number of movie ratings in each genre:")
    print(df.groupby('genre').size())
    
    # Correlation between would_recommend and ratings
    correlation = df['would_recommend'].corr(df['rating_1_5'])
    print("Correlation between would_recommend and ratings: ")
    print(correlation)
    
    # Trends in ratings over time
    ratings_over_time = df.groupby('release_year')['rating_1_5'].mean()
    print("Average ratings over time:")
    print(ratings_over_time)
    
    return avg_rating_by_genre, correlation, ratings_over_time

def visualize_data(df, avg_rating_by_genre, correlation, ratings_over_time):
    """Visualize the analysis results."""
    # bar chart for average ratings by genre
    avg_rating_by_genre.plot(kind='bar', color='skyblue')
    plt.title("Average Rating by Genre")
    plt.xlabel("Genre")
    plt.ylabel("Average Rating (1-5)")
    plt.tight_layout()
    plt.savefig("avg_rating_by_genre.png")
    plt.show()
    plt.clf()  # Clear the figure for the next plot
    
    # scatter plot for would_recommend vs. ratings
    plt.scatter(df['would_recommend'], df['rating_1_5'], alpha=0.5)
    plt.title("Would Recommend vs. Rating")
    plt.xlabel("Would Recommend")
    plt.ylabel("Rating (1-5)")
    plt.tight_layout()
    plt.savefig("would_recommend_vs_rating.png")
    plt.show()
    plt.clf()  # Clear the figure for the next plot
    
    # line chart for ratings over time
    ratings_over_time.plot(kind='line', color='green')
    plt.title("Ratings Over Time")
    plt.xlabel("Release Year")
    plt.ylabel("Average Rating (1-5)")
    plt.tight_layout()
    plt.savefig("ratings_over_time.png")
    plt.show()
    plt.clf()  # Clear the figure for the next plot

# Main execution

df = load_data("movie_ratings.csv")
df = clean_data(df)
validate_data(df)
avg_rating_by_genre, correlation, ratings_over_time = analyze_data(df)
visualize_data(df, avg_rating_by_genre, correlation, ratings_over_time)

# End