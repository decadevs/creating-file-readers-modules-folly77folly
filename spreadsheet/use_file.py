from spreadsheet import AllCsvFiles
import pandas as pd

text_file = AllCsvFiles('iris2.csv')
print(next(text_file))
print(next(text_file))
print(text_file.fetch_first_two_rows())
# print(text_file.fetch_last_two_rows())

# df = pd.read_csv('iris2.csv')
# print(df)
