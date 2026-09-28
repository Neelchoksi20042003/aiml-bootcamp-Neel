# Phase 1 Capstone — Ames Housing

## Project Overview
This project analyzes the Ames Housing dataset to understand which property characteristics and neighborhood factors are most strongly associated with house sale prices.

## Primary Question
**Which property characteristics are most strongly associated with house sale prices in the Ames housing dataset?**

Supporting questions:
1. Is above-ground living area (`GrLivArea`) associated with `SalePrice`?
2. Do higher-quality houses have meaningfully different sale prices?
3. Does `SalePrice` differ across neighborhoods?
4. Does the living-area/price relationship change when overall quality is considered?

## Key Findings
- `OverallQual` has the strongest observed correlation with `SalePrice` among the selected numeric variables: **r = 0.80**.
- `GrLivArea` is also positively associated with `SalePrice`: **r = 0.60**.
- The quality-group comparison produced **Welch t = 36.328**, **p = 4.74869e-149**, and **Cohen's d = 2.505**. A sensitivity check that includes Quality 6 gives **t = 31.72** and **d = 1.73**: the effect is smaller, but the conclusion is unchanged.
- Neighborhood comparison produced **ANOVA F = 400.101**, **p ≈ 0**, and **eta squared = 0.795**.
- The most notable finding is that living area alone does not fully explain price; overall quality shifts the price range even at similar living areas.

## Dataset
The project uses `ames_housing.csv` with 1,460 rows and 11 original columns. The cleaned file `ames_housing_final_cleaned.csv` has 1,460 rows and 10 columns (9 original columns + the derived `QualityGroup`).

## Cleaning Decisions
- Removed `Id` because it is an identifier, not a property characteristic (the `Id` is still read from the raw file when listing the outlier records).
- `LotFrontage` had 248 missing values (16.99%). Mean/median imputation was considered and its effect on spread was measured, but the column was removed because it was not required for the primary questions.
- No duplicate rows were found.
- `YearBuilt` was checked for impossible values: no zero/negative years, none after today's year, and none after 2010 (the last year of the Ames data). The observed range is 1900–2010.
- Six potential `SalePrice` outliers were identified by the IQR rule and investigated individually. They were retained because the available evidence did not establish data-entry errors.
- `QualityGroup` is a derived analysis variable. Quality 6 remains in the cleaned dataset but is excluded from the main two-group hypothesis test. Because this can inflate the effect size, the test is repeated with Quality 6 included as a sensitivity check, and the exclusion is documented as a limitation.

## Statistical Approach
- **Welch's t-test:** comparison of High Quality (`OverallQual >= 7`) vs Low/Medium Quality (`OverallQual <= 5`).
- **Cohen's d:** effect size for the two-group comparison.
- **One-way ANOVA:** comparison of SalePrice across 15 neighborhoods.
- **Levene's test:** variance assumption check for ANOVA.
- **Tukey HSD:** post-hoc pairwise neighborhood comparisons.
- **Eta squared:** ANOVA effect size.
- Normality was checked using Shapiro-Wilk tests. Both quality groups reject strict normality, as do 2 of the 15 neighborhoods (MeadowV and Timber). Because the groups are reasonably large, Welch's t-test and ANOVA are kept as robust methods and the non-normality is stated as a limitation.

## Repository Structure

```text
day22_miniproject/
├── phase1_capstone_FINAL_SUBMISSION.ipynb
├── ames_housing.csv
├── ames_housing_final_cleaned.csv
├── requirements.txt
├── README.md
├── report/
│   └── Phase1_Ames_Housing_Final_Project_Report_SUBMISSION.pdf
└── figures/
    ├── chart_01_saleprice_distribution.png
    ├── chart_02_grlivarea_saleprice.png
    ├── chart_03_neighborhood_median.png
    ├── chart_04_quality_saleprice.png
    ├── chart_05_area_quality_saleprice.png
    ├── chart_06_correlation_heatmap.png
    ├── chart_07_quality_groups.png
    └── chart_08_neighborhood_boxplot.png
```

## How to Run

Create/activate a Python environment, then install:

```bash
pip install -r requirements.txt
```

Open the notebook:

```bash
jupyter notebook
```

Run `phase1_capstone_FINAL_SUBMISSION.ipynb` from top to bottom on a fresh kernel. It re-creates `ames_housing_final_cleaned.csv` and the charts in `figures/`.

## Important Note
This is observational data. The findings describe associations in this dataset; they do not prove that a property characteristic causes a specific change in sale price.
