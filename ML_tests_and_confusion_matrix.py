#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
    precision_score,
    recall_score,
    accuracy_score,
    roc_curve,
    auc,
)
from sklearn.model_selection import learning_curve, train_test_split


df = pd.read_csv("final_hmm_model_results.csv")

# E-value ve Label'ı al
X = df["E-value"].astype(float).values
y = df["Label"].astype(int).values

# E-value and labels
data = list(zip(X, y))

# Confusion matrix 
def get_cm(data, th):
    preds = []
    labels = []
    for val, label in data:
        pred = 1 if val < th else 0
        preds.append(pred)
        labels.append(label)
    cm = confusion_matrix(labels, preds)
    return cm, preds, labels

# Threshold optimization
best_th = None
best_f1 = -1
scores = []

th_values = np.arange(min(X), max(X), 0.01)
for th in th_values:
    _, preds, labels = get_cm(data, th)
    f1 = f1_score(labels, preds)
    scores.append((th, f1))
    if f1 > best_f1:
        best_f1 = f1
        best_th = th

# best treshold
cm, preds, labels = get_cm(data, best_th)
print(f"Best Threshold: {best_th:.4f}")
print(f"F1 Score: {best_f1:.4f}")
print(f"Precision: {precision_score(labels, preds):.4f}")
print(f"Recall: {recall_score(labels, preds):.4f}")
print(f"Accuracy: {accuracy_score(labels, preds):.4f}")
print(f"\nConfusion Matrix:\n{cm}")

# Confusion matrix plot
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap="Greens")
plt.title(f"Confusion Matrix (Threshold = {best_th:.4f})")
plt.show()

# F1 Score vs Threshold graph
ths = [t for t, _ in scores]
f1s = [s for _, s in scores]
plt.plot(ths, f1s, label="F1 Score")
plt.axvline(x=best_th, color='r', linestyle='--', label=f"Best Threshold: {best_th:.4f}")
plt.xlabel("Threshold")
plt.ylabel("F1 Score")
plt.title("F1 Score vs Threshold")
plt.legend()
plt.grid(True)
plt.show()

#  Learning Curve
X_reshaped = X.reshape(-1, 1)
model = LogisticRegression()

train_sizes, train_scores, test_scores = learning_curve(
    model, X_reshaped, y, cv=5, scoring='accuracy', train_sizes=np.linspace(0.1, 1.0, 10))

train_mean = train_scores.mean(axis=1)
test_mean = test_scores.mean(axis=1)

plt.figure(figsize=(8, 5))
plt.plot(train_sizes, train_mean, 'o-', label='Training score')
plt.plot(train_sizes, test_mean, 'o-', label='Cross-validation score')
plt.xlabel('Training Size')
plt.ylabel('Accuracy')
plt.title('Learning Curve')
plt.legend(loc='best')
plt.grid(True)
plt.tight_layout()
plt.show()

# ROC Curve
X_train, X_test, y_train, y_test = train_test_split(X_reshaped, y, test_size=0.3, random_state=42)
model.fit(X_train, y_train)
y_scores = model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_scores)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC)')
plt.legend(loc="lower right")
plt.grid(True)
plt.show()
