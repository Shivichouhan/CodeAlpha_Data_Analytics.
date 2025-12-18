import seaborn as sns
import matplotlib.pyplot as plt

# Dataset load
df = sns.load_dataset('tips')

# Barplot
sns.barplot(x='day', y='total_bill', data=df)
plt.title('Total Bill by Day')
plt.show()

# Scatterplot
sns.scatterplot(x='total_bill', y='tip', data=df)
plt.title('Total Bill vs Tip')
plt.show()
