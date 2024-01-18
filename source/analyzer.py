import pandas as pd
import source.loader as load
import source.utilities as util

def analyzeCreditCard(month, year):
# Import Credit Card Account
  wfDf = load.importWF(f'./input/credit/wf/{month}_{year}.csv');
  boaDf = load.importBOACredit(f'./input/credit/boa/{month}_{year}.csv');
  appleDf = load.importApple(f'./input/credit/apple/{month}_{year}.csv');
  amexDf = load.importAmex(f'./input/credit/amex/{month}_{year}.csv');

  df = pd.concat([wfDf, boaDf, appleDf, amexDf], axis=0)
  df = util.sanitizeDataframe(df);

  # making transactions to be positive
  df = util.filter_df_at_month(df, month)
  df.loc[:, 'transaction'] = df['transaction'].abs()
  util.outputTable(df, f'credit_card_{month}_{year}')

  total_transaction_sum = df['transaction'].sum()
  print(f'Total Expense: {total_transaction_sum}')
  category_sums = df.groupby('category')['transaction'].sum()
  print(f'Expense: {category_sums}')

  category_percentages = (category_sums / total_transaction_sum * 100).round(2).astype(str) + '%'
  print(f'Category: {category_percentages}')

  util.plotDataframe(df, f'{month}/{year} Credit Card')


def analyzeChecking(month, year):
  # Import Checking Account
  wfDf = load.importWF(f'./input/checking/wf/{month}_{year}.csv');
  boaDf = load.importBOA(f'./input/checking/boa/{month}_{year}.csv');
  tdDf = load.importTD(f'./input/checking/td/{month}_{year}.csv');

  df = pd.concat([wfDf, boaDf, tdDf], axis=0)
  df = util.sanitizeDataframe(df, 'transaction');
  df = util.filter_df_at_month(df, month)
  util.exportDataframe(df, f'checking_{month}_{year}')

  incomeDf = df[df['transaction'] >= 0]

  totalIncomeSum = incomeDf['transaction'].sum()
  totalIncome = incomeDf.groupby('category')['transaction'].sum()
  print(f'Total Income: {totalIncomeSum.round(2)}')
  print(f'Income: {totalIncome}')

  util.outputTable(incomeDf, f'checking_income_{month}_{year}')
  util.exportDataframe(incomeDf, f'checking_income_{month}_{year}')

  expenseDf = df[df['transaction'] < 0]
  category_sums = expenseDf.groupby('category')['transaction'].sum()

  expenseDf.loc[:, 'transaction'] = expenseDf['transaction'].abs()

  total_transaction_sum = expenseDf['transaction'].sum()
  print(f'Total Expense: {total_transaction_sum.round(2)}')
  print(f'Expense: {category_sums}')

  category_percentages = (category_sums / total_transaction_sum * 100).round(2).astype(str) + '%'
  print(f'Category: {category_percentages}')

  util.outputTable(expenseDf, f'checking_expense_{month}_{year}')
  util.exportDataframe(expenseDf, f'checking_expense_{month}_{year}')
  util.plotDataframe(expenseDf, f'{month}/{year} Checking Expense')