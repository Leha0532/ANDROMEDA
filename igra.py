user_name = input("Вашe имя: ")
from random import randint

x = randint(1, 15)
attempt = 0

while True:
    print("Я загадал число от 1 до 15, угадай его :)")
    user_num = int(input(user_name+", Ваш Вариант: "))
    attempt += 1
    if user_num == x:
        print(f"{user_name}, Ты угадал число, молодец !\nКоличество твоих попыток: {attempt}\nСпасибо за игру!")
        break
    elif user_num > x:
        print("Моё число меньше.")
    elif user_num < x:
        print("Моё число больше")