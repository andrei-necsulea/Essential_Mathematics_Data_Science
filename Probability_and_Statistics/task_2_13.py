'''
Bayes' theorem applied

P(A|B)= P(B|A)⋅ P(A) / P(B)

Imagine you're testing for a rare disease,
and producent claims that the test is 95% accurate,
meaning that if you have a disease,
you will test positive 95% of the time and if yopu don't you will test negative 95% of the time.
Assuming that 0.5% of the population has the disease and someone tests positive.
What's the probability that the person is sick?
'''

import numpy as np

# Parameters
population_size = 1_000_000
disease_prevalence = 0.005      # 0.5% of population has the disease
sensitivity = 0.95              # P(positive | sick)
specificity = 0.95              # P(negative | healthy)

# 1. Simulate who has the disease
has_disease = np.random.rand(population_size) < disease_prevalence  # True if sick

# 2. Simulate the test result:
# If sick => 95% chance of positive test
# If healthy => 5% chance of false positive
test_positive = np.where(
    has_disease,
    np.random.rand(population_size) < sensitivity,
    np.random.rand(population_size) < (1 - specificity)
)

# 3. Count true positives (people who are both sick and tested positive)
true_positives = np.sum(test_positive & has_disease)
total_positives = np.sum(test_positive)

# 4. Compute P(sick | positive test)
probability_sick_given_positive = true_positives / total_positives

print(f"Out of {total_positives} positive results, {true_positives} are truly sick.")
print(f"Probability of being sick given a positive test: {probability_sick_given_positive:.4f} ({probability_sick_given_positive*100:.2f}%)")