from openpyxl import Workbook
wb = Workbook()
ws = wb.active
x =[[1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
    ]
ws.append(['row1', 'row2', 'row3', 'row4', 'row5'])
for i in x:
    ws.append(i)
    ws.save("Names.xls")
    print("File Created")