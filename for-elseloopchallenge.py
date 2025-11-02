file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]
# An empty list to keep track of files we have already seen.
filecheck = []

# Loop through each file in the original list.
for check in file_list:
    
    # If the current file is already in our tracking list, it's a duplicate.
    if check in filecheck:
        print(f'"Duplicate found": {check} is already in the list')
        break # Exit the loop immediately when a duplicate is found.
    # If it's not a duplicate, add it to our tracking list.
    filecheck.append(check)
else:
    # The 'else' block of a for-loop runs ONLY if the loop completes without hitting a 'break'.
    print('"All files are unique"')
