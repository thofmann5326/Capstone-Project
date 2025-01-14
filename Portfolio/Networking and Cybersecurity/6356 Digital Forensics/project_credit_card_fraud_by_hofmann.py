# -*- coding: utf-8 -*-
"""Project Credit Card Fraud by Hofmann

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TRG2iJeOu-vXPBI_UXeqa7oTCaOmvH5S

# Analysis of Three Machine Learning Algorithms on Credit Card Fraud.
By Trevor Hofmann

## Abstract

This study investigates the performance of various machine learning algorithms for credit card fraud detection in a dataset containing transactions made by European cardholders in September 2013. The dataset is imbalanced, with more legitimate transactions than fraudulent ones. There are three research questions to guide the inquiry:

**Question:** What machine learning algorithms perform better at predicting credit card fraud?

**Answer:** Logistic Regression

**Question:** What three variables contribute the most to the algorithm’s performance?

**Answer:** Logistic Regression model: 'V14', 'V4', 'V12'

**Question:** What is the relationship to the dependent variable (Class) of the three most important independent variables? Positive or negative?  

**Answer:** Relationship between the top three variables and Class for Logistic Regression:
V14: Negative relationship with Class
V4: Positive relationship with Class
V12: Negative relationship with Class

To answer these questions we implemented machine learning model and compaired their performance.

## Introduction

Credit card fraud is a significant concern for financial institutions and cardholders all over the world. Detecting fraudulent transactions quickly is extremly important to mitigate financial losses. Machine learning tools have shown to be effective at identifying fraudulent transactions by leveraging patterns and anomalies in the data.

## Literature Review

Recent research in credit card fraud detection (CCFD) emphasizes the effectiveness of machine learning (ML) and deep learning techniques at identifying fraudulent transactions.  For instance, works by Fu et al. (2016) and Zorion, et al. (2023) achieve high accuracy in credit card fraud detection using deep learning architectures, while acknowledging the challenges of imbalanced datasets common in fraud scenarios.  Additionally, research by Bodepudi (2021) explores unsupervised anomaly detection methods to identify outliers which might represent fraudulent activity.  These studies highlight the opportunities for researchers to continuously develop and refine ML algorithms to combat increasingly sophisticated fraud attempts.

## Research Questions

1.   What machine learning algorithms perform better at predicting credit card fraud?
2.   What three variables contribute the most to the algorithm’s performance?
3.   What is the relationship to the dependent variable (Class) of the three most important independent variables? Positive or negative?

## Methodology

**Dataset.** The dataset contains a subset of transactions made by European cardholders duringSeptember 2013. The original, full-sized dataset was collected during a research collaboration of the Worldline and the Machine Learning Group (http://mlg.ulb.ac.be) and ULB (Université Libre de Bruxelles) on big data mining and fraud detection. The full-sized dataset (N = 284,807) and list of researchers involved is available at https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud. A smaller dataset more amenable to working in Google Colab (N = 10,000) was compiled by Sean Humpherys and includes all the cases of fraud (n = 492) present in the original dataset and a random sampling of non-fraud cases (n = 9508). The dataset is imbalanced with only 4.92% of transactions being fraudlent. The smaller dataset is available at https://raw.githubusercontent.com/sean-humpherys/randomfilestorage/main/cc_transactions_10000.csv <br><br>
**Dependent Variable.** The dependent variable in this analysis is the Class variable, representing the classification of transactions as either fraudulent or non-fraudulent. It is a binary variable with the following meanings:

    0: Non-fraudulent transaction
    1: Fraudulent transaction

**Independent Variables.**The independent variables used to predict the dependent variable are as follows:
1.   Time: Number of seconds between the current transaction and the first transaction in the dataset.
2.   V1-V28: Principal Component Analysis (PCA) transformed features, representing anonymized numerical variables derived from the original transaction data.
3.   Amount: The monetary amount of the credit card transaction in Euros.

**Algorithms.** Three algorithms will be utilized to perform the analysis:
1.   Logistic Regression: A simple yet powerful linear model commonly used for binary classification tasks. It estimates the probability that a given instance belongs to a particular class.
2.   Random Forest: A versatile ensemble learning method that constructs a multitude of decision trees during training and outputs the class that is the mode of the classes (classification) of the individual trees.
3.   Gradient Boosting: Another ensemble learning technique that builds multiple models sequentially. Each model corrects errors made by the previous one, leading to better predictive performance.

Performance Metrics:

*   Confusion Matrix: Provides a tabular summary of the performance of a classification model, displaying the number of true positives, true negatives, false positives, and false negatives.
*   Area Under the ROC Curve (AUC ROC): Measures the area under the receiver operating characteristic curve, which plots the true positive rate against the false positive rate.
*   Precision-Recall Curve: Illustrates the trade-off between precision and recall for different threshold values, providing insights into the model's performance across various decision boundaries.<br><br>

## Results

### Prepair the code
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import confusion_matrix, roc_auc_score, precision_recall_curve, auc, roc_curve
import matplotlib.pyplot as plt

"""Load data in"""

# Load the credit card data
df = pd.read_csv('https://raw.githubusercontent.com/sean-humpherys/randomfilestorage/main/cc_transactions_10000.csv')

# Display summary statistics
print("Summary Statistics:")
print(df.describe())

"""### **Descriptive Statistics.**"""

