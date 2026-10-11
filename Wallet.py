def save_wallet():
    with open("save_wallet.txt", "w") as file:
        string_expenses = ",".join([str(x) for x in expenses])
        file.write(string_expenses)
        print("Список сохранён")

def load_wallet():
    with open("save_wallet.txt", "r") as file:
        data = file.read()
        if data == "" or data.strip() == "":
            return []
        return [int(x) for x in data.split(",")]

expenses = load_wallet()

while True:
    print("---Мой кашелёк---")
    print("1 - Добавить покупку")
    print("2 - Показать все расходы")
    print("3 - Посчитать общую сумму расходов")
    print("4 - Сохранить и выйти.")

    action = input("Выберите действие: ")

    if action == "1":
        print("---Добавить покупку---")
        product = input("Что купили: " )
        price = int(input("Сколько стоит: "))
        tovar = product
        bay = price
        expenses.append(price)
        print("• " + str(tovar) + " за " + str(bay) + " Рублей, успешно добавлен")

    elif action == "2":
        print("---Мои расходы---")
        for price in expenses:
            print("• " + str(price) + " Рублей")

    elif action == "3":
        totol = sum(expenses)
        print("---Всего потрачено:" + str(totol) + " Рублей---")

    elif action == "4":
        save_wallet()
        print("До свидания!")
        break