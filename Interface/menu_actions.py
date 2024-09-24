from Functions.operations import get_operator
from Interface.user_input import get_numbers
from Interface.user_settings import settings_menu
from Class.calculator import Calculator
from Logs.history import History
from Class.memory import Memory
import App_settings.settings as settings

# Ініціалізація об'єктів
calc = Calculator()
history = History()
memory = Memory()

def handle_calculation():
    operator = get_operator()
    num1, num2 = get_numbers(operator)

    try:
        match operator:
            case '+':
                result = calc.add(num1, num2)
            case '-':
                result = calc.subtract(num1, num2)
            case '*':
                result = calc.multiply(num1, num2)
            case '/':
                result = calc.divide(num1, num2)
            case '^':
                result = calc.power(num1, num2)
            case '√':
                result = calc.sqrt(num1)
            case '%':
                result = calc.mod(num1, num2)
            case _:
                print("Неправильний оператор!")
                return

        result = round(result, settings.DECIMAL_PLACES)
        print(f"Результат: {result}")
        history.add_record(f"{num1} {operator} {num2 if num2 is not None else ''}", result)

        save_memory = input("Зберегти результат в пам'ять? (так/ні): ").lower()
        if save_memory == 'так':
            memory.save_to_memory(result)

    except (ZeroDivisionError, ValueError) as e:
        print(f"Помилка: {e}")

def handle_settings():
    settings_menu()  # Відкриває меню налаштувань

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
