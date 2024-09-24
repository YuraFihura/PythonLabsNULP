import App_settings.settings as settings

def change_decimal_places():
    try:
        decimal_places = int(input("Введіть кількість десяткових розрядів для результату: "))
        if decimal_places >= 0:
            settings.DECIMAL_PLACES = decimal_places
            print(f"Кількість десяткових розрядів змінено на {settings.DECIMAL_PLACES}.")
        else:
            print("Кількість десяткових розрядів повинна бути не від'ємною!")
    except ValueError:
        print("Введіть ціле число!")


def settings_menu():
    print("\nНалаштування:")
    print("1. Змінити кількість десяткових розрядів")
    print("2. Вийти з налаштувань")

    choice = input("Виберіть дію (1-2): ")
    if choice == '1':
        change_decimal_places()
    elif choice == '2':
        return
    else:
        print("Неправильний вибір, спробуйте ще раз.")
        settings_menu()
