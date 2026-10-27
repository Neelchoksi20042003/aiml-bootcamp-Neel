# Tree-Based Insurance Claim Fraud Detection

**Day 30 — Week 6 Project**  
**Purpose:** Prioritize potentially fraudulent insurance claims for human investigation. The model is decision support, not an automatic fraud verdict.

## Repository contents

- `insurance_fraud_detection.ipynb` — complete analysis and modelling notebook.
- `insurance_claims.csv` — dataset required by the notebook.
- `recommendation.md` — one-page recommendation for the claims team.

## How to run

1. Keep the notebook and CSV in the same folder.
2. Install the required packages in your Python environment:

   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn xgboost shap jupyter
   ```

3. Open `insurance_fraud_detection.ipynb` in Jupyter Notebook or JupyterLab.
4. Restart the kernel and run all cells from top to bottom.

The notebook reads `insurance_claims.csv` using a relative path, so no machine-specific path should be needed.

## Dataset summary

- Records: 8,000 claims
- Target: `is_fraud` (`1` = fraud, `0` = legitimate)
- Fraud cases: 295
- Legitimate cases: 7,705
- Fraud prevalence: **3.6875%**
- Imbalance ratio: approximately **26.12 legitimate claims per fraud claim**
- Missing values: 120 in `age`; 90 in `days_to_report`

## Key evaluation results

The notebook uses a stratified train/validation/test workflow. Model and threshold choices are made before the final test evaluation.

| Final test metric | Result |
|---|---:|
| Average Precision (PR-AUC-style ranking summary) | 0.1227 |
| ROC-AUC | 0.7405 |
| Precision at the selected threshold | 0.1209 |
| Recall at the selected threshold | 0.3729 |
| Brier score | 0.0341 |
| Log loss | 0.1438 |
| Selected threshold (chosen on validation data after calibration) | 0.065 |
| True positives | 22 |
| False positives | 160 |
| False negatives | 37 |
| True negatives | 1,381 |

A model that predicts every claim as legitimate would achieve **96.31% accuracy** while detecting **zero fraud cases**. Accuracy is therefore not an appropriate headline metric for this imbalanced problem. The random-ranking Average Precision baseline is approximately the fraud prevalence, **0.0369**.

## Decision log

Each row records the alternatives, evidence, choice, and trade-off, as required by the project brief. Metrics are from this dataset's notebook run; see the corresponding notebook sections for the complete tables and plots.

| Decision | Options considered | Evidence | Choice | What it cost me |
|---|---|---|---|---|
| Primary evaluation metric | Accuracy; ROC-AUC; Average Precision | Fraud prevalence is 3.6875%; all-legitimate accuracy is 96.31%; random Average Precision baseline is 0.0369. | Use Average Precision as the primary ranking metric, alongside precision, recall, ROC-AUC and Brier score. | Average Precision does not itself encode investigation costs or team capacity. |
| Missing numeric values | Drop rows; mean imputation; median imputation | `age` has 120 missing values and `days_to_report` has 90; the notebook inspects distributions and missingness. | Median imputation plus missingness indicators, fitted inside the training pipeline. | Imputed values are estimates and may not explain why a value is missing. |
| Model family | Decision Tree; Random Forest; XGBoost | Validation Average Precision: Random Forest 0.1722; XGBoost 0.1698; Decision Tree 0.0800. Random Forest has a large train–validation gap (0.6768). | Carry Random Forest forward because it had the highest validation Average Precision. | The large gap signals substantial overfitting risk; the simpler Decision Tree ranked worse. |
| Imbalance handling | No handling; class weights; random oversampling | Validation Average Precision: no handling 0.1722; class weights 0.2037; oversampling 0.2151. Recall: 0.0000; 0.1064; 0.1277 respectively. Precision: 0.0000; 0.2941; 0.1818. Brier: 0.0330; 0.0448; 0.0479. | Use class weighting for the cost and calibration analysis because it gives a higher precision and better Brier score than oversampling, while improving ranking and recall over no handling. | Oversampling ranked better and caught more fraud at the evaluated threshold; class weighting still produces probability distortion that must be calibrated. |
| Threshold selection | Default 0.50; threshold minimizing validation cost | With false-negative cost 20 and false-positive cost 1, the uncalibrated cost-optimal threshold is 0.245; validation cost is 480 versus 852 at 0.50, a 43.66% reduction. | Select the threshold using validation costs, then reselect on calibrated validation probabilities before final test evaluation. | A cost-minimizing threshold can exceed review capacity and depends on the assumed cost ratio. |
| Capacity planning | Cost-optimal threshold; capacity-feasible threshold | The brief states a capacity of about 200 claims/month, but the dataset does not specify real monthly claim volume. The notebook's 1,000-claim monthly volume is illustrative only. | Compare the flag rate against capacity once the business confirms actual monthly volume; do not present the illustrative volume as a fact. | The final operational threshold cannot be confirmed from this dataset alone. |
| Probability calibration | Use raw class-weighted scores; calibrate on real-prevalence data | Class weighting can distort probabilities. The notebook compares Brier scores and calibration curves and calibrates without resampling the calibration data. | Use calibrated probabilities for the final probability-based test evaluation. | Calibration can improve probability reliability but does not guarantee perfect calibration or strong ranking. |
| Model interpretation | Use feature importance alone; inspect correlations and SHAP | The notebook checks numeric feature correlations and generates SHAP summary and individual explanations. | Use SHAP with correlation checks and individual claim explanations to support human review. | SHAP explains model behaviour, not causality; correlated features can share or obscure attribution. |
| Final test protocol | Tune using test data; keep test data untouched until final evaluation | The notebook creates train, validation and test partitions; model and threshold decisions are made using development/validation data. | Use the test set once for the final estimate. | The estimate can still vary because fraud cases are relatively rare; future monitoring is necessary. |

## Important limitations

- The final test precision is 0.1209, so many flagged claims will be legitimate and require human review.
- The final test contains 59 fraud cases; the reported results are estimates and may vary on future claims.
- Monthly claim volume is not supplied, so the 200-claim capacity constraint must be checked with real operational volume.
- SHAP explains model associations, not proof of fraud or causation.

## Submission checklist

- [x] Notebook included
- [x] Dataset included beside notebook
- [x] README includes a decision log with more than eight decisions and all five required columns
- [x] One-page recommendation included
- [ ] Restart kernel and run all cells in the submission folder before uploading
