# -*- coding: utf-8 -*-
"""CODESOFT_TASK_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12NPybhN6ISgx1i06v95iPHgFOG4D2b_Z
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Step 1: Load the Iris dataset from CSV file
iris_df = pd.read_csv('IRIS.csv')

# Step 2: Split the data into features and target variable
X = iris_df.drop(columns=['species'])  # Features
y = iris_df['species']  # Target variable

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 5: Train a logistic regression model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Step 6: Evaluate the model
y_pred = model.predict(X_test_scaled)

# Print classification report and confusion matrix
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))