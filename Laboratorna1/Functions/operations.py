def get_operator():
    operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
    if operator in ['+', '-', '*', '/', '^', '√', '%']:
        return operator
    else:
        print("Неправильний оператор! Спробуйте ще раз.")
        return get_operator()
