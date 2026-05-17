"""Compute Gini coefficient and Lorenz curve for contributor data."""
import numpy as np
import polars as pl


def gini(values):
    """Compute Gini coefficient for an array of non-negative values."""
    arr = np.sort(np.array(values, dtype=float))
    n = len(arr)
    index = np.arange(1, n + 1)
    return (2 * (index * arr).sum() / (n * arr.sum())) - (n + 1) / n


projects = ["numpy", "scikit-learn", "shell-novice"]
for project in projects:
    df = pl.read_csv(f"data/{project}_commits.csv")
    g = gini(df["commit_count"].to_numpy())
    top_share = df["commit_count"].max() / df["commit_count"].sum()
    print(f"{project}: Gini = {g:.3f}, top contributor share = {top_share:.1%}")
