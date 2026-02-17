import random

def rock_paper_scissors():
    user_choice = input("Введите ваш выбор (камень, ножницы, бумага): ")
    computer_choice = random.choice(["камень", "ножницы", "бумага"])
    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == "камень" and computer_choice == "ножницы") or (user_choice == "ножницы"
           and computer_choice == "бумага") or (user_choice == "бумага" and computer_choice == "камень"):
        print("Вы победили!")
    else:
        print("Вы проиграли :(")


def guess_the_number():
    computer_choice = random.randint(1, 10)
    while True:
        user_choice = int(input("Введите любое число от 1 до 10: "))
        if user_choice == computer_choice:
            print("Вы угадали!")
            break
        else:
            print("Вы не угадали :( \nПопробуйте еще раз!")
            print()


def main_menu():
    request = int(input("Здравствуйте! \nВыберите игру \n1 - Камень, ножницы, бумага \n2 - Угадай число: "))
    if request == 1:
        rock_paper_scissors()
    elif request == 2:
        guess_the_number()
    else:
        print("Ошибка ввода!")
        request = int(input("Выберите игру \n1 - Камень, ножницы, бумага \n2 - Угадай число: "))

main_menu()








