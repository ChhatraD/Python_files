import os
import openpyxl

folder_path = "D:\Dummy"
cell_address = "B17"  # Change this to the specific cell you want to pick the name from

for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(folder_path, filename)
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active  # or specify the sheet name: workbook['Sheet1']
        new_name = str(sheet[cell_address].value).strip()  # Get the value from the specified cell

        if new_name:
            new_filename = f"{new_name}.xlsx"
            new_file_path = os.path.join(folder_path, new_filename)
            os.rename(file_path, new_file_path)
            print(f"Renamed {filename} to {new_filename}")
        workbook.close()
