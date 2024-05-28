import os
import pandas as pd

# Specify the folder path
folder_path = 'C:/Users/thebe/OneDrive/Desktop/Progetto Icon/ProgettoIcon/Dataset Formula1'
folder_path1 = 'C:/Users/thebe/OneDrive/Desktop/Progetto Icon/ProgettoIcon/Dataset Energy'

# List all files in the folder
files = os.listdir(folder_path1)

# Iterate through each file
for file in files:
    if file.endswith('.csv'):  # Check if the file is a CSV file
        file_path = os.path.join(folder_path1, file)
        df = pd.read_csv(file_path)
        print(df)