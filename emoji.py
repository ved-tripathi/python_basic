import openpyxl 
path = "Lib_emoji.xlsx"    # Give the location of the file
wb_obj = openpyxl.load_workbook(path)  #To open the workbook object is created 
sheet_obj = wb_obj.active# Get workbook active sheet object from the active attribute



cell_obj = sheet_obj('A1':'A2')
val = cell_obj.value
print(val)



