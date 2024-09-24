from Interface.user_interface import display_main_menu, get_user_choice
from Interface.menu_actions import handle_calculation, handle_settings, handle_memory

def main():
    while True:
        display_main_menu()  # Вивести головне меню
        choice = get_user_choice()  # Отримати вибір користувача

        if choice == '1':
            handle_calculation()
        elif choice == '2':
            handle_settings()
        elif choice == '3':
            handle_memory()
        elif choice == '4':
            break
        else:
            print("Неправильний вибір! Спробуйте ще раз.")

if __name__ == "__main__":
    main()
