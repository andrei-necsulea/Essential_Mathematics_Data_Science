'''
Using the Shapiro-Wilk test, check whether the given sample has a normal distribution:
[0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869].
'''

from scipy.stats import shapiro

# Given sample
sample = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]

# Perform Shapiro-Wilk test
stat, p_value = shapiro(sample)

# Results
print(f"Shapiro-Wilk Test Statistic: {stat:.4f}")
print(f"P-value: {p_value:.4f}")

# Interpretation
if p_value < 0.05:
    print("→ The sample does NOT follow a normal distribution (reject H₀).")
else:
    print("→ The sample MAY follow a normal distribution (fail to reject H₀).")