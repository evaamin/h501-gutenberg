import pandas as pd


def get_data():
    # load authors and metadata, merge them on author id
    base_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/"
    authors = pd.read_csv(base_url + "gutenberg_authors.csv")
    metadata = pd.read_csv(base_url + "gutenberg_metadata.csv")
    return authors.merge(metadata.drop(columns="author"), on="gutenberg_author_id")
