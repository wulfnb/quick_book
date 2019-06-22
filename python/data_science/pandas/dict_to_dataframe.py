import pandas as pd


new_dict  = {'Day':[1,2,3,4,5,6],
            'Visitors':[1000,122,100,200,300,350], 
            'Bounce_Rate':[20,20,2,25,21,1]}


df = pd.DataFrame(new_dict)

print(df)

# Slice dataframe for starting 2 rows
print(df.head(2))

# Slice dataframe for ending 2 rows
print(df.tail(2))
