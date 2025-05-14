import pandas as pd
import os

# Define initial data
data = {
    'Name': ["Ankit", "Raj", "Rohit"],
    'Age': [20, 19, 22],
    'Score': [90, 85, 88]
}

# Create initial DataFrame
df = pd.DataFrame(data)

# Define a new row as a DataFrame (note the list around values to match column format)
df1 = pd.DataFrame([{
    'Name': "Himanshu",
    'Age': 18,
    'Score': 90
}])

# Concatenate new row to the original DataFrame
df = pd.concat([df, df1], axis=0, ignore_index=True)

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Define file path and save CSV
file_path = os.path.join('data', 'sample_data.csv')
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")
