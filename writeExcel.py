from xlwt import Workbook
import xlwt


# def BRAIN = [97, 98, 99, 101, 102, 103, 104, 109, 105, 106, 107]

# def ORGAN_PROTOCOL_MAPPING = {
#     "brain": {
#         "protocols": BRAIN
#     }
# }

text = ["1111", "22222", "3333"]


book = Workbook(style_compression=10)
sheet1 = book.add_sheet('Sheet 1')
for item in text:
    # print('---------------', row)
    print('---------------', item)
    sheet1.write(0, 0, item)
book.save('simple.xls')
