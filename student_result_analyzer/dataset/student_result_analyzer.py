import pandas as pd  #-->CSV handle
import matplotlib.pyplot as plt #-->basic graphs
import seaborn as sns #-->advance graphs

df = pd.read_csv("students.csv")

# ==========================
# Data Analysis
# ==========================
df["Total"] = df["Maths"] + df["Science"] + df["English"] + df["Computer"]

df["Percentage"] = (df["Total"]/400)*100
df["Percentage"] = round(df["Percentage"],2)

df["Average"] = df["Total"]/4
df["Average"] = round(df["Average"],2)

def grade(p):
    if p>=90:
        return "A"
    elif p>=75:
        return "B"
    elif p>=60:
        return "C"
    elif p>=40:
        return "D"
    else:
        return "Fail"

df["Grade"] = df["Percentage"].apply(grade)

def result(p):
    if p>=40:
        return "Pass"
    else:
        return "Fail"
df["Result"] = df["Percentage"].apply(result)

def status(a):
    if a>=90:
        return "Regular"
    else:
        return "Irregular"

df["Status"] = df["Attendance"].apply(status)
print(df)

print("\nHighest Total : ",df["Total"].max())
print("Lowest Total :",df["Total"].min())
print("Average Total :",round(df["Total"].mean(),2))

topper =  df.loc[df["Total"].idxmax()]
print("\nTopper")
print(topper)

lowest = df.loc[df["Total"].idxmin()]
print("\nLowest Scorer")
print(lowest)

print("\nGrade count")
print(df["Grade"].value_counts())

print("\nPass count")
print(df["Result"].value_counts())

print("\nAttendance")
print(df["Status"].value_counts())


df.to_csv("Student_Report.csv",index=False)
print("File saved successfully!")

subject_average = df[["Maths","Science","English","Computer"]].mean()

# ==========================
# Data Visualization
# ==========================

#Subject wise average 
plt.figure(figsize=(7,5))
plt.bar(subject_average.index,
        subject_average.values,
        color=["red","blue","green","orange"],
        )
plt.title("Average Marks of Each Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()

#Percentage Distribution
plt.figure(figsize=(7,5))
plt.hist(
    df["Percentage"],
    bins=[50,60,70,80,90,100],
    color="skyblue",
    edgecolor="black"
)
plt.xticks([50,60,70,80,90,100])
plt.title("Percentage Distribution")
plt.xlabel("Percentage")
plt.ylabel("No. of Students")
plt.show()

#Grade Distribution
plt.figure(figsize=(6,6))
grade_count = df["Grade"].value_counts()
plt.pie(
    grade_count,
    labels=grade_count.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["gold","skyblue","lightgreen","tomato"],
    explode=[0.05,0,0,0]
)
plt.title("Grade Distribution")
plt.show()

#Relation Between Attendance and Percentage
plt.figure(figsize=(7,5))
sns.scatterplot(
    x="Attendance",
    y="Percentage",
    data=df,
    hue="Grade",
    s=120
)
plt.title("Attendance vs Percentage")
plt.show()

#student wise Percentage
plt.figure(figsize=(8,5))
sns.lineplot(
    x="Name",
    y="Percentage",
    data=df,
    marker="o"
)
plt.title("Student Percentage")
plt.show()

#Box plot
plt.figure(figsize=(7,5))
sns.boxplot(
    data=df[["Maths","Science","English","Computer"]]
)
plt.title("Subject Marks Distribution")
plt.show()

plt.figure(figsize=(6,5))

sns.heatmap(
    df[["Maths","Science","English","Computer"]].corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.show()