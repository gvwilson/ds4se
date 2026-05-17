"""Descriptive statistics for PyPI release counts."""

import polars as pl

df = pl.read_csv("data/pypi_releases.csv")
counts = df["releases"]
print(f"Mean:   {counts.mean():.1f}")
print(f"Median: {counts.median():.1f}")
print(f"Std:    {counts.std():.1f}")
print(f"Max:    {counts.max()}")
for p in [10, 25, 75, 90]:
    print(f"  {p}th percentile: {counts.quantile(p / 100):.1f}")
