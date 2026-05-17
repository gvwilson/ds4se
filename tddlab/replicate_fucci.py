"""Replicate Mann-Whitney U and Cliff's delta from Fucci et al. (2016)."""
import numpy as np
import polars as pl
from scipy import stats


def cliffs_delta(a, b):
    n = len(a) * len(b)
    greater = sum(1 for x in a for y in b if x > y)
    less = sum(1 for x in a for y in b if x < y)
    return (greater - less) / n


df = pl.read_csv("data/fucci_tdd.csv")
tdd = df.filter(pl.col("approach") == "TDD")
tld = df.filter(pl.col("approach") == "TLD")

published = {"TESTS": (0.052, 0.19), "QLTY": (0.38, 0.12), "PROD": (0.89, 0.02)}
print(f"{'Outcome':<8} {'U':>8} {'p':>10} {'delta':>8} {'pub_p':>8} {'pub_d':>8}")
for outcome in ["TESTS", "QLTY", "PROD"]:
    a = tdd[outcome].drop_nulls().to_numpy()
    b = tld[outcome].drop_nulls().to_numpy()
    u, p = stats.mannwhitneyu(a, b, alternative="two-sided")
    delta = cliffs_delta(a, b)
    pub_p, pub_d = published[outcome]
    print(f"{outcome:<8} {u:>8.1f} {p:>10.3e} {delta:>8.3f} {pub_p:>8.3f} {pub_d:>8.3f}")
