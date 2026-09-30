from . import transform


def list_authors(by_languages=True, alias=True):
    # list authors/aliases ordered by translation count, most to fewest
    df = transform.get_data()
    name_col = "alias" if alias else "author"
    df = df.dropna(subset=[name_col])

    if by_languages:
        # count distinct languages per name, ties broken alphabetically
        counts = (
            df.groupby(name_col)["language"]
            .nunique()
            .reset_index(name="translation_count")
        )
        counts = counts.sort_values(
            ["translation_count", name_col], ascending=[False, True]
        )
        return counts[name_col].tolist()

    return sorted(df[name_col].unique().tolist())
