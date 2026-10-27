# Write a program to create a data visualization like using matplotlib with taking any datasets: Do the following 
# Create a Box plots, 
# Create a Histograms, 
# Create a Heat maps, 
# Create various Charts
import matplotlib.pyplot as plt #importing matplotlib
import pandas as pd #importing pandas library
import numpy as np  #importing numpy library

def boxPlot(df):
    plt.figure(figsize=(6, 4))
    plt.boxplot(df["Percentage"])
    plt.title("Box Plot of Percentage")
    plt.ylabel("Percentage")
    plt.show()

def histogram(df):
    plt.figure(figsize=(6, 4))
    plt.hist(df["Percentage"], bins=5, color="skyblue", edgecolor="black")
    plt.title("Histogram of Percentage")
    plt.xlabel("Percentage")
    plt.ylabel("Frequency")
    plt.show()
    
def heatmap(df):
    plt.figure(figsize=(5, 4))
    corr = df[["Age", "Percentage"]].corr()

    plt.imshow(corr, cmap="coolwarm")
    plt.colorbar()

    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.yticks(range(len(corr.columns)), corr.columns)

    plt.title("Heat Map")
    plt.show()

def barChart(df):
    plt.figure(figsize=(8, 4))
    plt.bar(df["ID"], df["Percentage"], color="green")
    plt.title("Bar Chart")
    plt.xlabel("Student ID")
    plt.ylabel("Percentage")
    plt.show()
    
def lineChart(df):
    plt.figure(figsize=(8, 4))
    plt.plot(df["ID"], df["Percentage"], marker="o")
    plt.title("Line Chart")
    plt.xlabel("Student ID")
    plt.ylabel("Percentage")
    plt.grid(True)
    plt.show()

def pieChart(df):
    plt.figure(figsize=(7, 7))
    plt.pie(
        df["Percentage"][:5],
        labels=df["ID"][:5],
        autopct="%1.1f%%"
    )
    plt.title("Pie Chart of First 5 Students")
    plt.show()

n = int(input("Enter number of Rows to Enter in DataFrame: ")) # input for total size of rows to be entered

stuIds = [] # holds ID of students
names = [] # hold names of students
percentage = [] # holds percentage of students
 
for i in range(n):
    stuId = input(f"Enter Id of student {i+1}: ") # input for id
    name = input(f"Enter Name of student {i+1}: ") # input for name
    per = input(f"Enter Percentage of student {i+1}: ") # input for percentage
    
    print("\n")
    
    stuIds.append( int(stuId) if stuId else np.nan )
    names.append( name if name else None )
    percentage.append( float(per) if per else np.nan )

data = {
    "ID": stuIds,
    "Name": names,
    "Percentage": percentage
}

df = pd.DataFrame(data)

ch = int(input("Choose the Option:---- MENU ----\n1.Box Plot\n2.Histogram\n3.Heatmap\n4.Bar Chart\n5.Line Chart\n"))


match(ch):
    case 1:
        boxPlot(df)
    case 2:
        histogram(df)
    case 3:
        heatmap(df)
    case 4:
        barChart(df)
    case 5:
        lineChart(df)
    case 6:
        pieChart(df)

