import pandas as pd

excel_data_df = pd.read_excel('./protocols_description.xlsx', sheet_name='Sheet3', usecols=['id', 'Description'])

list = {}

for index, row in excel_data_df.iterrows():
    id = str(row.id)
    description = str(row.Description)
    result = id.isnumeric()
    if result  :

        print ("000000000000000000000000000000000")

        list[int(id)] = description.strip()
    else :
        print ("11111111111111111111111111", id)


print(list)
# print(excel_data_df.to_json(orient='records'))
