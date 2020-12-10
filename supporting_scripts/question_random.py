from db import db
import random

question = random.choice(db)
print(question['question'])
for el in question['all_answers']:
	print(el)
t = input('Посмотреть ответ: ')
if t:
	print(question['correct_answer'])