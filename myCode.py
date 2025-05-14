import pandas as pd 
import os 

data = {'Name':["Ankit" , "Raj" , "Rohit"]
        , 'Age':[20,19,22]
        , 'Score':[90,85,88]}

df = pd.DataFrame(data)

os.makedirs('data',exist_ok = True)

file_path = os.path.join('data','sample_data.csv')

df.to_csv(file_path,index = False)

print(f"CSV file saved to {file_path}") 
