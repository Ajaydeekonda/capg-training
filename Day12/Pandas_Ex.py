import pandas as pd
data = {
    "Name":['Alice','Charlie','David'],
    "Age":[23,23,25],
    "City":['Mancherial','Hyderabad','Bangalore']
}
df = pd.DataFrame(data)
# print(df)
# print(df.head())
df2 = pd.read_csv('Day12/customers-100.csv')
# df2.to_json('Day12/output.json',index=False)
# df2.to_html('Day12/output.html',index=False)
# print(df2['Customer Id'])
# print(df2[['First Name','Last Name']])
# print(df2[df2['Index'] == 1])
# dd = df2[df2['Index'] == 1]
# print(dd)
# print(df2.sort_values(by='Index',ascending=False))
# print(df2)
# print(df2)
# df2.groupby('Country').count().to_html('Day12/groupby.html',index=False)
# print(df2.groupby('Country').count())
# print(df2.groupby('Country').sum('Index'))
# print(df2.groupby('Country')['Index'].count())  # Counts non-null 'Index' values per country



