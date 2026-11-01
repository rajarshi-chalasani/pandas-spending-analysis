import pandas as pd

df = pd.read_csv("spending.csv")
print(df)
print(df.info())
print(df.isna().sum())
df["date"] = pd.to_datetime(df["date"])
df["amount"] = df["amount"].fillna(0)
df["category"] = df["category"].fillna("Unknown")
print(df)
df.info()
print("Total spent:", df["amount"].sum())
print(df.groupby("category")["amount"].sum())
import matplotlib.pyplot as plt

totals = df.groupby("category")["amount"].sum()
totals.plot(kind="bar", title="Spending by category")
plt.ylabel("Dollars")
plt.tight_layout()
plt.savefig("spending_chart.png")
plt.show()