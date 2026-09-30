import pandas as pd

# source CSVs for the TidyTuesday Gutenberg dataset
DATA = {
    "authors": (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_authors.csv"
    ),
    "metadata": (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_metadata.csv"
    ),
}


def get_data():
    # load authors and metadata from DATA, merge them on author id
    authors = pd.read_csv(DATA["authors"])
    metadata = pd.read_csv(DATA["metadata"])
    # drop metadata's author column to avoid author_x/author_y
    metadata = metadata.drop(columns="author")
    return authors.merge(metadata, on="gutenberg_author_id")
