import json


#Функции работы с файлом

def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


#Остальные функции

def get_task_number(count):
    while True:
        try:
            number = int(input("Введите номер задачи: "))
        except ValueError:
            print("Нужно ввести число!")
            continue
        if number < 1 or number > count:
            print(f"Числа от 1 до {count}!")
            continue
        return number


def show_tasks(tasks):
    for number, task in enumerate(tasks, start=1):
        title = task["title"]
        if task["done"]:
            mark = "[x]"
        else:
            mark = "[ ]"
        print(f"{number}. {mark} {title}")


#Основная программа

tasks = load_tasks()

while True:
    print("---Список задач---")
    print("1 - Показать задачи")
    print("2 - Добавить задачу")
    print("3 - Удалить задачу")
    print("4 - Отметить задачу выполненной")
    print("5 - Выход")

    select = input("Что сделать: ")

    if select == "1":
        if not tasks:
            print("Задач нет!")
        else:
            show_tasks(tasks)

    elif select == "2":
        add = input("Добавить задачу: ").strip()
        if not add:
            print("Задача не может быть пустой!")
        else:
            tasks.append({"title": add, "done": False})
            save_tasks(tasks)
            print(f"Задача {add} успешно добавлена.")

    elif select == "3":
        if not tasks:
            print("Задач нет!")
        else:
            show_tasks(tasks)
            delete = get_task_number(len(tasks))
            removed = tasks.pop(delete - 1)
            save_tasks(tasks)
            print(f"Задача {removed['title']} удалена!")

    elif select == "4":
        if not tasks:
            print("Задач нет!")
        else:
            show_tasks(tasks)
            number = get_task_number(len(tasks))
            tasks[number - 1]["done"] = True
            save_tasks(tasks)
            print("Задача отмечена выполненной!")

    elif select == "5":
        print("До свидания")
        break

    else:
        print("Нет такого пункта!")