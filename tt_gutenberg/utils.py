import pandas as pd


def load_data():
    # load TidyTuesday Gutenberg tables
    # return authors, metadata, and languages
    base_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/"
    authors = pd.read_csv(base_url + "gutenberg_authors.csv")
    metadata = pd.read_csv(base_url + "gutenberg_metadata.csv")
    languages = pd.read_csv(base_url + "gutenberg_languages.csv")
    return authors, metadata, languages

def ct_langs(metadata, languages):
    # count distinct languages per author across all their books
    book_langs = metadata[["gutenberg_id", "gutenberg_author_id"]].merge(
        languages[["gutenberg_id", "language"]], on="gutenberg_id"
    )
    counts = (
        book_langs.groupby("gutenberg_author_id")["language"]
        .nunique()
        .reset_index(name="translation_count")
    )
    return counts
