import pandas as pd
import warnings
import os

from pathlib import Path

BASE_DIR = str(Path(__file__).resolve().parent)
OPENML_LIST = pd.read_csv(os.path.join(BASE_DIR, "data/openml_list.csv"))

# ignore warnings
def warn(*args, **kwargs):
    pass

warnings.warn = warn

