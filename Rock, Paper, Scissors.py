import random

beats = {
    "Камень": "Ножницы",
    "Ножницы": "Бумага",
    "Бумага": "Камень",
}

action = list(beats)

wins_computer = 0
wins_player = 0
draws = 0

def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif beats[player] == computer:
        return "wins_player"
    else:
        return "wins_computer"

while True:

    player = input("Чем будете ходить: ").strip().capitalize()
    computer = random.choice(action)

    if player == "Выход":
        print("Спасибо за игру!")
        print(f"Вы выиграли: {wins_player} раз.")
        print(f"Вы проиграли: {wins_computer} раз.")
        print(f"Сыграли в ничью: {draws} раз.")
        break

    if player in action:
        print(f"Вы выбрали: {player}")
    else:
        print("Действия нет, введите снова!")
        continue

    result = get_winner(player, computer)

    if result == "draw":
        print(f"Ничья! Компьютер выбрал {computer} ")
        draws += 1
    elif result == "wins_player":
        print(f"Вы выиграли! Компьютер выбрал {computer} ")
        wins_player += 1
    else:
        print(f"Вы проиграли! Компьютер выбрал {computer} ")
        wins_computer += 1