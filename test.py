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
df.to_csv('data/data.csv',header=None)

# Display the DataFrame
# print(df)


# commit c10ccfde2df63457ab838786014fbe4f50f901a9 (HEAD -> master)
# Author: Your Name <you@example.com>
# Date:   Sat Jul 20 20:56:53 2024 +0530

#     File adde

# commit 6c0a7d15b50a95847e1b64f42b12487bac65e73a
# Author: Your Name <you@example.com>
# Date:   Sat Jul 20 20:56:00 2024 +0530


# if you want to go previous commit the Use the
# git checkout 86014f