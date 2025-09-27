
import pandas as pd
import numpy as np
import math

def age_splitter(df, col_name, age_threshold):
    """
    Splits the dataframe into two dataframes based on an age threshold.

    Parameters:
    df (pd.DataFrame): The input dataframe.
    col_name (str): The name of the column containing age values.
    age_threshold (int): The age threshold for splitting.

    Returns:
    tuple: A tuple containing two dataframes:
        - df_below: DataFrame with rows where age is below the threshold.
        - df_above_equal: DataFrame with rows where age is above or equal to the threshold.
    """
    pass

def cohenEffectSize(group1, group2):
    # You need to implement this helper function
    # This should not be too hard...
    Group1 = np.array(group1)
    Group2 = np.array(group2)
    
    mean1, mean2 = group1.mean(), group2.mean()
    std1, std2 = group1.std(ddof=1), group2.std(ddof=1)
    n1, n2 = len(group1), len(group2)
    
    pooled_std = np.sqrt(((n1-1)*std1**2 + (n2-1)*std2**2)/(n1+n2-2))
    
    return (mean1 - mean2) / pooled_std
    pass

def effectSizer(df, num_col, cat_col):
    unique_vals = df[cat_col].dropna().unique()
    
    if len(unique_vals) != 2:
        raise ValueError(f"{cat_col} must have exactly 2 categories")
    
    x1, x2 = unique_vals
    group1 = df[df[cat_col] == x1][num_col].dropna()
    group2 = df[df[cat_col] == x2][num_col].dropna()
    
    d = cohenEffectSize(group1, group2)
    return {x1: d, x2: -d}
    """
    Calculates the effect sizes of binary categorical classes on a numerical value.

    Parameters:
    df (pd.DataFrame): The input dataframe.
    num_col (str): The name of the numerical column.
    cat_col (str): The name of the binary categorical column.

    Returns:
    float: Cohen's d effect size between the two groups defined by the categorical column.
    Raises:
    ValueError: If the categorical column does not have exactly two unique values.
    """
    pass




    pass

def cohortCompare(df, cohorts, statistics=['mean', 'median', 'std', 'min', 'max']):
    """
    This function takes a dataframe and a list of cohort column names, and returns a dictionary
    where each key is a cohort name and each value is an object containing the specified statistics
    """
    results = {}
    
    for col in cohorts:
        cohort = CohortMetric(cohort_name=col)
        
        # Numerical columns
        if np.issubdtype(df[col].dtype, np.number):
            cohort.setMean(df[col].mean())
            cohort.setMedian(df[col].median())
            cohort.setStd(df[col].std())
            cohort.setMin(df[col].min())
            cohort.setMax(df[col].max())
        
        # Categorical columns
        else:
            counts = df[col].value_counts()
            # Store counts in the 'mean' field just for printing purposes
            cohort.setMean(counts)
        
        results[col] = cohort
    
    return results
    pass
  

class CohortMetric():
    # don't change this
    def __init__(self, cohort_name):
        self.cohort_name = cohort_name
        self.statistics = {
            "mean": None,
            "median": None,
            "std": None,
            "min": None,
            "max": None
        }
    def setMean(self, new_mean):
        self.statistics["mean"] = new_mean
    def setMedian(self, new_median):
        self.statistics["median"] = new_median
    def setStd(self, new_std):
        self.statistics["std"] = new_std
    def setMin(self, new_min):
        self.statistics["min"] = new_min
    def setMax(self, new_max):
        self.statistics["max"] = new_max

    def compare_to(self, other):
        for stat in self.statistics:
            if not self.statistics[stat].equals(other.statistics[stat]):
                return False
        return True
    def __str__(self):
        output_string = f"\nCohort: {self.cohort_name}\n"
        for stat, value in self.statistics.items():
            output_string += f"\t{stat}:\n{value}\n"
            output_string += "\n"
        return output_string
