import pandas as pd
import numpy as np
import os

# Import
def importWF(filePath):
  if os.path.exists(filePath):
    df = pd.read_csv(filePath, usecols=[0, 1, 4], names=["date","transaction","description"])
    df['date'] = pd.to_datetime(df['date'])
    return df
  else:
    print(f"The file '{filePath}' does not exist.")

def importTD(filePath):
  if os.path.exists(filePath):
    df = pd.read_csv(filePath, skiprows=1, header=None, usecols=[0, 4, 5, 6], names=['date', 'description', 'debit', 'credit'])
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='coerce')
    df['debit'] = pd.to_numeric(df['debit'], errors='coerce')
    df['credit'] = pd.to_numeric(df['credit'], errors='coerce')
    df['transaction'] = np.where(df['debit'].notnull(), -df['debit'], df['credit'])
    df = df.drop(['debit', 'credit'], axis=1)
    return df
  else:
    print(f"The file '{filePath}' does not exist.")

def importBOA(filePath):
  if os.path.exists(filePath):
    df = pd.read_csv(filePath, header=None, skiprows=1, usecols=[0, 1, 2], names=['date', 'description', 'transaction'])
    df['date'] = pd.to_datetime(df['date'])
    df['transaction'] = pd.to_numeric(df['transaction'].str.replace(',', ''), errors='coerce')
    return df
  else:
    print(f"The file '{filePath}' does not exist.")

def importBOACredit(filePath):
  if os.path.exists(filePath):
    df = pd.read_csv(filePath, header=None, skiprows=1, usecols=[0, 2, 4], names=['date', 'description', 'transaction'])
    df['date'] = pd.to_datetime(df['date'])
    return df
  else:
    print(f"The file '{filePath}' does not exist.")

def importApple(filePath):
  if os.path.exists(filePath):
    df = pd.read_csv(filePath, skiprows=1, usecols=[0, 2, 6], names=['date', 'description', 'transaction'])
    df['date'] = pd.to_datetime(df['date'])
    return df
  else:
    print(f"The file '{filePath}' does not exist.")

def importAmex(filePath):
  if os.path.exists(filePath):
    df = pd.read_csv(filePath, skiprows=1, usecols=[0, 2, 3], names=['date', 'description', 'transaction'])
    df['date'] = pd.to_datetime(df['date'])
    return df
  else:
    print(f"The file '{filePath}' does not exist.")
