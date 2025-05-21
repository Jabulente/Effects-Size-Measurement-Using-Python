import pandas as pd
import numpy as np
from itertools import combinations

def compute_cohens_d(df, numerical_columns, group_column):
    def cohens_d(group1, group2):
        mean1, mean2 = np.mean(group1), np.mean(group2)
        std1, std2 = np.std(group1, ddof=1), np.std(group2, ddof=1)
        pooled_std = np.sqrt((std1**2 + std2**2) / 2)
        return (mean1 - mean2) / pooled_std if pooled_std != 0 else np.nan

    def interpret_d(d):
        abs_d = abs(d)
        if abs_d < 0.2:
            return "Small effect size"
        elif abs_d < 0.5:
            return "Medium effect size"
        elif abs_d < 0.8:
            return "Large effect size"
        else:
            return "Very large effect size"

    results = []

    unique_groups = df[group_column].dropna().unique()
    for var in numerical_columns:
        for group_a, group_b in combinations(unique_groups, 2):
            group1 = df[df[group_column] == group_a][var].dropna()
            group2 = df[df[group_column] == group_b][var].dropna()

            if not group1.empty and not group2.empty:
                d = cohens_d(group1, group2)
                results.append({
                    "Variable": var,
                    "Group Comparison": f"{group_a} vs {group_b}",
                    "Cohen's d": d,
                    "Interpretation": interpret_d(d)
                })

    return pd.DataFrame(results)