"""Compare Python and JavaScript function sizes using groupby."""
import polars as pl

py = pl.read_csv("data/py_func_counts.csv").with_columns(pl.lit("Python").alias("language"))
js = pl.read_csv("data/js_func_counts.csv").with_columns(pl.lit("JavaScript").alias("language"))
combined = pl.concat([py, js])
combined = combined.with_columns(
    (pl.col("lines") / pl.col("functions")).alias("lines_per_func")
)
stats = (combined
         .group_by("language")
         .agg(pl.col("lines_per_func").median().alias("median"),
              pl.col("lines_per_func").mean().alias("mean"),
              pl.col("lines_per_func").std().alias("std")))
print(stats)
