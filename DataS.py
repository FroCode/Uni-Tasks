import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# # Step 1: Read the wine.names file to extract attribute names
# attribute_names = ['id',
#     "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium",
#     "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins",
#     "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"
# ]
# with open('wine/wine.names', 'r') as names_file:
#     for line in names_file:
#         # Assuming attribute names start with a digit and end with a colon
#         if line[0].isdigit() and line.endswith(':'):
#             attribute_names.append(line.strip()[:-1])

# # Step 2: Read the wine.data file
# data_df = pd.read_csv('wine/wine.data', header=None)

# # Step 3: Rename the columns of the data DataFrame with attribute names
# data_df.columns = attribute_names

# # Step 4: Save the merged DataFrame to a new CSV file
# data_df.to_csv('merged_wine_data.csv', index=False)


df = pd.read_csv('merged_wine_data.csv')
alcohol_range = df['Alcohol'].min(), df['Alcohol'].max()

print("Range of Alcohol content: {}".format(alcohol_range))


# Assuming your dataset is stored in a variable called 'df'
# Access the 'Malic acid' column and calculate the mean
malic_acid_mean = df['Malic acid'].mean()

print("Average amount of Malic acid: {}".format(malic_acid_mean))
plt.figure(figsize=(8, 6))
sns.histplot(color_intensity_values, bins=20, kde=True, color='blue')  # Adjust the number of bins as needed
plt.title('Distribution of Color intensity')
plt.xlabel('Color intensity')
plt.ylabel('Frequency')
plt.show()