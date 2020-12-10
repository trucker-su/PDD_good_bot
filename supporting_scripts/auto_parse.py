import pyautogui as pg
from time import sleep

#print(pg.position())

def add_photo_to_telegram():
    pg.click(322, 131)  # выбрать первую фотку
    pg.typewrite(["enter"])
    sleep(1)
    pg.typewrite(["enter"])
    sleep(7)
    pg.click(558, 703)   # открыть выбор фото
    sleep(2)
    pg.click(322, 131)  # выбрать первую фотку
    pg.typewrite(["delete"])
    sleep(5)


pg.click(558, 703)   # открыть выбор фото

for el in range(562):
    add_photo_to_telegram()

print('Поздравляю! Загрузка фотографий в телеграм окончена!')

