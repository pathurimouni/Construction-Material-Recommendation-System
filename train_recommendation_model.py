
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv("material_recommendation_dataset.csv")

# Encode categorical variables
le_project = LabelEncoder()
le_quality = LabelEncoder()
le_material = LabelEncoder()

df["Project_Size"] = le_project.fit_transform(df["Project_Size"])
df["Required_Quality"] = le_quality.fit_transform(df["Required_Quality"])
df["Recommended_Material"] = le_material.fit_transform(df["Recommended_Material"])

# Features and target
X = df.drop("Recommended_Material", axis=1)
y = df["Recommended_Material"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and encoders
joblib.dump(model, "material_model.pkl")
joblib.dump(le_project, "le_project.pkl")
joblib.dump(le_quality, "le_quality.pkl")
joblib.dump(le_material, "le_material.pkl")

print("Model and encoders saved successfully.")
