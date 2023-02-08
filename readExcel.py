import pandas as pd

excel_data_df = pd.read_excel('./123.xlsx', sheet_name='Sheet5', usecols=['id', 'test'])

list = {}
data = []

for index, row in excel_data_df.iterrows():
    id1 = str(row.id)
    id1s = int(row.id)
    print("78777", id1s);
    list[id1s] = []
    data.append({"id": id1, "test": row.test})

print("--------------------------------")

for index, row in excel_data_df.iterrows():
    id = str(row.id)
    ids = int(row.id)
    test = str(row.test).strip()


    list[ids].append({"en": test, "indo": test})

    # print ("33333333333333333333", list)


print(list)
# print(excel_data_df.to_json(orient='records'))
