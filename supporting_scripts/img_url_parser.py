from db import db

new_db = db.copy()
file_name = 'img_id.txt'

with open(file_name, encoding='utf-8', mode='r', newline='') as f:
    stroka = f.readlines()

new_stroka = list(map(lambda x: x.replace('\ufeff', '').replace('\n', ''), stroka))

for el in new_db:
    if el['img'] is not None:
        el['img'] = new_stroka.pop(0)

for el in new_db:
    print(f'{el},')