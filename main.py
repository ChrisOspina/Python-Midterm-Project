import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read csv file
df = pd.read_csv('dataset.csv')

# remove null values
df.dropna(inplace=True)

# fill missing values with average
df.fillna(df.mean(), inplace=True)

# display the cleaned data
print(df.head())

# read csv file
data = np.genfromtxt('dataset.csv', delimiter=',')

# remove null values
data = data[~np.isnan(data).any(axis=1)]

# fill missing values with average
col_mean = np.nanmean(data, axis=0)
inds = np.where(np.isnan(data))
data[inds] = np.take(col_mean, inds[1])

# display the cleaned data
print(data)

# create a figure with 3 subplots
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

# subplot 1: histogram of feature 1
axs[0].hist(data['feature1'], bins=20)
axs[0].set_title('Feature 1 Distribution')
axs[0].set_xlabel('Feature 1 Value')
axs[0].set_ylabel('Count')

# subplot 2: scatter plot of feature 1 vs feature 2
axs[1].scatter(data['feature1'], data['feature2'])
axs[1].set_title('Feature 1 vs Feature 2')
axs[1].set_xlabel('Feature 1 Value')
axs[1].set_ylabel('Feature 2 Value')

# subplot 3: box plot of feature 3 by feature 4 category
data.boxplot(column=['feature3'], by=['feature4'], ax=axs[2])
axs[2].set_title('Feature 3 by Feature 4')
axs[2].set_xlabel('Feature 4')
axs[2].set_ylabel('Feature 3 Value')

# adjust subplot spacing and display the plot
plt.subplots_adjust(wspace=0.3)
plt.show()

# create a figure with 4 subplots
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# subplot 1: scatter plot of feature 1 vs feature 3 by feature 4 category
for category, group in data.groupby('feature4'):
    axs[0, 0].scatter(group['feature1'], group['feature3'], label=category)
axs[0, 0].set_title('Feature 1 vs Feature 3 by Feature 4')
axs[0, 0].set_xlabel('Feature 1 Value')
axs[0, 0].set_ylabel('Feature 3 Value')
axs[0, 0].legend()

# subplot 2: bar plot of feature 4 category counts
data['feature4'].value_counts().plot(kind='bar', ax=axs[0, 1])
axs[0, 1].set_title('Feature 4 Category Counts')
axs[0, 1].set_xlabel('Feature 4 Category')
axs[0, 1].set_ylabel('Count')

# subplot 3: scatter matrix of all features
pd.plotting.scatter_matrix(data, ax=axs[1, 0])
axs[1, 0].set_title('Scatter Matrix of All Features')

# subplot 4: heatmap of feature correlations
corr_matrix = data.corr()
im = axs[1, 1].imshow(corr_matrix, cmap='coolwarm')
cbar = axs[1, 1].figure.colorbar(im, ax=axs[1, 1])
cbar.ax.set_ylabel('Correlation')
axs[1, 1].set_title('Feature Correlations')

# adjust subplot spacing and display the plot
plt.subplots_adjust(wspace=0.3, hspace=0.3)
plt.show()
