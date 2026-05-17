"""Correlation and regression for lines vs. functions per file."""

import polars as pl
from scipy import stats

py = pl.read_csv("data/py_func_counts.csv")
js = pl.read_csv("data/js_func_counts.csv")

for lang, df in [("Python", py), ("JavaScript", js)]:
    clean = df.drop_nulls(["lines", "functions"]).filter(pl.col("functions") > 0)
    r, p = stats.pearsonr(clean["lines"].to_numpy(), clean["functions"].to_numpy())
    print(f"{lang}: Pearson r = {r:.3f}, p = {p:.2e}")

# Linear regression on Python data
clean_py = py.drop_nulls(["lines", "functions"]).filter(pl.col("functions") > 0)
x = clean_py["lines"].to_numpy()
y = clean_py["functions"].to_numpy()
slope, intercept, r, p, se = stats.linregress(x, y)
print(
    f"\nPython regression: slope = {slope:.4f}, intercept = {intercept:.2f}, R² = {r**2:.3f}"
)
residuals = y - (slope * x + intercept)
print(f"Residual std: {residuals.std():.2f}")
