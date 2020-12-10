from aiogram import Bot, Dispatcher, executor, types
from config import *
from db import db
import random
import pymongo as pymongo

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


client = pymongo.MongoClient(MongoDB_key)
mongo_db = client.test
users_data_base = mongo_db.pdd_bot


def id_seach(simple_user_id):
    id_collection = []
    for item in users_data_base.find():
        id_collection.append(item["_id"])
    if simple_user_id in id_collection:
        return True
    else:
        return False


def new_client(user_id, user_name):
    if id_seach(user_id):
        pass
    else:
        users_data_base.insert_one({
            "_id": user_id,
            "user_name": user_name
        })


def db_stat():
    all_date_base = users_data_base.find()
    id_collection = []
    for item in all_date_base:
        id_collection.append(item["_id"])
    return len(id_collection)


class RandomQuestion:
    def __init__(self, question_block=None, question=None, options=None, correct_option_id=None, explanation=None, image=None):
        self.question_block = question_block
        self.question = question
        self.options = options
        self.correct_option_id = correct_option_id
        self.explanation = explanation
        self.image = image

    def get_question(self):
        self.question_block = random.choice(db)
        self.question = self.question_block['question']
        random.shuffle(self.question_block['all_answers'])
        self.options = self.question_block['all_answers']
        self.correct_option_id = self.question_block['all_answers'].index(self.question_block['correct_answer'])
        self.explanation = self.question_block['explanation']
        self.image = self.question_block['img']


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    if message.from_user.id == admin_id:
        await message.answer('Ты админ')
    question = RandomQuestion()
    question.get_question()
    if question.image:
        await bot.send_photo(message.from_user.id, question.image)
    new_client(message.from_user.id, message.from_user.full_name)
    await bot.send_poll(message.chat.id,
                        type='quiz',
                        is_anonymous=False,
                        is_closed=False,
                        question=question.question,
                        options=question.options,
                        correct_option_id=question.correct_option_id,
                        explanation=question.explanation)


@dp.message_handler(commands=["statistics"])
async def cmd_stat(message: types.Message):
    if message.from_user.id == admin_id:
        number_of_users = db_stat()
        await message.answer(f'Зарегестрировано человек: {number_of_users}')
    else:
        await message.answer('Тут записано сколько человек пользуются ботом.\nТак как ты не админ, эту информация '
                             'для тебя не доступна.')
        

@dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    await message.answer('Телеграм налагает ограничения на количество символов в тексте при составлении опросов и '
                         'викторин.\nПоэтому некоторые слова в ответах были заменены на более короткие аналоги, '
                         'например:\nтранспорное средство -> транспорт -> авто\nА конструкции вида дом/дорога/машина '
                         '- означают:\nдом, дорога, машина')


# text = 'Автобусы, троллейбусы/трамваи,едущие по установленному маршруту с обозначенными местами'
#
#
# @dp.message_handler(commands=["test"])
# async def cmd_test(message: types.Message):
#     if message.from_user.id == admin_id:
#         await message.answer('Ты админ')
#     question = RandomQuestion()
#     question.get_question()
#     question.image = 'AgACAgIAAxkBAAIGMl_Pqwgdr5BhW0Y_zskt_xMB18b-AAIksTEbt7F4ShqY-WgVM1SZkewXmC4AAwEAAwIAA3kAA_4jBAABHgQ'
#     if question.image:
#         await bot.send_photo(message.from_user.id, question.image)
#     await bot.send_poll(message.chat.id,
#                         type='quiz',
#                         is_anonymous=False,
#                         is_closed=False,
#                         question='Верно ли утверждение: Требование "Уступить дорогу" означает что Вы не должны '
#                                  'возобновлять или продолжать движение, осуществлять какой либо маневр, '
#                                  'если это может вынудить других участников движения, имеющих по отношению к Вам '
#                                  'преимущество, изменить направление движения или скорость',
#                         options=[text, text, text],
#                         correct_option_id=question.correct_option_id,
#                         explanation='Нельзя возобновлять/продолжать движение/осуществлять маневр, если это вынудит '
#                                     'других водителей, имеющих по отношению к Вам преимущество, изменить направление '
#                                     'движения или скорость')


@dp.poll_answer_handler()
async def handle_poll_answer(quiz_answer: types.PollAnswer):
    question = RandomQuestion()
    question.get_question()
    if question.image:
        await bot.send_photo(quiz_answer.user.id, question.image)
    await quiz_answer.bot.send_poll(quiz_answer.user.id,
                                    type='quiz',
                                    is_anonymous=False,
                                    is_closed=False,
                                    question=question.question,
                                    options=question.options,
                                    correct_option_id=question.correct_option_id,
                                    explanation=question.explanation)


# @dp.message_handler(content_types=['photo'])
# async def handle_docs_photo(message: types.Message):
#     for el in message.photo:
#         print(el.file_id)
#     with open('img_id.txt', encoding='utf-8', mode='a', newline='') as f:
#         f.write(message.photo[0].file_id + '\n')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
