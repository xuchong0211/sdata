import pandas as pd

excel_data_df = pd.read_excel('./123321.xls', sheet_name='description', usecols=['id', 'en', 'indo'])

list = {}
data = []

for index, row in excel_data_df.iterrows():
    id = int(row.id)
    en = str(row.en).strip()
    indo = str(row.indo).strip()
    value = {"description":{"en" :en, "indo": indo}}
    # keyList = en.split(" ")
    # key = "_".join(keyList).upper()

    # print(key)
    list[id] = value
    # print("index:", index);
    # if indo != database:
    #     data.append({"indo": indo, "database": database})

print("--------------------------------")

print(list)

# for index, row in excel_data_df.iterrows():
#     id = str(row.id)
#     ids = int(row.id)
#     test = str(row.test).strip()
#
#
#     list[ids].append({"en": test, "indo": test})
#
#     # print ("33333333333333333333", list)


# print(list)
# print(excel_data_df.to_json(orient='records'))
