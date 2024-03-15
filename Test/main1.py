import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('social_media1.csv')

data.dropna(inplace=True)

plt.figure(figsize=(8, 6))
sns.histplot(data['Age'], bins=20, kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

mean_usage_by_age = data.groupby('Age')['Usage'].mean()

plt.figure(figsize=(10, 6))
mean_usage_by_age.plot(kind='bar')
plt.title('Mean Social Media Usage by Age')
plt.xlabel('Age')
plt.ylabel('Mean Usage')
plt.xticks(rotation=45)
plt.show()
