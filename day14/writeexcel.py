import os , openpyxl

file = os.path.join(os.getcwd(),"day14\\empty.xlsx")

workbook = openpyxl.load_workbook(file)
sheet = workbook.active   ##if only one sheet present (called active sheet)

# sheet = workbook["Sheet1"] ##if multiple sheets then we use this

# # write same data in all the rows
# for r in range(1,5):
#     for c in range(1,4):
#         sheet.cell(r,c).value="testdata"+str(r)+str(c) ##set data in specific place


###write different data
sheet.cell(1,1).value="Name"
sheet.cell(1,2).value="Age"
sheet.cell(1,3).value="Sex"

sheet.cell(2,1).value="Ajay"
sheet.cell(2,2).value="34"
sheet.cell(2,3).value="Male"

sheet.cell(3,1).value="Vijay"
sheet.cell(3,2).value="33"
sheet.cell(3,3).value="Male"

sheet.cell(4,1).value="Rashmi"
sheet.cell(4,2).value="24"
sheet.cell(4,3).value="Female"


workbook.save(file)