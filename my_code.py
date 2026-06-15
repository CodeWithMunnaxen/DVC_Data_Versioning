import pandas as pd

df = pd.read_csv("students.csv")

print(df)
print("Average Marks:", df["marks"].mean())