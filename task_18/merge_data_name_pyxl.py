from openpyxl import Workbook
wb = Workbook()
ws = wb.active
x =[['John','Tom','Sawyer','Ron','Bob'],
    ['Katie','Isabelle','Kimmy','Cheryl','Betty'],
    ['Joe','Emma','Nathan','Sam','Robert']
    ]
ws.append(['col1', 'col2', 'col3', 'col4', 'col5'])
for i in x:
    ws.append(i)
    ws.save("Names.xls")
    print("File Created")