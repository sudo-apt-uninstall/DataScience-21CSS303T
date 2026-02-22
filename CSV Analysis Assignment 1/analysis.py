import pandas as pd
import numpy as np

def analyze_csv(file):
    df = pd.read_csv(file)

    print("\n===== DATA PREVIEW =====")
    print(df.head())

    print("\n===== BASIC INFO =====")
    df.info()

    print("\n===== STATISTICAL SUMMARY =====")
    print(df.describe())

    print("\n===== MEAN =====")
    print(df.mean(numeric_only=True))

    print("\n===== MEDIAN =====")
    print(df.median(numeric_only=True))

    print("\n===== MODE =====")
    print(df.mode(numeric_only=True).iloc[0])

    print("\n===== VARIANCE =====")
    print(df.var(numeric_only=True))

    print("\n===== STANDARD DEVIATION =====")
    print(df.std(numeric_only=True))

    print("\n===== NUMPY OPERATIONS (Salary Column) =====")
    salary_array = np.array(df['Salary'])

    print("Salary Array:", salary_array)
    print("Min Salary:", np.min(salary_array))
    print("Max Salary:", np.max(salary_array))
    print("Mean Salary:", np.mean(salary_array))
    print("Std Dev Salary:", np.std(salary_array))

if __name__ == "__main__":
    file = input("Enter CSV file path: ")
    analyze_csv(file)