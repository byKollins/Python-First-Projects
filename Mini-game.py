name = input("Назавись сударь: ")

backpack = ["меч", "щит", "падарожник"]

def calculate_damage(uron):
    results = uron
    return results

def game_ower(hero_name, reason):
    print("Эх ты, умер ")
    print("Судрь " + hero_name + " Больше не живой ")
    print("Ты: " + reason)
    print("Да уж, грутсно... ")

def show_backpack():
    print("Что у нас тут: ")
    for item in backpack:
        print("Во есть: " + item)
    print("Сколько барахла в сумке: " + str(len(backpack)))

while True:
    HP = int(input("Введите здоровье героя: "))

    if HP <= 0:
        game_ower(name, "Умер")
        break

    elif HP <= 25:
        print("Сударь был ранен, хоть бы был падарожник...")
        if "падарожник" in backpack:
            print("Ура сударь будет стоять дальше!")
            HP = HP + 50
            backpack.remove("падарожник")
            print("Теперь у нас здаровья: " + str(HP))

        else:
            print("Эх тыж, нет падарожника...")

    elif HP == 100:
            print("А ты живучий, на медальку")
            backpack.append("Медаль")
            print("Сударь заработал медаль!")

    elif HP == 50:
        print("Герой ранен, но не смертельно")

    elif HP == 666:
        show_backpack()

    elif HP == 999:
        print("---Файт---")
        uron = int(input("Ударить на: "))
        damage = uron
        print("Сударь ударил врага на: " + str(damage) + " урона")

    else:
        print("Сударь как бы есть, но и как бы нету")

    print("Сколько барахла в сумке: " + str(len(backpack)))
    print("Что у нас тут: " + str(backpack))
    print("Давай по новай Миша все хуйня")
