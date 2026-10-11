import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample Dataset
data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Age": [20, 21, 19, 22, 20, 21, 22, 19, 20, 23],
    "Percentage": [88.5, 76.0, 92.5, 81.0, 67.5, 89.0, 73.5, 95.0, 72.5, 84.0]
}

df = pd.DataFrame(data)

# --------------------
# Box Plot
# --------------------
plt.figure(figsize=(6, 4))
plt.boxplot(df["Percentage"])
plt.title("Box Plot of Percentage")
plt.ylabel("Percentage")
plt.show()

# --------------------
# Histogram
# --------------------
plt.figure(figsize=(6, 4))
plt.hist(df["Percentage"], bins=5, color="skyblue", edgecolor="black")
plt.title("Histogram of Percentage")
plt.xlabel("Percentage")
plt.ylabel("Frequency")
plt.show()

# --------------------
# Heat Map
# --------------------
plt.figure(figsize=(5, 4))
corr = df[["Age", "Percentage"]].corr()

plt.imshow(corr, cmap="coolwarm")
plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Heat Map")
plt.show()

# --------------------
# Bar Chart
# --------------------
plt.figure(figsize=(8, 4))
plt.bar(df["ID"], df["Percentage"], color="green")
plt.title("Bar Chart")
plt.xlabel("Student ID")
plt.ylabel("Percentage")
plt.show()

# --------------------
# Line Chart
# --------------------
plt.figure(figsize=(8, 4))
plt.plot(df["ID"], df["Percentage"], marker="o")
plt.title("Line Chart")
plt.xlabel("Student ID")
plt.ylabel("Percentage")
plt.grid(True)
plt.show()

# --------------------
# Pie Chart
# --------------------
plt.figure(figsize=(7, 7))
plt.pie(
    df["Percentage"][:5],
    labels=df["ID"][:5],
    autopct="%1.1f%%"
)
plt.title("Pie Chart of First 5 Students")
plt.show()

# --------------------
# Scatter Plot
# --------------------
plt.figure(figsize=(6, 4))
plt.scatter(df["Age"], df["Percentage"], color="red")
plt.title("Scatter Plot")
plt.xlabel("Age")
plt.ylabel("Percentage")
plt.show()