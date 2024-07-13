'''
Задание 2
'''


import collections

pets = {
    1: {
        "Кличка": "Мухтар",
        "Вид питомца": "Собака",
        "Возраст питомца": 9,
        "Имя владельца": "Павел"
    },
    2: {
        "Кличка": "Каа",
        "Вид питомца": "желторотый питон",
        "Возраст питомца": 19,
        "Имя владельца": "Саша"
    }
}


def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False


def get_suffix(age):
    if age % 10 == 1 and age != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and (age < 10 or age >= 20):
        return "года"
    else:
        return "лет"


def pets_list():
    for ID, pet in pets.items():
        print(f"({ID}) {pet['Кличка']}")


def create():
    last = collections.deque(pets, maxlen=1)[0]
    new_id = last + 1 if pets else 1

    pet_name = input("Введите кличку питомца: ")
    pet_type = input("Введите вид питомца: ")
    pet_age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")

    pets[new_id] = {
        "Кличка": pet_name,
        "Вид питомца": pet_type,
        "Возраст питомца": pet_age,
        "Имя владельца": owner_name
    }

    print(f"Новый питомец с ID {new_id} успешно добавлен!")


def read():
    pet_id = int(input("Введите ID питомца: "))
    pet = get_pet(pet_id)
    if pet:
        print(
            f"Это {pet['Вид питомца']} по кличке \"{pet['Кличка']}\". Возраст питомца: {pet['Возраст питомца']} {get_suffix(pet['Возраст питомца'])}. Имя владельца: {pet['Имя владельца']}")
    else:
        print(f"Питомец с ID {pet_id} не найден.")


def update():
    pet_id = int(input("Введите ID питомца для обновления: "))
    pet = get_pet(pet_id)
    if pet:
        new_name = input(f"Введите новую кличку (старая: {pet['Кличка']}): ")
        new_type = input(f"Введите новый вид (старый: {pet['Вид питомца']}): ")
        new_age = int(input(f"Введите новый возраст (старый: {pet['Возраст питомца']}): "))
        new_owner = input(f"Введите новое имя владельца (старое: {pet['Имя владельца']}): ")

        pet['Кличка'] = new_name
        pet['Вид питомца'] = new_type
        pet['Возраст питомца'] = new_age
        pet['Имя владельца'] = new_owner

        print(f"Информация о питомце с ID {pet_id} успешно обновлена.")
    else:
        print(f"Питомец с ID {pet_id} не найден.")


def delete():
    pet_id = int(input("Введите ID питомца для удаления: "))
    if pet_id in pets:
        del pets[pet_id]
        print(f"Питомец с ID {pet_id} успешно удален.")
    else:
        print(f"Питомец с ID {pet_id} не найден.")


while True:
    command = input("Введите команду (create, read, update, delete, list, stop): ")

    if command == 'create':
        create()
    elif command == 'read':
        read()
    elif command == 'update':
        update()
    elif command == 'delete':
        delete()
    elif command == 'list':
        pets_list()
    elif command == 'stop':
        print("Работа программы завершена.")
        break
    else:
        print("Неизвестная команда. Попробуйте еще раз.")
