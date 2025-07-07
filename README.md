
 Predicting Babies' Survival Rate Using Random Forest
This project aims to predict the survival of newborn babies within the first 28 days of life using clinical and maternal data. The model is built using the Random Forest Classifier, chosen for its robustness and interpretability in classification tasks.

 Problem Statement
Neonatal mortality remains a significant public health challenge in many parts of the world. Timely identification of at-risk newborns can help healthcare providers intervene earlier. This project develops a predictive model to classify whether a baby is likely to survive or not based on key features such as gestational age, birth weight, APGAR scores, maternal history, and delivery details.

🧠 Machine Learning Approach
Model Used: Random Forest Classifier

Handling Imbalance: SMOTE (Synthetic Minority Over-sampling Technique)

Evaluation Metrics: Accuracy, Recall, Precision, F1-Score

Pipeline: Preprocessing → Oversampling → Training → Evaluation

 Dataset
Source: Hospital-collected neonatal clinical data

Size: 5,766 entries

Target Variable: BABY FINAL DIAGNOSIS (0 = Survived, 1 = Died)

Important Features:

Mother's Age

Gravida & Parity

Gestation Age

Term/Preterm Status

HIV Status

Mode of Delivery

APGAR Scores (1 min & 5 min)

Baby's Sex

Weight

Postnatal Care (6 hrs, 24 hrs)

 Tools and Libraries
Python

Pandas, NumPy, Seaborn, Matplotlib
