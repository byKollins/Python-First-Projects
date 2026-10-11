import random

def save_game():
    with open("save.txt", "w") as file:
        file.write(",".join(backpack))
        print("Данный сохранены")

def load_game():
    with open("save.txt", "r") as file:
        return file.read().split(",")

hero_hp = 100
monstr_hp = 500
backpack = load_game()

def calculate_damage(uron):
    results = uron
    return results

def show_backpack():
    print("Что у нас тут: ")
    for item in backpack:
        print("Во есть: " + item)
    print("Сколько барахла в сумке: " + str(len(backpack)))


while True:
    print("Твое ХП: " + str(hero_hp) + "/ ХП Монстра: " + str(monstr_hp))
    action = input("Что ты выберишь (1-Драться, 2-Открыть сумку, 3-Трусливо сбежать!: ")

    if action == "1":
        print("Мудрое решение")
        uron = int(input("Ударить на: "))
        damage = uron
        monstr_hp = monstr_hp - damage
        print("Ударил на: " + str(damage) + " урона")

        if monstr_hp <= 0:
           backpack.append("Голова гоблина")
           print("Ты получил голову гоблина!")
           print("Гоблин умер")
           save_game()
           break

        else:
            monstr_damage = random.randint(5,25)
            hero_hp = hero_hp - monstr_damage
            print("Гоблин ударил на: " + str(monstr_damage) + " урона")

            if hero_hp <= 0:
                print("Сударь умер")
                break

    elif action == "2":
        show_backpack()

    elif action == "3":
        show_backpack()
        print("Не знал что вы трусливы")
        save_game()
        break