# Count of fraudulent records
fraudulent_records = df[df['Class'] == 1]
num_fraudulent_records = fraudulent_records.shape[0]

# Count of legitimate records
legitimate_records = df[df['Class'] == 0]
num_legitimate_records = legitimate_records.shape[0]

# Check for missing values
missing_values = df.isnull().sum().any()

# Check if Class is coded as only zero and one
unique_classes = df['Class'].unique()
class_coded_correctly = (len(unique_classes) == 2) and (0 in unique_classes) and (1 in unique_classes)

print("Number of fraudulent records:", num_fraudulent_records)
print("Number of legitimate records:", num_legitimate_records)
print("Are there any missing values?", "Yes" if missing_values else "No")
print("Is Class coded as only zero and one?", "Yes" if class_coded_correctly else "No")

"""###Define dependent and independent variables"""

X = df.drop('Class', axis=1)
y = df['Class']

"""### Split data into train and test sets"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""### Standardize independent variables"""

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

"""### Model implementation

Logistic Regression
"""

log_reg = LogisticRegression()
log_reg.fit(X_train_scaled, y_train)

"""Random Forest"""

random_forest = RandomForestClassifier()
random_forest.fit(X_train_scaled, y_train)

"""Gradient Boosting"""

gradient_boosting = GradientBoostingClassifier()
gradient_boosting.fit(X_train_scaled, y_train)

"""### Model Performance

Confusion Matrix
"""

def print_confusion_matrix(model, model_name):
    y_pred = model.predict(X_test_scaled)
    conf_matrix = confusion_matrix(y_test, y_pred)
    print(f"Confusion Matrix ({model_name}):")
    print(conf_matrix)
    print()

print_confusion_matrix(log_reg, "Logistic Regression")
print_confusion_matrix(random_forest, "Random Forest")
print_confusion_matrix(gradient_boosting, "Gradient Boosting")

"""AUC ROC"""

def print_auc_roc(model, model_name):
    y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
    auc_roc = roc_auc_score(y_test, y_pred_proba)
    print(f"AUC ROC ({model_name}): {auc_roc:.4f}")

print_auc_roc(log_reg, "Logistic Regression")
print_auc_roc(random_forest, "Random Forest")
print_auc_roc(gradient_boosting, "Gradient Boosting")

"""Precision-Recall Curve"""

def plot_precision_recall_curve(model, model_name):
    y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
    precision, recall, _ = precision_recall_curve(y_test, y_pred_proba)
    pr_auc = auc(recall, precision)
    plt.plot(recall, precision, label=f'{model_name} (AUC = {pr_auc:.4f})')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title(f'Precision-Recall Curve ({model_name})')
    plt.legend()
    plt.show()

plot_precision_recall_curve(log_reg, "Logistic Regression")
plot_precision_recall_curve(random_forest, "Random Forest")
plot_precision_recall_curve(gradient_boosting, "Gradient Boosting")

