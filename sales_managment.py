import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

#OOP concepts

class Employee:
    def __init__(self,name,sales):
        self.name=name
        self.sales=sales

    def bonus(self):
        if self.sales >= 80000:
            return 10000
        else:
            return 5000
    
    def display(self):
        print("Employee Name:",self.name)
        print("Sales:",self.sales)
        print("Bonus:",self.bonus())
        print("-----------------------------------")
    
#craete objects
emp1 = Employee("Anjali",50000)
emp2 = Employee("Amol",70000)
emp3 = Employee("Riya",65000)
emp4 = Employee("Dipika",90000)
emp5 = Employee("Rahul",85000)

employees = [emp1,emp2,emp3,emp4,emp5]

#Loop

for emp in employees:
    emp.display()

#string example

comapny = "Google"

print("Comapny Name :",comapny.upper())

#numpy

sales_array= np.array([50000,70000,65000,90000,85000])

print("\nTotal Sales :",np.sum(sales_array))
print("\nAverage Sales :",np.mean(sales_array))
print("\nHighest salary :",np.max(sales_array))
print("\nLowest salary :",np.min(sales_array))

#pandas

data={
    "Employee":["Anjali","Amol","Riya","Dipika","Rahul"],
    "sales":[50000,70000,65000,90000,85000]
}
df = pd.DataFrame(data)

print("\nEmployee Data")
print(df)

#matplotlib

plt.figure(figsize=(8,5))

plt.plot(df["Employee"],df["sales"])

plt.title("Employee sales Report")

plt.xlabel("Employee")

plt.ylabel("Sales")

plt.savefig("matplotlibfig.png")

#seaborn

sns.barplot(x="Employee",y="sales",data=df)

plt.title("Sales Analysis")

plt.savefig("sebornchart.png")
