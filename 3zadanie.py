import os
from operator import itemgetter
# from contextlib import nested
current = os.getcwd()
folder_name = 'sorted'
file_name1 = '1.txt'
file_name2 = '2.txt'
file_name3 = '3.txt'
full_path1 = os.path.join(current, folder_name, file_name1)
full_path2 = os.path.join(current, folder_name, file_name2)
full_path3 = os.path.join(current, folder_name, file_name3)
new_dict = {}
with open (full_path1, 'rt', encoding='utf-8') as file1, open (full_path2, 'rt', encoding='utf-8') as file2, open (full_path3, 'rt', encoding='utf-8') as file3:
    res1 = len(file1.readlines())
    res2 = len(file2.readlines())
    res3 = len(file3.readlines())
    print(res1)
    new_dict = {'1.txt': res1, '2.txt': res2, '3.txt': res3}
    print(new_dict)
    sorted_dict = dict(sorted(new_dict.items(), key=itemgetter(1)))
    x = 1
    for name in sorted_dict:
        print(name)
        print(x)
        x += 1
        i = 0
        while i < sorted_dict.get(name): 
            i += 1
            print(f'Строка номер {i} файла номер {name[0]}')
# with open (full_path2, 'rt', encoding='utf-8') as file:
#     res = file.readlines()
#     print(len(res))
# with open (full_path3, 'rt', encoding='utf-8') as file:
#     res = file.readlines()
#     print(len(res))