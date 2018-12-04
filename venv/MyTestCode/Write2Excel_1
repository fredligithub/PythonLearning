# https://openpyxl.readthedocs.io/en/stable/
# pip install openpyxl

from openpyxl import Workbook
import datetime

wb= Workbook()
ws= wb.active

# Define the Header
ws['A1'] = 'DateTime'
ws['B1'] = 'Percentage'

ws.append([datetime.datetime.now(),'2%'])
ws.append([datetime.datetime.now(),'3%'])

wb.save("Sample.xlsx")

print("Done!")
