from data_collection.scrape_books import scrape_books
from data_processing.clean_data import clean_data
from analysis.descriptive_stats import descriptive_stats
from analysis.predictive_analysis import predictive_analysis
from visualizations.plots import create_plots

def main():
    print("Step 1: Scraping books data...")
    scrape_books(pages=5, output_file="books_raw.csv")

    print("\nStep 2: Cleaning data...")
    clean_data(input_file="books_raw.csv", output_file="books_clean.csv")

    print("\nStep 3: Descriptive Statistics...")
    descriptive_stats(input_file="books_clean.csv")

    print("\nStep 4: Predictive Analysis...")
    predictive_analysis(input_file="books_clean.csv")

    print("\nStep 5: Generating Visualizations...")
    create_plots(input_file="books_clean.csv")

if __name__ == "__main__":
    main()
