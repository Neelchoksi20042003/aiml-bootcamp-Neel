"""Optional: save the EXACT scikit-learn California Housing dataset (20,640 rows, no missing values)
to data/california_housing.csv. Needs internet. Run:  python download_data.py"""
from pathlib import Path
from sklearn.datasets import fetch_california_housing

Path("data").mkdir(exist_ok=True)
df = fetch_california_housing(as_frame=True).frame
df.to_csv("data/california_housing.csv", index=False)
print("Saved", df.shape, "-> data/california_housing.csv")
