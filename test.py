import pandas as pd

# Create a dictionary with the data
data = {
    'Name': ['Alice Johnson', 'Bob Smith', 'Carol White', 'David Brown', 'Emily Davis', 
             'Frank Wilson', 'Grace Miller', 'Henry Moore', 'Irene Taylor', 'Jack Anderson'],
    'Age': [30, 25, 28, 35, 22, 40, 27, 32, 29, 33],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 
             'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

~