# Recommendation to the Claims Investigation Team

**Subject: Pilot recommendation for insurance claim fraud prioritization**

## Recommendation

Pilot the model as a **human-review prioritization aid**, not as an automatic fraud decision. The dataset contains 8,000 claims, of which 295 (3.69%) are labelled fraudulent. The final test results show that the calibrated model identified 22 of 59 fraud cases in the test set (recall 37.29%). At the selected threshold, 182 claims were flagged: 22 fraudulent and 160 legitimate. This means the model can help surface some suspicious claims, but investigators should expect most flagged claims to be legitimate.

The final test Average Precision is **0.1227**, compared with a random-ranking baseline of about **0.0369**. This is an improvement over random ranking, but it is not sufficient to treat the model as a reliable fraud verdict. The test ROC-AUC is **0.7405**. At the selected threshold, precision is **12.09%** and recall is **37.29%**.

## How to use the score

The notebook selects a probability threshold of **0.065** using validation data after calibration, under the assumed cost of 20 units for a missed fraud case versus 1 unit to investigate a legitimate claim. Claims above the threshold should be sent for investigation, with the score used to help order the queue. The threshold should not be treated as final until the team confirms actual incoming monthly claim volume: the brief states capacity of approximately 200 investigations per month, but the dataset does not tell us the real monthly volume. A 1,000-claim monthly volume used in the notebook is illustrative, not a measured business fact.

Do not multiply the score by claim amount for financial prioritization until probability calibration has been checked on representative, recent data. Even calibrated probabilities need ongoing validation as claim patterns change.

## What influences predictions

The notebook includes feature-level and individual-claim SHAP explanations so investigators can inspect why the model assigned a higher or lower score. These explanations describe patterns learned by the model; they do not prove that a claim is fraudulent. Investigators should record whether explanations are sensible and flag unexpected drivers for review.

## Two important limitations

1. **False alarms remain common.** On the final test set, 160 legitimate claims were flagged alongside 22 fraud cases. Human review is essential, and the team must decide whether this workload is acceptable.
2. **Performance and capacity are uncertain in live use.** Fraud cases are rare, the test estimate is based on a limited number of positive cases, and real monthly claim volume was not supplied. Performance may change on future claims.

## Next steps over one more week

Run a controlled pilot on recent claims with investigator feedback; confirm monthly volume and review capacity; measure precision, recall, investigation workload and missed-fraud cost; monitor calibration and feature drift; and review SHAP explanations for suspicious or unavailable-at-prediction-time features. Adjust the threshold only using a validation process, then evaluate once on a separate holdout set.
