from data_collection.scrape_books import scrape_books
from data_processing.clean_data import clean_books_data
from analysis.descriptive_stats import summarize
from analysis.advanced_stats import advanced_stats
from analysis.predictive_model import price_predictor
from visualizations.plots import plot_hist, plot_scatter
from visualizations.interactive_plots import interactive_hist

if __name__ == "__main__":
    # Collect and save raw data
    df_raw = scrape_books(pages=3)
    # Clean data
    df_clean = clean_books_data("books_data.csv")
    # Stats and analysis
    summarize(df_clean)
    advanced_stats(df_clean)
    # Visualizations
    plot_hist(df_clean)
    plot_scatter(df_clean)
    interactive_hist(df_clean)
    # Predictive model
    price_predictor(df_clean)
