"""Compute development-time percentiles from Prechelt data."""
import polars as pl

df = pl.read_csv("data/jccpprtTR.csv")
print("All languages:")
print(df.select(pl.col("whours").quantile(0.10).alias("p10"),
                pl.col("whours").quantile(0.50).alias("p50"),
                pl.col("whours").quantile(0.90).alias("p90")))
p10 = df["whours"].quantile(0.10)
p90 = df["whours"].quantile(0.90)
print(f"90th/10th ratio: {p90 / p10:.1f}X")

java = df.filter(pl.col("lang") == "Java")
print("\nJava only:")
print(java.select(pl.col("whours").quantile(0.10).alias("p10"),
                  pl.col("whours").quantile(0.50).alias("p50"),
                  pl.col("whours").quantile(0.90).alias("p90")))
