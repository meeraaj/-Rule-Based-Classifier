# ---------------------------------------------
# 🏦 Loan Approval Rule-Based Classifier
# ---------------------------------------------
# This program predicts whether a loan application
# will be Approved or Rejected using simple rules
# based on Income, Credit Score, and Employment Status.
#
# Steps:
# 1. Load dataset from CSV using pandas
# 2. Define a rule-based classifier (if-else logic)
# 3. Apply classifier to dataset to generate predictions
# 4. Evaluate performance with accuracy & confusion matrix
# 5. Visualize confusion matrix using matplotlib
# 6. Allow user to input values for real-time prediction
# ---------------------------------------------

import pandas as pd                  # For dataset handling
import matplotlib.pyplot as plt      # For plotting confusion matrix
from sklearn.metrics import accuracy_score, confusion_matrix  # For evaluation metrics

# -----------------------------
# Step 1: Load Dataset
# -----------------------------
df = pd.read_csv("dataset.csv")   # Load dataset from CSV into a DataFrame
print("📊 Dataset Loaded:")
print(df.head())                  # Show first 5 rows for verification

# -----------------------------
# Step 2: Define Rule-Based Classifier
# -----------------------------
def rule_based_classifier(income, credit, employed):
    """
    Rule-based classifier:
    - If Income is High AND Credit is Good → Approved
    - If Credit is Good AND Employed is Yes → Approved
    - If Income is High AND Employed is Yes → Approved
    - Else → Rejected
    """
    if income == "High" and credit == "Good":
        return "Approved"
    elif credit == "Good" and employed == "Yes":
        return "Approved"
    elif income == "High" and employed == "Yes":
        return "Approved"
    else:
        return "Rejected"

# -----------------------------
# Step 3: Apply Classifier to Dataset
# -----------------------------
# For each row, run the rule-based function and store result in new column 'Predicted'
df["Predicted"] = df.apply(
    lambda row: rule_based_classifier(row["Income"], row["Credit"], row["Employed"]),
    axis=1,   # axis=1 means apply row-wise
)

# -----------------------------
# Step 4: Evaluate Performance
# -----------------------------
# Accuracy = (Correct Predictions / Total Predictions)
accuracy = accuracy_score(df["Approved"], df["Predicted"])
print(f"\n✅ Model Accuracy: {accuracy * 100:.2f}%")

# Confusion Matrix: shows how many were correctly/incorrectly classified
cm = confusion_matrix(df["Approved"], df["Predicted"], labels=["Approved", "Rejected"])

# -----------------------------
# Step 5: Visualize Confusion Matrix
# -----------------------------
fig, ax = plt.subplots()                 # Create a figure and axis
cax = ax.matshow(cm, cmap="Blues")       # Show confusion matrix as colored grid
plt.title("Confusion Matrix", pad=20)    # Add title
fig.colorbar(cax)                        # Add color scale bar

# Set axis labels
ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(["Approved", "Rejected"])
ax.set_yticklabels(["Approved", "Rejected"])
plt.xlabel("Predicted")   # X-axis = predicted values
plt.ylabel("Actual")      # Y-axis = actual values

# Add numbers inside the matrix (e.g., TP, FP, TN, FN counts)
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        ax.text(j, i, str(cm[i, j]), va='center', ha='center', color='black')


plt.savefig("confusion_matrix.png")
print("📊 Confusion Matrix saved as confusion_matrix.png")


# -----------------------------
# Step 6: Real-Time User Input
# -----------------------------
print("\n🔮 Real-Time Loan Approval Prediction 🔮")        

income = input("Applicant Income (High/Low): ").capitalize()    # Ask user for income level  
credit = input("Credit Score (Good/Poor): ").capitalize()       # Ask user for credit score
employed = input("Employed? (Yes/No): ").capitalize()           # Ask user for employment status


# Run classifier on user input
prediction = rule_based_classifier(income, credit, employed)
print(f"👉 Loan Decision: {prediction}")   # Display final result
