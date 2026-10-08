inventory = {
    "Мячи": 10,
    "Гантели": 8,
    "Скакалки": 5,
    "Коврики": 12
}

while True:
    print("\n1 - Показать инвентарь")
    print("2 - Добавить инвентарь")
    print("3 - Выдать инвентарь")
    print("4 - Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        for item, count in inventory.items():
            print(item, "-", count)

    elif choice == "2":
        item = input("Название инвентаря: ")
        count = int(input("Количество: "))
        inventory[item] = inventory.get(item, 0) + count
        print("Инвентарь добавлен!")

    elif choice == "3":
        item = input("Название инвентаря: ")
        count = int(input("Количество: "))

        if item in inventory and inventory[item] >= count:
            inventory[item] -= count
            print("Инвентарь выдан!")
        else:
            print("Недостаточно инвентаря!")

    elif choice == "4":
        print("Программа завершена.")
        break

    else:
        print("Неверный выбор!")