"""### Results for Research Question 1
What machine learning algorithms perform better at predicting credit card fraud? Logistics Regression

We begain by setting Class as the dependent variable, spliting the data for training and test, and Standardize independent variables
"""

X = df.drop('Class', axis=1)
y = df['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

"""We then ran all three algorithms against the data."""

#LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(X_train_scaled, y_train)
#Forest
random_forest = RandomForestClassifier()
random_forest.fit(X_train_scaled, y_train)
#Gradient Boosting
gradient_boosting = GradientBoostingClassifier()
gradient_boosting.fit(X_train_scaled, y_train)

"""**Performance Metrics**. [Evaluate the performance metrics of your models. Code a confusion matrix. Code plots of AUC ROC and Precision-Recall curve. ]"""

print_confusion_matrix(log_reg, "Logistic Regression")
print_confusion_matrix(random_forest, "Random Forest")
print_confusion_matrix(gradient_boosting, "Gradient Boosting")

"""The Confusion Matrix shows Gradient Boosting and Logistic Regression performed equally well."""

print_auc_roc(log_reg, "Logistic Regression")
print_auc_roc(random_forest, "Random Forest")
print_auc_roc(gradient_boosting, "Gradient Boosting")

"""The AUC shows the Logistic Regression had the best performance at 0.9924 with Gradient Boosting jus behind it at 0.9911."""

plot_precision_recall_curve(log_reg, "Logistic Regression")
plot_precision_recall_curve(random_forest, "Random Forest")
plot_precision_recall_curve(gradient_boosting, "Gradient Boosting")

"""The Precision-Recall Curve show Random Forest performed best with Logistic Regression just behind it.

The overall interpretation is that the Logistics Regression Performs best overall. Gradient Boosting and Logistic Regression tied once then place 2nd and 3rd respectively. On the final performance review Gradient Boosting placed last and Logistic Regression placed 2nd.
Logistic Regression on average performs better.

### Results for Research Question 2
What three variables contribute the most to the algorithm’s performance?

We ran code for each algorithm to see what three variables perform best.

For Logistic Regression:
"""

# Get absolute coefficients
abs_coefficients = abs(log_reg.coef_[0])

# Get indices of top three coefficients
top_three_indices_log_reg = abs_coefficients.argsort()[-3:][::-1]

# Get names of top three variables
top_three_variables_log_reg = X.columns[top_three_indices_log_reg]
print("Top three variables contributing the most to Logistic Regression model:")
print(top_three_variables_log_reg)

"""For Random Forest:"""

# Get feature importances
feature_importances_rf = random_forest.feature_importances_

# Get indices of top three feature importances
top_three_indices_rf = feature_importances_rf.argsort()[-3:][::-1]

# Get names of top three variables
top_three_variables_rf = X.columns[top_three_indices_rf]
print("Top three variables contributing the most to Random Forest model:")
print(top_three_variables_rf)

"""For Gradient Boosting"""

# Get feature importances
feature_importances_gb = gradient_boosting.feature_importances_

# Get indices of top three feature importances
top_three_indices_gb = feature_importances_gb.argsort()[-3:][::-1]

# Get names of top three variables
top_three_variables_gb = X.columns[top_three_indices_gb]
print("Top three variables contributing the most to Gradient Boosting model:")
print(top_three_variables_gb)

"""The three variables contribute the most to the algorithm’s performance is as follows:

Top three variables contributing the most to Logistic Regression model:
'V14', 'V4', 'V12'

Top three variables contributing the most to Gradient Boosting model:
'V14', 'V17', 'V10'

Top three variables contributing the most to Gradient Boosting model:
'V14', 'V17', 'V10'

### Results for Research Question 3
What is the relationship to the dependent variable (Class) of the three most important independent variables? Positive or negative?

For Logistic Regression:
"""

# Get coefficients
coefficients_log_reg = log_reg.coef_[0]

# Get indices of top three coefficients
top_three_indices_log_reg = abs(coefficients_log_reg).argsort()[-3:][::-1]

# Print top three features and their relationships with Class for Logistic Regression
print("\nRelationship between the top three variables and Class for Logistic Regression:")
for i in top_three_indices_log_reg:
    variable_name = X.columns[i]
    variable_values_fraud = X_test_scaled[y_test == 1, i]
    variable_values_non_fraud = X_test_scaled[y_test == 0, i]
    mean_fraud = variable_values_fraud.mean()
    mean_non_fraud = variable_values_non_fraud.mean()
    if mean_fraud > mean_non_fraud:
        print(f"{variable_name}: Positive relationship with Class")
    elif mean_fraud < mean_non_fraud:
        print(f"{variable_name}: Negative relationship with Class")
    else:
        print(f"{variable_name}: No clear relationship with Class")

"""For Random Forest:"""

# Get feature importances
feature_importances_rf = random_forest.feature_importances_

# Get indices of top three feature importances
top_three_indices_rf = feature_importances_rf.argsort()[-3:][::-1]

# Print top three features and their relationships with Class for Random Forest
print("\nRelationship between the top three variables and Class for Random Forest:")
for i in top_three_indices_rf:
    variable_name = X.columns[i]
    variable_values_fraud = X_test_scaled[y_test == 1, i]
    variable_values_non_fraud = X_test_scaled[y_test == 0, i]
    mean_fraud = variable_values_fraud.mean()
    mean_non_fraud = variable_values_non_fraud.mean()
    if mean_fraud > mean_non_fraud:
        print(f"{variable_name}: Positive relationship with Class")
    elif mean_fraud < mean_non_fraud:
        print(f"{variable_name}: Negative relationship with Class")
    else:
        print(f"{variable_name}: No clear relationship with Class")

"""For Gradient Boosting"""

# Get feature importances
feature_importances_gb = gradient_boosting.feature_importances_

# Get indices of top three feature importances
top_three_indices_gb = feature_importances_gb.argsort()[-3:][::-1]

# Print top three features and their relationships with Class for Gradient Boosting
print("\nRelationship between the top three variables and Class for Gradient Boosting:")
for i in top_three_indices_gb:
    variable_name = X.columns[i]
    variable_values_fraud = X_test_scaled[y_test == 1, i]
    variable_values_non_fraud = X_test_scaled[y_test == 0, i]
    mean_fraud = variable_values_fraud.mean()
    mean_non_fraud = variable_values_non_fraud.mean()
    if mean_fraud > mean_non_fraud:
        print(f"{variable_name}: Positive relationship with Class")
    elif mean_fraud < mean_non_fraud:
        print(f"{variable_name}: Negative relationship with Class")
    else:
        print(f"{variable_name}: No clear relationship with Class")

"""## Conclusion

We where able to answer all there questions as follows:

**Question:** What machine learning algorithms perform better at predicting credit card fraud?

**Answer:** Logistic Regression

**Question:** What three variables contribute the most to the algorithm’s performance?

**Answer:** Logistic Regression model: 'V14', 'V4', 'V12'

**Question:** What is the relationship to the dependent variable (Class) of the three most important independent variables? Positive or negative?  

**Answer:** Relationship between the top three variables and Class for Logistic Regression:
V14: Negative relationship with Class
V4: Positive relationship with Class
V12: Negative relationship with Class

## References

<p>Bodepudi, H. (2021) Credit Card Fraud Detection Using Unsupervised Machine Learning Algorithms. International Journal of Computer Trend and Technology. 69 (9) https://www.ijcttjournal.org/2021/Volume-69%20Issue-8/IJCTT-V69I8P101.pdf</p>
<p>Fu, K., Cheng, D., Tu, Y., Zhang, L. (2016). Credit Card Fraud Detection Using Convolutional Neural Networks. In: Hirose, A., Ozawa, S., Doya, K., Ikeda, K., Lee, M., Liu, D. (eds) Neural Information Processing. ICONIP 2016. Lecture Notes in Computer Science(), vol 9949. Springer, Cham. https://doi.org/10.1007/978-3-319-46675-0_531</p>
<p>Zorion, P. K., Sachan, L. , Chhabra, R.,  Pandey, V., Fatima, H., (2023) Credit Card Financial Fraud Detection Using Deep Learning. Available at SSRN: https://ssrn.com/abstract=4629093 or http://dx.doi.org/10.2139/ssrn.4629093</p>
"""