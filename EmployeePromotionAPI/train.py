import pandas as pd
import joblib

from sklearn.tree import DecisionTreeClassifier

# Read Dataset
df = pd.read_csv('employee_data.csv')

# Input Features
X = df[['Experience', 'Performance', 'Training']]

# Output
y = df['Promotion']

# Train Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Save Model
joblib.dump(model, 'promotion_model.pkl')

print("Promotion Model Created Successfully")