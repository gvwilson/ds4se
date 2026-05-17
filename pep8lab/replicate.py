"""Replicate PEP 8 compliance analysis from Bafatakis et al. (2019)."""
import polars as pl
import altair as alt

df = pl.read_csv("data/line_lengths.csv").drop_nulls("line_length")
total = df["count"].sum()
over79 = df.filter(pl.col("line_length") > 79)["count"].sum()
print(f"Overall non-compliance: {over79 / total:.1%}")

# Split by directory type
lib = df.filter(pl.col("filepath").str.contains("site-packages"))
scripts = df.filter(~pl.col("filepath").str.contains("site-packages"))
for label, subset in [("Library", lib), ("Script", scripts)]:
    t = subset["count"].sum()
    o = subset.filter(pl.col("line_length") > 79)["count"].sum()
    print(f"{label} non-compliance: {o / t:.1%}")

# Histogram with PEP 8 limit marked
chart = (alt.Chart(df.to_pandas())
         .mark_bar()
         .encode(x=alt.X("line_length:Q", bin=alt.Bin(step=10), title="Line Length (chars)"),
                 y=alt.Y("sum(count):Q", title="Total Lines"))
         .properties(title="Distribution of Python Line Lengths"))
rule = alt.Chart({"values": [{"x": 79}]}).mark_rule(color="red").encode(x="x:Q")
(chart + rule).save("figures/line_lengths.html")
