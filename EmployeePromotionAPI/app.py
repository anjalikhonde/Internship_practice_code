from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load Model
model = joblib.load("promotion_model.pkl")

@app.route("/")
def home():
    return "Employee Promotion Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    experience = data["Experience"]
    performance = data["Performance"]
    training = data["Training"]

    # FIXED: Added double brackets [[...]] to make it a 2D array for the model
    prediction = model.predict([[experience, performance, training]])

    # FIXED: Handled comparison safely directly or via prediction[0]
    if prediction[0] == 1:
        result = "Promotion Eligible"
    else:
        result = "Promotion Not Eligible"

    # FIXED: Corrected 'retrun' typo to 'return'
    return jsonify({
        "Experience": experience,
        "Performance": performance,
        "Training": training,
        "prediction": result
    })

if __name__ == "__main__":
    app.run(debug=True)
