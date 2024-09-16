import pandas as pd
import pd_settings

tables=pd.read_html(
    "https://www.iban.com/country-codes",
    flavor="html5lib"
)

table_one=tables[0]
table_one['Numeric']=[int(i) for i in table_one['Numeric'].to_list()]

table_one.sort_values('Numeric', ascending=True, inplace=True)
print(table_one.loc[table_one['Country']=='Sierra Leone'])

print(table_one.count())
print(table_one.head())

# print(table_one)