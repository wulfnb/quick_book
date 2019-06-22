import pandas as pd

df1 = pd.DataFrame({'Int_rate': [5, 6, 4, 5, 8],
                    'IND_GDP': [50, 45, 45, 67, 30]},
                   index=[2001, 2002, 2003, 2004, 2005])

df2 = pd.DataFrame({'Low_Tier_HPI': [5, 6, 4, 5],
                    'Unemployment': [1,3,5,6]},
                   index=[2001, 2003, 2004, 2005])


joined = df1.join(df2)

print(joined)