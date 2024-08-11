import pandas as pd
import pd_settings

tables=pd.read_html(
    "https://www.iban.com/country-codes",
    flavor="html5lib"
)

table_one=tables[0]

print(table_one)