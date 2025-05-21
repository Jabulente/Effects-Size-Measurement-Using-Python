import re
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Utility: Clean variable names for formula compatibility
def rename(text):
    return re.sub(r'[^a-zA-Z0-9]', "", text)

# Helper: Calculate Eta-squared from ANOVA table
def calculate_eta_squared(aov_table):
    ss_between = aov_table["sum_sq"].iloc[0]
    ss_total = aov_table["sum_sq"].sum()
    return ss_between / ss_total

# Helper: Run ANOVA and calculate Eta-squared
def perform_anova(data, dependent_var, independent_var):
    formula = f"{dependent_var} ~ C({independent_var})"
    model = ols(formula, data=data).fit()
    aov_table = sm.stats.anova_lm(model, typ=2)
    
    eta_sq = calculate_eta_squared(aov_table)
    aov_table["Eta-squared (η²)"] = np.nan
    aov_table.loc[f"C({independent_var})", "Eta-squared (η²)"] = eta_sq
    
    return aov_table.reset_index().rename(columns={"index": "Source"})

# Main: Compute eta squared for multiple dependent variables
def compute_eta_squared(df, independent_variable, dependent_variables):
    results = []
    for dep_var in dependent_variables:
        safe_dep = rename(dep_var)
        temp_df = df.rename(columns={dep_var: safe_dep})  # Non-destructive rename

        aov_df = perform_anova(temp_df, safe_dep, independent_variable)
        aov_df.insert(0, "Dependent Variable", dep_var)  # Preserve original name
        results.append(aov_df)

    results = pd.concat(results, ignore_index=True).fillna("-")
    return results