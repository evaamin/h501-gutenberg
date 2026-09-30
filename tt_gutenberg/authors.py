from .utils import load_data, ct_langs


def list_authors(by_languages=True, alias=True):
    # list authors/aliases ordered by translation count, most to fewest
    authors, metadata, languages = load_data()
    counts = ct_langs(metadata, languages)

    name_col = "alias" if alias else "author"
    df = authors.merge(counts, on="gutenberg_author_id")
    df = df.dropna(subset=[name_col])

    if by_languages:
        df = df.sort_values(["translation_count", name_col], ascending=[False, True])
    else:
        df = df.sort_values(name_col)

    return df[name_col].drop_duplicates().tolist()

