from typing import Callable

from utils import (
    get_project_toml_data,
    parse_args,
)

TEST_SETS = [3, 5, 7, 9, 11, 13, 17, 20]
SOLVERS: list[tuple[str, Callable, list[int], bool]] = []
SOLVER_COUNT = len(SOLVERS)
PASSED_COUNT = [0] * SOLVER_COUNT


if __name__ == "__main__":
    __toml = get_project_toml_data()
    args = parse_args(
        prog=__toml["name"],
        desc=__toml["description"],
        wrappers=[],
    )

    plot_data: dict[str, list[tuple[str, float, float, bool]]] = {}

    print("+ Testing")
    print("\n+ Summary")
    if args.metrics:
        print("\n+ Plotting")
