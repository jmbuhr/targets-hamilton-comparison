from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm


def get_data(file: str) -> pd.DataFrame:
    return pd.read_csv(file).dropna()


def fit_model(data: pd.DataFrame) -> Tuple[float, float]:
    return tuple(sm.OLS(data["Ozone"], sm.add_constant(data["Temp"])).fit().params)


def plot_model(
    model: Tuple[float, float], data: pd.DataFrame
) -> Tuple[plt.Figure, plt.Axes]:
    fig, ax = plt.subplots()
    ax.scatter(data["Temp"], data["Ozone"])
    x = np.linspace(data["Temp"].min(), data["Temp"].max(), 100)
    y = model[0] + model[1] * x
    ax.plot(x, y, color="black")

    return fig, ax
