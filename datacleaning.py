import pandas as pd
data={
    "Name":["Pravin","Amit","Rahul"],
    "salary":[50000,None,70000]
}
df = pd.DataFrame(data)
print("Original data")
print(df)
df["Salary"] = df["salary"].fillna(df["salary"].mean())
print("Cleaned data")
print(df)