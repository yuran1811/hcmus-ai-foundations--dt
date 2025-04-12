def in_bounds(r: int, c: int, nrows: int, ncols: int):
    return 0 <= r < nrows and 0 <= c < ncols


def display_ratio(_: float):
    return f"{_ * 100:.0f}/{100 - _ * 100:.0f}"


def normalize_dataset_name(_: str):
    return _.replace(" ", "_").replace("-", "_").lower()


def normalize_dataset_ratio(_: float):
    return (
        display_ratio(_)
        .replace(" ", "_")
        .replace("-", "_")
        .lower()
        .replace(":", "_vs_")
        .replace("/", "_vs_")
        .replace("(", "")
        .replace(")", "")
    )
