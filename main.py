import matplotlib.pyplot as plt
import pandas as pd

media_df = pd.read_csv('statistic.csv')

media_df.columns = media_df.columns.str.strip()

print(media_df.columns)


media_df['Year'] = media_df['Year'].astype(str).str.replace('-', '').astype(int)

plt.plot(media_df['Year'], 
         media_df.iloc[:, 1]) 
plt.xlabel('Year')
plt.ylabel('Number of social media users in the US (millions)')
plt.title('Social Media User Growth Over the Years')
plt.grid(True)
plt.xticks(media_df['Year']) 
plt.show()

df = pd.read_csv('social media use by age.csv')
percentage = df['Percentage'].str.rstrip('%').astype('float')
age_groups = df['Age Group'].tolist()

plt.figure(figsize=(8, 8))
plt.pie(percentage, labels=age_groups, autopct='%1.1f%%', startangle=0)
plt.axis('equal')
plt.title('Social Media Use by Age Group in the US in 2023')
plt.show()
