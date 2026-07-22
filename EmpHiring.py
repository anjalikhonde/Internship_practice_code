import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("=" * 60)
print("       AI EMPLOYEE HIRING PREDICTION SYSTEM")
print("=" * 60)

# -------------------------------------------------------------
# Employee Dataset
# -------------------------------------------------------------

data = {
    'Experience': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Python': [40, 50, 60, 70, 80, 85, 90, 95, 98, 100],
    'SQL': [35, 45, 55, 65, 75, 85, 90, 95, 98, 100],
    'MachineLearning': [20, 30, 40, 50, 60, 70, 80, 90, 95, 100],
    'Communication': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    'Attendance': [75, 78, 80, 82, 85, 88, 90, 92, 95, 98],
    'Selected': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

print("\nEmployee Database\n")
print(df)

# -------------------------------------------------------------
# Statistics
# -------------------------------------------------------------

print("\nAverage Python Skill :", df['Python'].mean())
print("Average Attendance :", df['Attendance'].mean())
print("Highest Experience :", df['Experience'].max())
print("Lowest Experience :", df['Experience'].min())

# -------------------------------------------------------------
# Graph
# -------------------------------------------------------------

plt.figure(figsize=(8, 4))
plt.plot(df['Experience'], df['Python'], marker='o')

plt.title("Experience vs Python Skill")
plt.xlabel("Experience")
plt.ylabel("Python Skill")
plt.grid()

plt.savefig("ABC.png")
plt.show(block=False)
plt.pause(3)
plt.close()

# -------------------------------------------------------------
# Machine Learning
# -------------------------------------------------------------

x = df.drop('Selected', axis=1)
y = df['Selected']

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(random_state=42)

model.fit(x_train, y_train)

prediction = model.predict(x_test)

accuracy = accuracy_score(y_test, prediction)

print("\nModel Accuracy : {:.2f}%".format(accuracy * 100))

# -------------------------------------------------------------
# User Input
# -------------------------------------------------------------

print("\nEnter Candidate Details\n")

experience = float(input("Experience (Years): "))
python_skill = float(input("Python Skill: "))
sql = float(input("SQL Skill: "))
machine_learning = float(input("Machine Learning Skill: "))
communication = float(input("Communication Skill: "))
attendance = float(input("Attendance (%): "))

candidate = pd.DataFrame({
    "Experience": [experience],
    "Python": [python_skill],
    "SQL": [sql],
    "MachineLearning": [machine_learning],
    "Communication": [communication],
    "Attendance": [attendance]
})

result = model.predict(candidate)

# -------------------------------------------------------------
# Prediction
# -------------------------------------------------------------

result = model.predict(candidate)

print("\nPrediction Result")

if result[0] == 1:
    print("Candidate Selected")
else:
    print("Candidate Not Selected")

print("\nThank you for using AI Employee Hiring Prediction System.")