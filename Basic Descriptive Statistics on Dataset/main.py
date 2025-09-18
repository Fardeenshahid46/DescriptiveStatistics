import seaborn as sns
#Load the iris dataset
iris=sns.load_dataset('iris')
#Display the first 5 rows and descriptive statistics of the dataset
print("First 5 rows of the Iris dataset:\n", iris.head(),"\n")
print("Descriptive Statistics:\n", iris.describe(),"\n")
#Calculate and display mean, min, max, and standard deviation for each numerical column
print("Mean of each column:\n",iris.mean(numeric_only=True),"\n")
print("Min of each column:\n",iris.min(numeric_only=True),"\n")
print("Max of each column:\n",iris.max(numeric_only=True),"\n")
print("Standard Deviation of each column:\n",iris.std(numeric_only=True),"\n")