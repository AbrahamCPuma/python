file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]
filecheck = []

for check in file_list:
    
    if check in filecheck:
        print(f'"Duplicate found": {check} is already in the list')
        break
    filecheck.append(check)
else:
    print('"All files are unique"')
