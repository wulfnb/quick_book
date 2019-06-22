import pandas as pd


df1 = pd.DataFrame({'HPI': [80, 99, 90, 78, 77],
                    'Int_rate': [5, 6, 4, 5, 8],
                    'IND_GDP': [50, 45, 45, 67, 30]},
                   index=[2001, 2002, 2003, 2004, 2005])

df2 = pd.DataFrame({'HPI': [80, 99, 90, 78, 77],
                    'Int_rate': [5, 6, 4, 5, 8],
                    'IND_GDP': [50, 45, 45, 67, 30]},
                   index=[2006, 2007, 2008, 2009, 2010])


merge = pd.merge(df1, df2)
# On one column
merge2 = pd.merge(df1, df2, on="HPI")

print(merge)
print(merge2)

