import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "sample_crop_yield.csv")
RESULTS_DIR = os.path.join(BASE_DIR, "results")

os.makedirs(RESULTS_DIR, exist_ok=True)


def save_plot(filename: str):
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, filename), dpi=200)
    plt.close()


def main():
    df = pd.read_csv(DATA_PATH)

    print("\nFirst 5 rows:\n")
    print(df.head())

    print("\nDataset info:\n")
    print(df.info())

    print("\nSummary statistics:\n")
    print(df.describe(numeric_only=True))

    numeric_cols = ["Yield", "Rainfall", "Temperature", "Soil_pH", "Nutrients"]
    corr = df[numeric_cols].corr()
    corr.to_csv(os.path.join(RESULTS_DIR, "correlation_matrix.csv"))

    # Yield distribution
    plt.figure(figsize=(7, 4))
    df["Yield"].hist(bins=8)
    plt.title("Yield Distribution")
    plt.xlabel("Yield")
    plt.ylabel("Frequency")
    save_plot("yield_distribution.png")

    # Rainfall vs Yield
    plt.figure(figsize=(7, 4))
    plt.scatter(df["Rainfall"], df["Yield"])
    plt.title("Rainfall vs Yield")
    plt.xlabel("Rainfall")
    plt.ylabel("Yield")
    save_plot("rainfall_vs_yield.png")

    # Temperature vs Yield
    plt.figure(figsize=(7, 4))
    plt.scatter(df["Temperature"], df["Yield"])
    plt.title("Temperature vs Yield")
    plt.xlabel("Temperature")
    plt.ylabel("Yield")
    save_plot("temperature_vs_yield.png")

    # Soil pH vs Yield
    plt.figure(figsize=(7, 4))
    plt.scatter(df["Soil_pH"], df["Yield"])
    plt.title("Soil pH vs Yield")
    plt.xlabel("Soil pH")
    plt.ylabel("Yield")
    save_plot("soilph_vs_yield.png")

    print("\nAnalysis complete. Check the results folder for plots and CSV output.")


if __name__ == "__main__":
    main()
