import pandas as pd
from scipy.stats import pearsonr

def compute_pearson_r(df, numerical_columns=None):
    """
    Computes Pearson correlation coefficients between all pairs of numerical columns in a DataFrame.

    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - numerical_columns (list, optional): A list of numerical column names to include. 
      If None, all numeric columns in the DataFrame will be used.

    Returns:
    - pd.DataFrame: A DataFrame with pairs of variables, Pearson's r, p-values,
      correlation direction, and strength.
    """
    # Select numeric columns if not explicitly provided
    if numerical_columns is None:
        numerical_columns = df.select_dtypes(include=['number']).columns.tolist()
    else:
        # Filter DataFrame to only include specified columns
        df = df[numerical_columns]

    results = []

    # Loop through all unique pairs of columns
    for i in range(len(numerical_columns)):
        for j in range(i + 1, len(numerical_columns)):
            col1, col2 = numerical_columns[i], numerical_columns[j]
            r_value, p_value = pearsonr(df[col1], df[col2])

            # Interpret direction and strength
            direction = (
                "Positive" if r_value > 0 else 
                "Negative" if r_value < 0 else 
                "No correlation"
            )
            abs_r = abs(r_value)
            strength = (
                "Strong" if abs_r >= 0.7 else 
                "Moderate" if abs_r >= 0.3 else 
                "Weak"
            )

            results.append({
                "Variable 1": col1,
                "Variable 2": col2,
                "Pearson's r": round(r_value, 4),
                "P-value": round(p_value, 4),
                "Direction": direction,
                "Strength": strength
            })

    return pd.DataFrame(results)

# Example usage
# Automatically detects numeric columns
pearson_results_df = compute_pearson_r(df)
display(pearson_results_df)