# Titanic Random Forest Model Recommendation

## Objective
Predict Titanic passenger survival (`survived`) using pclass, sex_male, age, sibsp, parch, and fare from the supplied Titanic dataset.

## Model choice
A Random Forest is a suitable baseline because it combines many decision trees, uses bootstrap samples and random feature subsets, and can reduce the variance of an individual tree. It can model nonlinear patterns without requiring feature scaling.

## Evaluation
- Final test accuracy: 0.730
- Final test ROC-AUC: 0.831
- Final model OOB score: 0.709
- Stability across 25 bootstrap training samples: consult the Task 04 mean and standard deviation table before making a claim.

## Key findings
Use the Task 07 permutation-importance ranking and Task 08 PDPs to state two patterns supported by the actual plots. Do not claim that a feature causes survival.

## Risks and limitations
The dataset is historical and may not represent other populations. Missing-value imputation can affect results. Correlation is not causation, and importance rankings can be biased or unstable. A single train/test split has sampling uncertainty, and predictions raise fairness and ethical interpretation concerns.

## Recommendation
Use this Random Forest as a baseline only. Next, run cross-validation on the training set and compare it with logistic regression or gradient boosting; assess probability calibration before using predicted probabilities for decisions.
