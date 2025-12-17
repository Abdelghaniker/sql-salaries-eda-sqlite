import numpy as np
import pandas as pd

def overview(df: pd.DataFrame) -> None:
    """Quick EDA overview."""
    print("Shape:", df.shape)
    print("\nHead:")
    print(df.head())
    print("\nDtypes:")
    print(df.dtypes)
    print("\nNulls:")
    print(df.isnull().sum())
    print("\nDescribe (numeric):")
    print(df.describe())

def clean_salaries(df: pd.DataFrame) -> pd.DataFrame:
    """Clean salaries dataset: replace 'Not Provided', drop nulls, convert pay columns to numeric."""
    df = df.replace("Not Provided", np.nan).dropna()

    num_cols = ["BasePay", "OvertimePay", "OtherPay", "Benefits", "TotalPay", "TotalPayBenefits"]
    for c in num_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    df = df.dropna(subset=num_cols)
    return df
