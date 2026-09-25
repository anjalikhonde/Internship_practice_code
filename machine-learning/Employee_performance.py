import numpy as np
import pandas as pd
import statistics
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
#oop concepts

class EmployeeAnalysis:

    def __init__(self):

        self.name = ["Pravin","Amit","Rahul","Neha","Pooja","karan"]

        self.scores = [85,90,78,95,88,90]

    def display_data(self):

        print("===========================================")
        print("*******Employee Performance Report******")
        print("===========================================")

        for i in range(len(self.name)):
            print(self.name[i], ":" ,self.scores[i])
    
    def calculate_statistics(self):

        mean_score = statistics.mean(self.scores)

        median_score = statistics.median(self.scores)

        mode_score = statistics.mode(self.scores)

        std_dev = statistics.stdev(self.scores)

        print("=============================")
        print("****Statistics Report*****")
        print("============================")

        print("Average Score:",mean_score)
        print("median_score:",median_score)
        print("mode_score:",mode_score)
        print("std_dev:",std_dev)

    def performance_status(self):
        
        print("============================================")
        print("************Performance Status*********")
        print("============================================")

        for i in range(len(self.name)):

            if self.scores[i] >= 90:
                print(self.name[i], "Excellent")

            elif self.scores[i] >=80:
                print(self.name[i], "Good")

            else:
                print(self.name[i], "Needs Improvment")

    def numpy_analysis(self):

        arr = np.array(self.scores)

        print("===================================================")
        print("*****************Numpy Analisis****************")
        print("===================================================")
        #print(arr)
        print("Highest Score:",np.max(arr))
        print("Lowest Score",np.min(arr))
        print("Average score:",np.mean(arr))
        print("Total Score:",np.sum(arr))

    def pandas_report(self):

        data = {
            
            "Employee":self.name,
            "scores": self.scores
        }

        df = pd.DataFrame(data)

        print("=======================================")
        print("**********Pandas DataFrame***********")
        print("=======================================")
        print(df)

        return df
    
    def visulalization(self,df):

        plt.figure(figsize=(8,5))

        plt.bar(df["Employee"], df["scores"])

        plt.title("Employe Performance Analysis")

        plt.xlabel("Employee Name")

        plt.ylabel("Performance Score")

        plt.savefig("matplotlibfig1.png")
        #plt.show()
        
    #seaborn

        data = {
            
            "Employee":self.name,
            "scores": self.scores
        }

        df = pd.DataFrame(data)

    sns.barplot(x="Employee",y="scores",data=df)

    plt.title("Sales Analysis")

    plt.savefig("sebornchart.png")
            
        

            


e1=EmployeeAnalysis()
e1.display_data()
e1.calculate_statistics()
e1.performance_status()
e1.numpy_analysis()
dataframe = e1.pandas_report()
e1.visulalization(dataframe)