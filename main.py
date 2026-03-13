#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
from data import get_stock_data, read_data

def compute_returns(df):
    """
    Calcula rendimientos porcentuales
    """

    df["return"] = df["Close"].pct_change()

    return df

def plot_price(df):

    plt.figure()
    plt.plot(df["Close"])
    plt.title("S&P500 últimos 5 años")
    plt.xlabel("Tiempo")
    plt.ylabel("Precio")
    plt.show()


def plot_returns(df):
    plt.figure()
    plt.plot(df["return"])
    plt.title("Rendimientos del S&P500")
    plt.xlabel("Tiempo")
    plt.ylabel("Return")
    plt.show()


def main():
    # descargar datos
    get_stock_data()
    # leer datos
    df = read_data()
    # calcular rendimientos
    df = compute_returns(df)
    # graficas
    plot_price(df)
    plot_returns(df)

if __name__ == "__main__":
    main()
