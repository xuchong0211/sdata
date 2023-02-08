from xlwt import Workbook
import xlwt
# book = Workbook(style_compression=10)
# sheet1 = book.add_sheet('Sheet 1')
for i in range(0, 100):
    # st = xlwt.easyxf('pattern: pattern solid;')
    # st.pattern.pattern_fore_colour = i
    print(i // 24)
    # sheet1.write(i % 24, i // 24, 'Test text', st)
# book.save('simple.xls')
