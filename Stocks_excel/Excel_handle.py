import openpyxl

wb = openpyxl.load_workbook('stocks.xlsx')
ws = wb['IBM']
tData = []
for row in ws.iter_rows(min_col=1, max_col=4):
    date = row[0].value
    price=row[3].value
    if (date.year ==2010):
        tData.append(price) 

print("2010 Min ", min(tData))
print("2010 Max ", max(tData))
print("2010 Avg ", sum(tData)/len(tData))