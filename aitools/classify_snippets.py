"""Classify Copilot-generated code snippets for security weaknesses."""

import polars as pl

# Fu et al. security categories
CATEGORIES = [
    "injection",
    "memory_management",
    "error_handling",
    "cryptography",
    "other",
    "none",
]

snippets = pl.read_csv("data/copilot_snippets.csv")
results = []
for row in snippets.iter_rows(named=True):
    print(f"\n--- Snippet {row['id']} ---")
    print(row["code"])
    compiles = input("Compiles? (y/n): ").strip().lower() == "y"
    if compiles:
        has_issue = input("Obvious security issue? (y/n): ").strip().lower() == "y"
        if has_issue:
            print(f"Categories: {', '.join(CATEGORIES)}")
            category = input("Category: ").strip()
        else:
            category = "none"
    else:
        has_issue = False
        category = "does_not_compile"
    results.append(
        {
            "id": row["id"],
            "compiles": compiles,
            "has_issue": has_issue,
            "category": category,
        }
    )

result_df = pl.DataFrame(results)
print("\nTally:")
print(result_df.group_by("category").agg(pl.len()).sort("len", descending=True))
