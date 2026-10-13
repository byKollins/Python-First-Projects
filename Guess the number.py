import random

max_number = 100
max_attempts = 15

def play_game():

    secret = random.randint(1, max_number)
    guesses = []
    attempts = 0

    print("Давай сыграем в игру «Угадай число»!")
    print(f"У тебя есть {max_attempts} попыток!")
    print(f"Я загадал число от 1 до {max_number}")

    while True:
        hero = get_number(max_number)

        if hero in guesses:
            print("Ты уже называл это число!")
            continue

        attempts += 1
        guesses.append(hero)

        left = max_attempts - attempts

        if hero == secret:
            print(f"Угадал за {attempts} попыток!")
            print(f"Твои догадки: {guesses}")
            break

        elif attempts >= max_attempts:
            print(f"Попытки закончились! Я загадал {secret}")
            print(f"Твои догадки: {guesses}")
            break

        elif hero > secret:
            print("Меньше!")

        else:
            print("Больше!")

        print(f"Осталось {left} попыток!")

def get_number(max_number):
    while True:
        try:
            number = int(input("Введите число: "))
        except ValueError:
            print("Нужно ввести число!")
            continue

        if number < 1 or number > max_number:
            print(f"Числа от 1 до {max_number}!")
            continue

        return number

while True:
    play_game()
    answer = input("Сыграть еще раз? (да/нет): ").lower().strip()
    if answer != "да":
        break