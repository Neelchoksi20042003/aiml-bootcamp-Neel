# Ames Housing Price Analysis

## Phase 1 Capstone — End-to-End Data Analysis

This project is the Phase 1 Capstone Mini Project of the CodeTrade
AI/ML Internship.

The objective is to analyze the Ames Housing dataset and determine
which property characteristics are most strongly associated with
house sale prices, with particular focus on overall quality,
living area, and neighborhood.

---

# 1. Project Question

## Primary Question

Which property characteristics are most strongly associated with
house sale prices in the Ames Housing dataset, and how much do
overall quality and neighborhood contribute to differences in
sale price?

## Supporting Questions

1. Is SalePrice strongly related to above-ground living area?
2. Does overall quality correspond to higher sale prices?
3. Do sale prices differ substantially across neighborhoods?
4. Are the observed differences between quality groups and
   neighborhoods statistically meaningful?

---

# 2. Dataset

The project uses the Ames Housing dataset.

The original dataset contains:

- 1,460 rows
- 11 columns
- 248 missing values

The main variables used in the analysis include:

- `Neighborhood`
- `OverallQual`
- `GrLivArea`
- `YearBuilt`
- `Bedrooms`
- `FullBath`
- `GarageCars`
- `LotArea`
- `SalePrice`

### Target Variable

`SalePrice`

This represents the sale price of the house.

---

# 3. Project Workflow

The project follows the complete Phase 1 Capstone workflow:

1. Frame the question
2. Assess the data
3. Clean the data
4. Explore the data
5. Test two hypotheses
6. Visualize the findings
7. Write the final report
8. Package the project for reproducibility

---

# 4. Stage 1 — Frame the Question

The project begins by defining a specific question about the
factors associated with house sale prices.

The analysis focuses on three major factors:

- Overall Quality
- Above-Ground Living Area
- Neighborhood

The goal is not simply to create charts, but to use the evidence
to answer a practical property-pricing question.

---

# 5. Stage 2 — Assess the Data

The original dataset contained:

```text
Rows: 1,460
Columns: 11