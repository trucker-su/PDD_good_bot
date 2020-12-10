import re

file_name = 'bilet.txt'

with open(file_name, encoding='utf-8', mode='r', newline='') as f:
    stroka = f.read()

result = re.sub(r'Билет №\d{1,3}', '', stroka)
result = re.sub(r'http.+', '', result)
result = re.split(r'Вопрос №\d{1,3}', result)
res = []
for el in result:
    el = el.replace('\r', '')
    el = el.replace('\n', ' ')
    res.append(el)
res.remove('\ufeff ')

def len_check_error(answer):
	if len(answer) > 100:
		print('слишком длинный ответ, нужно укоротить!')

db = []

for el in res:

    dictionary = {'question': None, 'correct_answer': None, 'all_answers': None, 'img': None,
                  'explanation': 'Не верно!'}
    answer_list = []

    question = re.search(r'.+ Варианты ответа:', el).group()
    question = re.sub(r' Варианты ответа:', '', question)
    question = question.strip()
    question = re.sub(r'\.$', '', question)
    dictionary['question'] = question

    answer_1 = re.search(r'1\..+2\.', el).group()
    answer_1 = re.sub(r'^1\. ', '', answer_1)
    answer_1 = re.sub(r' 2\.$', '', answer_1)
    answer_1 = answer_1.strip()
    answer_1 = re.sub(r'\.$', '', answer_1)
    answer_list.append(answer_1)
    len_check_error(answer_1)

    try:
        answer_2 = re.search(r'2\..+3\.', el).group()
        answer_2 = re.sub(r'^2\. ', '', answer_2)
        answer_2 = re.sub(r' 3\.$', '', answer_2)
        answer_2 = answer_2.strip()
        answer_2 = re.sub(r'\.$', '', answer_2)
    except AttributeError:
        answer_2 = re.search(r'2\..+ Правильный ответ:', el).group()
        answer_2 = re.sub(r'^2\. ', '', answer_2)
        answer_2 = re.sub(r' Правильный ответ:', '', answer_2)
        answer_2 = answer_2.strip()
        answer_2 = re.sub(r'\.$', '', answer_2)
    answer_list.append(answer_2)
    len_check_error(answer_2)

    try:
        answer_3 = re.search(r'3\..+4\.', el).group()
        answer_3 = re.sub(r'^3\. ', '', answer_3)
        answer_3 = re.sub(r' 4\.$', '', answer_3)
        answer_3 = answer_3.strip()
        answer_3 = re.sub(r'\.$', '', answer_3)
        answer_list.append(answer_3)
        len_check_error(answer_3)
    except AttributeError:
        try:
            answer_3 = re.search(r'3\..+ Правильный ответ:', el).group()
            answer_3 = re.sub(r'^3\. ', '', answer_3)
            answer_3 = re.sub(r' Правильный ответ:', '', answer_3)
            answer_3 = answer_3.strip()
            answer_3 = re.sub(r'\.$', '', answer_3)
            answer_list.append(answer_3)
            len_check_error(answer_3)
        except AttributeError:
            pass

    try:
        answer_4 = re.search(r'4\..+5\.', el).group()
        answer_4 = re.sub(r'^4\. ', '', answer_4)
        answer_4 = re.sub(r' 5\.$', '', answer_4)
        answer_4 = answer_4.strip()
        answer_4 = re.sub(r'\.$', '', answer_4)
        answer_list.append(answer_4)
        len_check_error(answer_4)
    except AttributeError:
        try:
            answer_4 = re.search(r'4\..+ Правильный ответ:', el).group()
            answer_4 = re.sub(r'^4\. ', '', answer_4)
            answer_4 = re.sub(r' Правильный ответ:', '', answer_4)
            answer_4 = answer_4.strip()
            answer_4 = re.sub(r'\.$', '', answer_4)
            answer_list.append(answer_4)
            len_check_error(answer_4)
        except AttributeError:
            pass

    try:
        answer_5 = re.search(r'5\..+ Правильный ответ:', el).group()
        answer_5 = re.sub(r'^5\. ', '', answer_5)
        answer_5 = re.sub(r' Правильный ответ:', '', answer_5)
        answer_5 = answer_5.strip()
        answer_5 = re.sub(r'\.$', '', answer_5)
        answer_list.append(answer_5)
        len_check_error(answer_5)
    except AttributeError:
        pass

    dictionary['all_answers'] = answer_list

    correct_answer = re.search(r'Правильный ответ:.+', el).group()
    correct_answer = re.sub(r'Правильный ответ: ', '', correct_answer)
    correct_answer = correct_answer.strip()
    correct_answer = re.sub(r'\.$', '', correct_answer)
    dictionary['correct_answer'] = correct_answer

    db.append(dictionary)

for el in db:
    print(f'{el},')

# скопировать результат в db = []
# после, проверить длину ответов. не должно превышать 100 символов