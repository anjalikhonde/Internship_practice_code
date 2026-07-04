# =====================================================================
# House Price Prediction
# =====================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('Agg')

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


class HousePricePrediction:

    def __init__(self):

        self.data = {
            "Area": [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000, 3500],
            "Bedrooms": [2, 2, 3, 3, 3, 4, 4, 4, 5, 5],
            "Bathroom": [1, 2, 2, 2, 3, 3, 3, 4, 4, 5],
            "Age": [10, 8, 6, 5, 4, 3, 2, 2, 1, 1],
            "Prices": [45, 52, 65, 75, 85, 95, 110, 125, 140, 170]
        }

    # --------------------------------------------------------------------

    def create_dataframe(self):

        self.df = pd.DataFrame(self.data)

        print("\nOriginal Dataset\n")
        print(self.df)

    # --------------------------------------------------------------------

    def visualize(self):

        plt.figure(figsize=(8, 5))

        sns.scatterplot(
            x="Area",
            y="Prices",
            data=self.df,
            s=100
        )

        plt.title("Area vs House Price")
        plt.xlabel("Area (sq.ft)")
        plt.ylabel("Price (Lakhs)")
        plt.grid(True)

        plt.savefig("house_price_plot.png")
        plt.close()

    # --------------------------------------------------------------------

    def split_data(self):

        x = self.df[["Area", "Bedrooms", "Bathroom", "Age"]]
        y = self.df["Prices"]

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            x,
            y,
            test_size=0.2,
            random_state=42
        )

    # --------------------------------------------------------------------

    def train_model(self):

        self.model = LinearRegression()

        self.model.fit(
            self.x_train,
            self.y_train
        )

        print("\nModel Trained Successfully!")

    # --------------------------------------------------------------------

    def prediction(self):

        self.prediction = self.model.predict(self.x_test)

        print("\nActual Prices")
        print(self.y_test.values)

        print("\nPredicted Prices")
        print(self.prediction)

    # --------------------------------------------------------------------

    def accuracy(self):

        mae = mean_absolute_error(self.y_test, self.prediction)
        mse = mean_squared_error(self.y_test, self.prediction)
        r2 = r2_score(self.y_test, self.prediction)

        print("\n================ MODEL REPORT ================")
        print("Mean Absolute Error :", round(mae, 2))
        print("Mean Squared Error  :", round(mse, 2))
        print("R² Score            :", round(r2, 2))
        print("==============================================")

    # --------------------------------------------------------------------

    def predict_new_house(self):

        print("\n----------- Predict New House -----------")

        Area = int(input("Enter Area: "))
        Bedrooms = int(input("Enter Bedrooms: "))
        Bathroom = int(input("Enter Bathrooms: "))
        Age = int(input("Enter House Age: "))

        new_house = pd.DataFrame({
            "Area": [Area],
            "Bedrooms": [Bedrooms],
            "Bathroom": [Bathroom],
            "Age": [Age]
        })

        result = self.model.predict(new_house)

        print("\nEstimated House Price")
        print("Rs.", round(result[0], 2), "Lakhs")


# =====================================================================
# Main Program
# =====================================================================

obj = HousePricePrediction()

obj.create_dataframe()
obj.visualize()
obj.split_data()
obj.train_model()
obj.prediction()
obj.accuracy()
obj.predict_new_house()