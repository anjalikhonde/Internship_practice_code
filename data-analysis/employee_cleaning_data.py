import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# 1. Create Database
data = {
    "Name": ["Pravin", "Amit", "Rahul", "Neha", "Amit"],
    "Age": [25, 30, None, 28, 30],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Experience": [2, 5, 4, None, 5],
    "Salary": [50000, 70000, 65000, 80000, 70000]
}

# Create dataframe
df = pd.DataFrame(data)
print("--- Initial Dataframe ---")
print(df)


###########################################################################

# 2. Remove Duplicate Rows

df = df.drop_duplicates()
print("\n--- After Removing Duplicates ---")
print(df)

############################################################################

# 3. Handle Missing Values

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Experience"] = df["Experience"].fillna(df["Experience"].mean())

print("\n--- After Handling Missing Values ---")
print(df) 

#############################################################################

# 4. Encoding Categorical Variables

encoder = LabelEncoder()
df["Department"] = encoder.fit_transform(df["Department"])

print("\n--- After Encoding ---")
print(df)

###############################################################################

# 5. Feature Scaling

scalar = MinMaxScaler()

# FIX: Grouped column strings inside a single Python list
columns_to_scale = ["Age", "Experience", "Salary"]
df[columns_to_scale] = scalar.fit_transform(df[columns_to_scale])
    
print("\n--- After Feature Scaling Data ---")
print(df)


# 6. Feature and Target Separation

# FIX: Unified formatting to standard nested bracket syntax
x = df[["Age", "Experience", "Salary"]]
y = df["Salary"] # FIX: Match capitalization with the 'Salary' key string

#########################################################################################

# 7. Train Test Split

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.20,
    random_state=42
)
    
print("\n--- Training Data (X) ---")
print(x_train)

print("\n--- Testing Data (X) ---")
print(x_test)

###################################################################################

print("\nData Preprocessing completed successfully!")
