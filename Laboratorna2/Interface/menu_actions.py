from Class.calculator import Calculator
from Interface.user_settings import change_decimal_places
from Logs.history import History
from Class.memory import Memory
import App_settings.settings as settings

calc = Calculator()
history = History()
memory = Memory()


def handle_calculation():
    while True:  # Цикл для повторного виконання обчислень
        operator = calc.get_operator()
        num1, num2 = calc.get_numbers()

        result = calc.calculate()
        if result is not None:
            print(f"Результат: {result}")
            history.add_record(f"{num1} {operator} {num2 if num2 is not None else ''}", result)

            save_memory = input("Зберегти результат в пам'ять? (так/ні): ").lower()
            if save_memory == 'так':
                memory.save_to_memory(result)

            # Запит на продовження
            continue_calculation = input("Хочете виконати ще одне обчислення? (так/ні): ").lower()
            if continue_calculation != 'так':
                print("Дякуємо за використання програми! Вихід з програми.")
                break  # Вихід з циклу, щоб завершити програму


def handle_settings():
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
        handle_settings()  # Виклик знову для повторного вибору


def handle_memory():
    print("\nПам'ять:")
    print("1. Показати значення з пам'яті")
    print("2. Очистити пам'ять")
    print("3. Додати значення до пам'яті вручну")
    print("4. Вийти з меню пам'яті")

    memory_choice = input("Виберіть дію (1-4): ")

    if memory_choice == '1':
        memory.recall_memory()
    elif memory_choice == '2':
        memory.clear_memory()
    elif memory_choice == '3':
        try:
            manual_value = float(input("Введіть значення для збереження в пам'ять: "))
            memory.save_to_memory(manual_value)
        except ValueError:
            print("Невірне значення! Введіть число.")
    elif memory_choice == '4':
        return
    else:
        print("Неправильний вибір!")
