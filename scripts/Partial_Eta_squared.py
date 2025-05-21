import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

def interpret_eta_squared(eta_squared):
    """Interpretation based on Cohen's guidelines."""
    if eta_squared >= 0.14:
        return "Large effect size (≥ 14%)"
    elif eta_squared >= 0.06:
        return "Medium effect size (6% - 14%)"
    else:
        return "Small effect size (< 6%)"

def compute_partial_eta_squared(df, variables, categories):
    """
    Computes Partial Eta-squared (ηp²) for each numeric variable against each categorical factor.

    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - variables (list): List of numeric variable names.
    - categories (list): List of categorical variable names.

    Returns:
    - pd.DataFrame: A DataFrame with variable, factor, partial eta-squared, and interpretation.
    """
    results = []

    for var in variables:
        for cat in categories:
            import re
            def safe_rename(text): return re.sub(r'[^a-zA-Z0-9_]', "", text)
            
            # Create unique safe aliases for both variable and category
            safe_var = safe_rename(var) + "_var"
            safe_cat = safe_rename(cat) + "_cat"
            
            # Make a copy of the dataframe and apply both renames at once (non-destructive)
            temp_df = df.rename(columns={var: safe_var, cat: safe_cat})

            # Fit the ANOVA model
            formula = f'{safe_var} ~ C({safe_cat})'
            model = ols(formula, data=temp_df).fit()
            anova_table = anova_lm(model, typ=2)

            # Compute partial eta-squared
            ss_factor = anova_table.loc[f'C({safe_cat})', 'sum_sq']
            ss_error = anova_table.loc['Residual', 'sum_sq']
            eta_squared = ss_factor / (ss_factor + ss_error)

            results.append({
                "Variable": var,
                "Factor": cat,
                "Partial Eta-squared (ηp²)": eta_squared,
                "Interpretation": interpret_eta_squared(eta_squared)
            })

    return pd.DataFrame(results)