from data_collection.scrape_books import scrape_books
from data_processing.clean_data import clean_data
from analysis.descriptive_stats import analyze_data
from analysis.predictive_model import predictive_model

def main():
    # Step 1: Collect the data
    data = scrape_books()

    # Step 2: Clean the data
    clean_df = clean_data(data)

    # Step 3: Analyze the data
    analyze_data(clean_df)

    # Step 4: Build predictive model
    predictive_model(clean_df)

if __name__ == '__main__':
    main()
