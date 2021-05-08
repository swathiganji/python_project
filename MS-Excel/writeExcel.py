import openpyxl

path="C:/selenium/writeExcel.xlsx"
workbook=openpyxl.load_workbook(path)

#sheet=workbook.get_sheet_by_name("sheet1")
sheet=workbook.active

for r in range(1,5):
    for c in range(1,8):
        sheet.cell(row=r,column=c).value="Welcome"

workbook.save(path)