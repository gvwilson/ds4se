"""Compute PEP 8 line-length compliance from file data."""

import polars as pl

df = pl.read_csv("data/line_lengths.csv")
print("Shape:", df.shape)
print("Columns:", df.columns)
print(df.head())

clean = df.drop_nulls("line_length")
total = clean["count"].sum()
over79 = clean.filter(pl.col("line_length") > 79)["count"].sum()
print(f"Lines over 79 chars: {over79:,} / {total:,} = {over79 / total:.1%}")
clean.write_csv("data/line_lengths_clean.csv")
