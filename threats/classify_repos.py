"""Apply Kalliamvakou criteria to classify GitHub repositories."""

import polars as pl
from scipy import stats
import datetime

df = pl.read_csv("data/github_repos.csv")
cutoff = (datetime.date.today() - datetime.timedelta(days=730)).isoformat()

not_real = df.filter(
    (pl.col("commits") < 5)
    | (pl.col("contributors") == 1)
    | (pl.col("last_commit") < cutoff)
)
print(
    f"Repositories failing Kalliamvakou criteria: {len(not_real)} / {len(df)} = {len(not_real) / len(df):.1%}"
)

r, p = stats.pearsonr(df["stars"].to_numpy(), df["commits"].to_numpy())
print(f"\nPearson r (stars vs. commits): {r:.3f}, p = {p:.2e}")
