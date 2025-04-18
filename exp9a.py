#read the csv dataset and implement group by functionality using pandas
import pandas as pd
text_file_path = r'C:\Users\Harsh Jain\Documents\Python_sem4\Salaries.csv'
read_data = pd.read_csv(r'C:\Users\Harsh Jain\Documents\Python_sem4\Salaries.csv')
""" print(read_data) """


#now use groupby function only on rank column and find the mean of all the columns
grouped_data = read_data.groupby('rank')
print(grouped_data)

#check the size of the grouped data
print("Size of grouped data:", grouped_data.size())


#convert txt file to csv file
import pandas as pd

# Read the .txt file (assuming it is tab-delimited or space-delimited)
txt_file_path = r'C:\Users\Harsh Jain\Documents\Python_sem4\Marketing_analysis.txt'
csv_file_path = r'C:\Users\Harsh Jain\Documents\Python_sem4\Marketing_analysis.csv'

# Adjust the delimiter based on your .txt file structure (e.g., '\t' for tab, ',' for comma, or ' ' for space)
read_txt = pd.read_csv(txt_file_path, delimiter='\t')

# Save the data to a .csv file
read_txt.to_csv(csv_file_path, index=False)

print(f"File converted successfully and saved to {csv_file_path}")

#refine the dataset use skip rows = 2

# Convert txt file to csv file with refinement (skip first 2 rows)
import pandas as pd

# File paths
txt_file_path = r'C:\Users\Harsh Jain\Documents\Python_sem4\Marketing_analysis.txt'
csv_file_path = r'C:\Users\Harsh Jain\Documents\Python_sem4\Marketing_analysis.csv'

# Read the .txt file, skipping the first 2 rows
read_txt = pd.read_csv(txt_file_path, delimiter='\t', skiprows=2)

# Save the refined data to a .csv file
read_txt.to_csv(csv_file_path, index=False)

print(f"File refined (skipped first 2 rows) and converted successfully to {csv_file_path}")

