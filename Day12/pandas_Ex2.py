import pandas as pd



# Indexing the columns for faster retrieval
"""data = {
    'Region': ['North', 'South', 'East', 'West', 'Central'],
    'State': ['New York', 'Texas', 'Florida', 'California', 'Illinois'],
    'Year': [2020, 2021, 2022, 2023, 2024],
    'Sales': [5000, 7000, 6500, 8000, 7200],
    'Profit': [1200, 1500, 1700, 2000, 1800]
}
df = pd.DataFrame(data)
print(df,"\n")
df.set_index(['Region', 'State', 'Year'], inplace=True)
print(df.loc[('North', 'New York', 2020),'Sales'])

print(df) """ 

df_sales = pd.DataFrame({
    'State': ['New York', 'Texas', 'Florida', 'California', 'Illinois'],
    'Sales': [5000, 7000, 6500, 8000, 7200]
})


df_profits = pd.DataFrame({
    'State': ['New York', 'Texas', 'Florida', 'California', 'Illinois'],
    'Profits': [1200, 1500, 1700, 2000, 1800]
})

df_merged = pd.merge(df_sales,df_profits,on='State',how='inner')
# print(df_merged.loc[0])
print(df_merged)


