"""Compare replication results to published Fucci et al. (2016) values."""
import polars as pl

published = pl.DataFrame({
    "outcome": ["TESTS", "QLTY", "PROD"],
    "pub_p": [0.052, 0.380, 0.890],
    "pub_delta": [0.19, 0.12, 0.02]
})

# Load your replication results (produced by tddlab/replicate_fucci.py)
try:
    replicated = pl.read_csv("data/fucci_replication.csv")
    combined = published.join(replicated, on="outcome")
    combined = combined.with_columns(
        (pl.col("rep_p") - pl.col("pub_p")).abs().alias("p_diff"),
        (pl.col("rep_delta") - pl.col("pub_delta")).abs().alias("delta_diff")
    )
    print(combined.select(["outcome", "pub_p", "rep_p", "p_diff", "pub_delta", "rep_delta", "delta_diff"]))
except Exception as e:
    print(f"Could not load replication data: {e}")
    print("Published values:")
    print(published)
