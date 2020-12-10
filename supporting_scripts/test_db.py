from db import db

count = 0
for idd, el in enumerate(db):
    try:
        el['all_answers'].index(el['correct_answer'])
    except:
        print(f'Ключ не найден, строка = {idd+1}')
    for op in el['all_answers']:
        if len(op) > 100:
            print(idd + 1, len(op))
            count += 1

print(f'всего дилинных ответов: {count}')

text = 'Управление авто пьяным водителем не имеющим права управления транспортом либо лишенным этого права'
print(f'Размер строки {len(text)}')

