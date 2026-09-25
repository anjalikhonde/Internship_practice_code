import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class selfdrivingcar:

    def __init__(self):

        self.distances=[50,40,30,20,10]
        self.speeds=[80,75,70,60,40]

    def sensors_data(self):

        print("Sensers Information")
        print("======================")

        for i in range(len(self.distances)):
            print("Distance =",self.distances[i],
                  "Speed =" ,self.speeds[i])
            
    def driving_decision(self):

        print("\nDriving Decisions")
        print("========================")

        for i in range(len(self.distances)):

            distance = self.distances[i]
            
            if distance >30:
                print("move forward")

            if distance > 15:
                print("Slow Down")

            else:
                print("Emergency Brake")

    def numpy_analysis(self):
        distance_array = np.array(self.distances)

        print("\nNumpy Analysis")
        print("========================")
        print("Average Distance =", np.mean(distance_array))
        print("Maximum Distance =", np.max(distance_array))          
        print("Minimum Distance =", np.min(distance_array))

    def panadas_report(self):
        
        data={
            "distance":self.distances,
            "speed":self.speeds
        }

        df = pd.DataFrame(data)

        print("Car senser report")
        print(df)

        return df

    def visualization(self,df):

        plt.figure(figsize=(8,5))

        plt.plot(
                df["distance"],
                df["speed"],
                marker="o")
            
        plt.title("Car Handeling Analysis")

        plt.xlabel("Distance")

        plt.ylabel("Speed")

        #plt.show()
        plt.savefig("matplotlibfig2.png")




s1=selfdrivingcar()
s1.sensors_data()
s1.driving_decision()
s1.numpy_analysis()
df=s1.panadas_report()
s1.visualization(df)