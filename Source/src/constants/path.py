import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

INP_DIR = os.path.join(ROOT_DIR, "data", "input")
OUT_DIR = os.path.join(ROOT_DIR, "data", "output")
FIG_DIR = os.path.join(ROOT_DIR.replace(os.path.basename(ROOT_DIR), ""), "Report/imgs")

DATA_WDBC = "../data/wdbc.csv"
DATA_WINE = "../data/winequality-white.csv"
# DATA_CARS = "https://archive.ics.uci.edu/dataset/19/car+evaluation"
DATA_CARS = "../data/car+evaluation/car.csv"
