"""Bootstrap confidence interval for Spearman correlation between educator rankings and Blackbox data."""

import numpy as np
import polars as pl
from scipy import stats

df = pl.read_csv("data/educator_rankings.csv")
blackbox = df["blackbox_rank"].to_numpy()

# Compute Spearman r for each educator
educator_cols = [c for c in df.columns if c.startswith("educator_")]
spearman_rs = [
    stats.spearmanr(df[col].to_numpy(), blackbox).statistic for col in educator_cols
]
print(f"Median Spearman r across educators: {np.median(spearman_rs):.3f}")

# Bootstrap 95% CI for median Spearman r
rng = np.random.default_rng(42)
n = len(spearman_rs)
boot_medians = [
    np.median(rng.choice(spearman_rs, size=n, replace=True)) for _ in range(1000)
]
lo, hi = np.percentile(boot_medians, [2.5, 97.5])
print(f"95% bootstrap CI: [{lo:.3f}, {hi:.3f}]")
