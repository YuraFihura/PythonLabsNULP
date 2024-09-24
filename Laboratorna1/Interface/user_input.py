def get_numbers(operator):
    if operator == '√':
        num1 = float(input("Введіть число для обчислення квадратного кореня: "))
        return num1, None
    else:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        return num1, num2
