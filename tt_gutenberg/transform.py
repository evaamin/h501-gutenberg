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


def load_table(name):
    # find the DATA entry whose key contains name, read it if it's a path
    for key, value in DATA.items():
        if name in key:
            if isinstance(value, pd.DataFrame):
                return value
            return pd.read_csv(value)
    raise KeyError(name)


def get_data():
    # load authors and metadata from DATA, merge them on author id
    authors = load_table("author")
    metadata = load_table("metadata")
    # drop metadata's author column to avoid author_x/author_y
    metadata = metadata.drop(columns="author", errors="ignore")
    return authors.merge(metadata, on="gutenberg_author_id")
