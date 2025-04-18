
import pandas as pd

# File paths
txt_file_path = r'C:\Users\Harsh Jain\Documents\Python_sem4\Marketing_analysis.txt'
csv_file_path = r'C:\Users\Harsh Jain\Documents\Python_sem4\MA1.csv'

# Step 1: Read the .txt file, skipping the first 2 rows and assuming it is tab-delimited
try:
    read_txt = pd.read_csv(txt_file_path, delimiter='\t', skiprows=2)
    print("Successfully read the .txt file.")
except FileNotFoundError:
    print(f"Error: The file {txt_file_path} was not found.")
    exit()
except Exception as e:
    print(f"An error occurred while reading the .txt file: {e}")
    exit()

# Step 2: Save the refined data to a .csv file
try:
    read_txt.to_csv(csv_file_path, index=False)
    print(f"File refined (skipped first 2 rows) and converted successfully to {csv_file_path}")
except Exception as e:
    print(f"An error occurred while saving the .csv file: {e}")
    exit()

# Step 3: Read the newly created CSV file to check its size
try:
    read_csv = pd.read_csv(csv_file_path)
    print(f"Size of the dataset: {read_csv.shape}")  # Outputs (rows, columns)
except FileNotFoundError:
    print(f"Error: The file {csv_file_path} was not found.")
except Exception as e:
    print(f"An error occurred while reading the .csv file: {e}")


#use fillna function to fill the missing values as well as "yes" with 1 and "no" with 0
try:
    read_csv.replace({'yes': 1, 'no': 0}, inplace=True)
    print("Replaced 'yes' with 1 and 'no' with 0.")
except Exception as e:
    print(f"An error occurred while replacing values: {e}")
    exit()