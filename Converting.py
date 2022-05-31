'''
This program convert date in base_pd from yyyy.mm.dd to dd.mm.yyyy'''


import csv
import re


new_list = []
with open(file = 'base_pd.csv', mode = 'r', encoding = 'utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = ';')
    for row in file_reader:
        pattern_old = r'^\d{4}.\d{2}.\d{2}'
        old_date = re.search(pattern_old, row[1])
        if old_date:
            yyyy, mm, dd = tuple(re.split(r'\.', row[1]))
            new_date = dd + '.' + mm + '.' + yyyy
            row[1] = new_date
            new_list.append(row)
        else:
            new_list.append(row)
print(new_list)
