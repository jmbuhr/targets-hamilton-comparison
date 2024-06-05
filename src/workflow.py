from typing import Tuple

import matplotlib.pyplot as plt
import pandas as pd

from src.utils import fit_model, get_data, plot_model


def file() -> str:
    return "./data/data.csv"


def data(file: str) -> pd.DataFrame:
    return get_data(file)


def model(data: pd.DataFrame) -> Tuple[float, float]:
    return fit_model(data)


def plot(model: Tuple[float, float], data: pd.DataFrame) -> Tuple[plt.Figure, plt.Axes]:
    return plot_model(model, data)
