"""Compute percent agreement and Cohen's kappa for two coders."""
from collections import Counter


def cohen_kappa(coder_a, coder_b):
    """Compute Cohen's kappa for two lists of categorical labels."""
    n = len(coder_a)
    assert len(coder_b) == n, "Coders must label the same number of items"
    categories = list(set(coder_a) | set(coder_b))
    observed_agreement = sum(a == b for a, b in zip(coder_a, coder_b)) / n
    count_a = Counter(coder_a)
    count_b = Counter(coder_b)
    expected_agreement = sum((count_a[c] / n) * (count_b[c] / n) for c in categories)
    kappa = (observed_agreement - expected_agreement) / (1 - expected_agreement)
    return observed_agreement, kappa


if __name__ == "__main__":
    # Example: two coders classify pull request comments
    coder_a = ["change", "question", "approve", "change", "change",
               "question", "approve", "approve", "change", "question"]
    coder_b = ["change", "approve", "approve", "change", "question",
               "question", "approve", "approve", "change", "question"]
    pct, kappa = cohen_kappa(coder_a, coder_b)
    print(f"Percent agreement: {pct:.1%}")
    print(f"Cohen's kappa: {kappa:.3f}")
    label = (
        "poor" if kappa < 0.4
        else "moderate" if kappa < 0.6
        else "substantial" if kappa < 0.8
        else "near-perfect"
    )
    print(f"Interpretation: {label}")
