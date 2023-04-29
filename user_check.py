import json
import time
import os

users = {}

true_success = 0

def load_accs():
    global users
    with open('users.json', encoding="utf-8") as users_file:
        users = json.load(users_file)


def save():
    global users
    with open('users.json', 'w', encoding="utf-8") as outfile:
        json.dump(users, outfile)


def user_check():
    global true_success
    success = 0
    tries = 0
    while tries < 3 and success < 1:
        login = input("Введите ваш логин: ")
        password = input("Введите ваш пароль: ")
        for i in users['users']:
            if login in i:
                if password == i[login]:
                    print('Авторизация прошла успешно.')
                    success = 1
                    true_success = 1
            if login not in i or not password == i[login]:
                tries += 1
                if tries == 3:
                    print("Авторизация не удалась.Попробуйте позже.")
                    time.sleep(10)
                    break
                print("Неправильный логин или пароль. Попробуйте еще раз.")


def regester():
    global users
    print("Регистрация в умном кошельке")
    new_login = input('Введите логин для аккаунта: ')
    new_password = input("Введите пароль для аккаунта: ")
    for i in users['users'][0]:
        if new_login in i:
            print("Логин уже занят. Измените логин и попробуйте снова.")
            break
        elif new_login not in i:
            r = users['users'][0]
            r[new_login] = new_password
            os.system('cls')
            print('Логин и пароль успешно приняты. Сохраняю.')
            time.sleep(1)
            os.system('cls')
            print('Логин и пароль успешно приняты. Сохраняю..')
            time.sleep(1)
            os.system('cls')
            print('Логин и пароль успешно приняты. Сохраняю...')
            os.system('cls')
    save()




load_accs()

regester()