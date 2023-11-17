from bs4 import BeautifulSoup
import pandas as pd


# Load the HTML file
with open('./data/bonos.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

# Find all tables in the HTML
tables = soup.find_all('table')

# Extract data from each table and convert to a DataFrame
dataframes = []
for i, table in enumerate(tables):
    # Extracting the table
    df = pd.read_html(str(table))[0]
    dataframes.append(df)

    # Saving the table as a CSV
    csv_file_path = f'data/extracted_table_{i+1}.csv'
    df.to_csv(csv_file_path, index=False)

# Display the paths to the saved CSV files
csv_file_paths = [f'data/extracted_table_{i+1}.csv' for i in range(len(tables))]
csv_file_paths

