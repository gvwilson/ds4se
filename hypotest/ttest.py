"""Two-sample t-test comparing Python and JavaScript line lengths."""
import polars as pl
from scipy import stats

py = pl.read_csv("data/py_line_lengths.csv")
js = pl.read_csv("data/js_line_lengths.csv")

py_medians = py.group_by("file_id").agg(pl.col("line_length").median())["line_length"]
js_medians = js.group_by("file_id").agg(pl.col("line_length").median())["line_length"]

result = stats.ttest_ind(py_medians.to_numpy(), js_medians.to_numpy())
print(f"t-statistic: {result.statistic:.2f}")
print(f"p-value: {result.pvalue:.2e}")
print(f"95% CI: {result.confidence_interval(0.95)}")
