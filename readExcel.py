import pandas as pd

excel_data_df = pd.read_excel('./123.xlsx', sheet_name='Sheet3', usecols=['id', 'Description'])

list = {}

for index, row in excel_data_df.iterrows():
    id = str(row.id)
    ids = int(row.id)
    description = str(row.Description)
    result = True
    # id.isnumeric()
    if result  :

        print ("000000000000000000000000000000000", ids)

        list[ids] = description.strip()
    else :
        print ("11111111111111111111111111", id)


print(list)
# print(excel_data_df.to_json(orient='records'))
