"""Compare weekday vs. weekend programmer working hours."""
import polars as pl
from scipy import stats

df = pl.read_csv("data/programmer_hours.csv")
weekday = df.filter(pl.col("day_type") == "weekday")["hours"].to_numpy()
weekend = df.filter(pl.col("day_type") == "weekend")["hours"].to_numpy()

print(f"Weekday mean: {weekday.mean():.1f} hours")
print(f"Weekend mean: {weekend.mean():.1f} hours")

t_result = stats.ttest_ind(weekday, weekend)
print(f"\nt-test: t = {t_result.statistic:.1f}, p = {t_result.pvalue:.2e}")

mw_result = stats.mannwhitneyu(weekday, weekend, alternative="two-sided")
print(f"Mann-Whitney U: U = {mw_result.statistic:.0f}, p = {mw_result.pvalue:.2e}")
