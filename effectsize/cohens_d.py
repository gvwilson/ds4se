"""Cohen's d and Cliff's delta for Fucci TDD study outcomes."""
import numpy as np
import polars as pl
from scipy import stats

def cohens_d(a, b):
    """Compute Cohen's d for two arrays."""
    pooled_std = np.sqrt((a.std()**2 + b.std()**2) / 2)
    return (a.mean() - b.mean()) / pooled_std

def cliffs_delta(a, b):
    """Compute Cliff's delta for two arrays."""
    n = len(a) * len(b)
    greater = sum(1 for x in a for y in b if x > y)
    less = sum(1 for x in a for y in b if x < y)
    return (greater - less) / n

df = pl.read_csv("data/fucci_tdd.csv")
tdd = df.filter(pl.col("approach") == "TDD")
tld = df.filter(pl.col("approach") == "TLD")

for outcome in ["PROD", "QLTY", "TESTS"]:
    a = tdd[outcome].drop_nulls().to_numpy()
    b = tld[outcome].drop_nulls().to_numpy()
    d = cohens_d(a, b)
    delta = cliffs_delta(a, b)
    print(f"{outcome}: Cohen's d = {d:.3f}, Cliff's delta = {delta:.3f}")
