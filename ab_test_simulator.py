import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
import seaborn as sns

# Simulate data
np.random.seed(42)
n = 1000
group_A = np.random.normal(loc=60, scale=10, size=n)
group_B = np.random.normal(loc=62, scale=10, size=n)

# Create DataFrame
df = pd.DataFrame({
    'user_id': np.arange(2 * n),
    'group': ['A'] * n + ['B'] * n,
    'conversion_rate': np.concatenate([group_A, group_B])
})

# Save data
df.to_csv('ab_test_data.csv', index=False)

# Run t-test
t_stat, p_val = ttest_ind(group_A, group_B)

# Write summary
with open('ab_test_summary.txt', 'w') as f:
    f.write(f"T-test Statistic: {t_stat:.4f}\n")
    f.write(f"P-value: {p_val:.4f}\n")
    f.write("Result: " + ("Statistically significant difference.\n" if p_val < 0.05 else "No significant difference.\n"))

# Plot
plt.figure(figsize=(10, 5))
sns.histplot(data=df, x='conversion_rate', hue='group', kde=True, bins=30)
plt.title('A/B Test Conversion Rate Distribution')
plt.xlabel('Conversion Rate')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('ab_test_plot.png')
