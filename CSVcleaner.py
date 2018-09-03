import pandas as pd

# Load the raw data 
df = pd.read_csv('marriage_data.csv')

#reshapes dataframe from wide to long format and renames columns
reshape = pd.melt(df, id_vars=['State'], var_name='Year and Type', value_name='Rate')

#takes the 'Year and Type' column and splits it into 'Year' and 'Relationship'
reshape['Year'], reshape['Relationship'] = zip(*reshape['Year and Type'].map(lambda x: x.split(' ')))

#drop the 'Year and Type' column from being listed and prints the dataset 
print(reshape.drop(['Year and Type'], axis=1).to_string())

#produce a csv file of the 'reshape' output
reshape.drop(['Year and Type'], axis=1).to_csv('output.csv')