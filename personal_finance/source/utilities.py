import matplotlib.pyplot as plt
import source.category_mapping as cat_map
from tabulate import tabulate
import pandas as pd

def categorize_description(description):
    for substring, category in cat_map.category_mapping.items():
        if substring in description:
            return category
    return 'OTHER'

def sanitizeDataframe(df, sortBy='date'):
  df['category'] = df['description'].apply(categorize_description)
  df = df.sort_values(by=sortBy)
  return df[~df['category'].isin(['SKIP', 'INVESTMENT', 'TRANSFER'])]

# Export by month
def filter_df_at_month(df, month):
  df = df.sort_values(by='date')
  df = df[df['date'].dt.month == month]
  return df

def exportDataframe(df, exportFile):
  df = df[['date', 'category', 'transaction', 'description']]
  df.to_csv(f'./output/{exportFile}.csv', index=False)

def plotDataframe(df, title):
  category_sums = df.groupby('category')['transaction'].sum()
  category_percentages = ((category_sums / category_sums.sum()) * 100).astype(int)
  category_percentages.plot.pie(autopct='%1.0f%%', startangle=90, ylabel='', title=title, labeldistance=1.1)
  plt.axis('equal')
  plt.show()

def showPercentage(df):
  category_sums = df.groupby('category')['transaction'].sum()
  category_percentages = ((category_sums / category_sums.sum()) * 100).astype(int).astype(str) + '%'
  print(category_percentages)

def outputTable(df, fileName):
  df = df.sort_values(by=['transaction'])
  
  def format_date(date):
    return pd.to_datetime(date).strftime('%m-%d-%Y')
  
  def format_transaction(transaction):
    return '${:.2f}'.format(transaction)
  
  df['date'] = df['date'].apply(format_date)
  df['transaction'] = df['transaction'].apply(format_transaction)

  # Format the DataFrame as a table using tabulate
  formatted_table = tabulate(df, headers='keys', colalign=['center', 'center', 'center', 'left'])

  # Save the formatted table to a text file
  with open(f'./output/{fileName}.txt', 'w') as file:
      file.write(formatted_table)