"""Altair visualization examples using Prechelt and function-count data."""
import altair as alt
import polars as pl

# Box plot of working hours by language (Prechelt)
prechelt = pl.read_csv("data/jccpprtTR.csv")
chart1 = (alt.Chart(prechelt.to_pandas())
          .mark_boxplot()
          .encode(x=alt.X("lang:N", title="Language"),
                  y=alt.Y("whours:Q", title="Working Hours"))
          .properties(title="Development Time by Language"))
chart1.save("figures/boxplot.html")

# Log-scale histogram of lines per file
funcs = pl.read_csv("data/py_func_counts.csv")
chart2 = (alt.Chart(funcs.to_pandas())
          .mark_bar()
          .encode(x=alt.X("lines:Q", bin=alt.Bin(maxbins=30), title="Lines per File"),
                  y=alt.Y("count():Q", scale=alt.Scale(type="log"), title="Count (log)"))
          .properties(title="Python File Sizes (log scale)"))
chart2.save("figures/file_sizes.html")
