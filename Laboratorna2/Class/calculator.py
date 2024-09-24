class Calculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.operator = ''

    def get_operator(self):
        self.operator = input("Виберіть операцію (+, -, *, /, ^, √, %): ").strip()
        return self.operator

    def get_numbers(self):
        if self.operator == '√':
            self.num1 = float(input("Введіть число для обчислення квадратного кореня: "))
            self.num2 = None
        else:
            self.num1 = float(input("Введіть перше число: "))
            self.num2 = float(input("Введіть друге число: "))
        return self.num1, self.num2

    def calculate(self):
        try:
            match self.operator:
                case '+':
                    result = self.num1 + self.num2
                case '-':
                    result = self.num1 - self.num2
                case '*':
                    result = self.num1 * self.num2
                case '/':
                    result = self.num1 / self.num2 if self.num2 != 0 else float('inf')  # Захист від ділення на нуль
                case '^':
                    result = self.num1 ** self.num2
                case '√':
                    result = self.num1 ** 0.5
                case '%':
                    result = self.num1 % self.num2
                case _:
                    print("Неправильний оператор!")
                    return None

            result = round(result, 2)  # Результат за замовчуванням округлюється до 2 знаків
            return result
        except (ZeroDivisionError, ValueError) as e:
            print(f"Помилка: {e}")
            return None
