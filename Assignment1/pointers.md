Goal: Predict the mood of the next day for the subjects in the dataset (being the average of the mood values measured during that day).

TASK 1: DATA PREPARATION (30 points)

1A: EXPLORATORY DATA ANALYSIS (10 points)
- Counts of entries of each unique variable in the dataset for every person/id.
- The warning you received about the Shapiro-Wilk test indicates that the test's p-value might not be accurate for sample sizes greater than 5,000. This limitation is a known issue with the Shapiro-Wilk test, as it was primarily designed for smaller datasets. For large datasets, the test can become overly sensitive, often rejecting the null hypothesis of normality for even slight deviations from a perfect normal distribution, which might not be practically significant. UserWarning: scipy.stats.shapiro: For N > 5000, computed p-value may not be accurate. Current N is 96578.
- 