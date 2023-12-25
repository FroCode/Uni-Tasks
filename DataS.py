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
color_intensity_values = df['Color intensity']

plt.figure(figsize=(8, 6))
sns.histplot(color_intensity_values, bins=20, kde=True, color='blue')  # Adjust the number of bins as needed
plt.title('Distribution of Color intensity')
plt.xlabel('Color intensity')
plt.ylabel('Frequency')
plt.show()

alcohol_content = df['Alcohol']
color_intensity = df['Color intensity']

# Calculate the correlation coefficient
correlation_coefficient = alcohol_content.corr(color_intensity)

print("Correlation coefficient between Alcohol content and Color intensity: {}".format(correlation_coefficient))
phenolic_compounds = df[['Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins']]

# Calculate the correlation matrix
correlation_matrix = phenolic_compounds.corr()

# Create a heatmap for visualization
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix of Phenolic Compounds')
plt.show()

magnesium_values = df['Magnesium']

# Create a histogram for Magnesium values
plt.figure(figsize=(8, 6))
plt.hist(magnesium_values, bins=20, color='green', edgecolor='black')  # Adjust the number of bins as needed
plt.title('Distribution of Magnesium Values')
plt.xlabel('Magnesium')
plt.ylabel('Frequency')
plt.show()

# Assuming 'OD280/OD315 of diluted wines' is the column you're interested in
od_values = df['OD280/OD315 of diluted wines']

# Create a histogram for OD280/OD315 values
plt.figure(figsize=(8, 6))
plt.hist(od_values, bins=20, color='orange', edgecolor='black')  # Adjust the number of bins as needed
plt.title('Distribution of OD280/OD315 Values')
plt.xlabel('OD280/OD315')
plt.ylabel('Frequency')
plt.show()
od_values = df['OD280/OD315 of diluted wines']

# Create a histogram for OD280/OD315 values
plt.figure(figsize=(8, 6))
plt.hist(od_values, bins=20, color='orange', edgecolor='black')  # Adjust the number of bins as needed
plt.title('Distribution of OD280/OD315 Values')
plt.xlabel('OD280/OD315')
plt.ylabel('Frequency')
plt.show()


# magnesium_values = df['Magnesium']

# # Get the frequency values using value_counts
# frequency_values = magnesium_values.value_counts()

# # Create a DataFrame to store the frequency values
# frequency_df = pd.DataFrame({'Magnesium': frequency_values.index, 'Frequency': frequency_values.values})

# # Export the frequency values to a CSV file
# frequency_df.to_csv('magnesium_frequency_values.csv', index=False)

# Export OD280/OD315 values to a CSV file
# od_values.to_csv('od_values_distribution_values.csv', index=False)