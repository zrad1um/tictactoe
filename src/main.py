from pyfiglet import Figlet
import inquirer
from colorama import init, Fore
from game import TicTacToe
from constants import BOARD_SIZE, WIN_CONDITION

# ИНИЦИАЛИЗАЦИЯ ЦВЕТНОГО ВЫВОДА
init(autoreset=True)

def show_welcome():
    """Отображает приветственное сообщение"""
    f = Figlet(font="slant")
    print(Fore.CYAN + f.renderText("Tic Tac Toe"))
    print(Fore.YELLOW + f"Версия {BOARD_SIZE}x{BOARD_SIZE} | Победная серия: {WIN_CONDITION}")
    print(Fore.LIGHTBLACK_EX + "-" * 50)

def show_menu():
    """Отображает главное меню с настройками"""
    questions = [
        inquirer.List(
            "action",
            message="Выберите действие",
            choices = [
                ("Начать игру", "play"),
                ("Настройки", "settings"),
                ("Выход", "exit")
            ],
            carousel=True
        )
    ]
    return inquirer.prompt(questions)["action"]

def show_settings():
    """Меню настроек"""
    questions = [
        inquirer.List(
            "setting",
            message="Выберите настройку",
            choices=[
                (f"Размер поля (текущий: {BOARD_SIZE}×{BOARD_SIZE})", "board_size"),
                (f"Победная серия (текущая: {WIN_CONDITION})", "win_condition"),
                ("Назад", "back")
            ]
        )
    ]
    return inquirer.prompt(questions)["setting"]

def change_board_size():
    """Изменение размера игрового поля"""
    sizes = [(f"{size}x{size}", size) for size in range(3, 13)]
    questions = [
        inquirer.List(
            "size",
            message="Выберите размер поля",
            choices=sizes
        )
    ]
    return inquirer.prompt(questions)["size"]

def change_win_condition():
    """Изменение условия победы"""
    questions = [
        inquirer.Text(
            "condition",
            message=f"Введите длину серии (3-{BOARD_SIZE})",
            validate=lambda _, x: x.isdigit() and 3 <= int(x) <= BOARD_SIZE
        )
    ]
    return int(inquirer.prompt(questions)["condition"])

def main():
    show_welcome()

    while True:
        choice = show_menu()

        if choice == "play":
            game = TicTacToe()
            game.run()
        elif choice == "settings":
            while True:
                setting = show_settings()
                if setting == "board_size":
                    new_size = change_board_size()
                    print(f"Размер поля изменен на {new_size}×{new_size}")
                    # Здесь нужно реализовать изменение BOARD_SIZE
                elif setting == "win_condition":
                    new_condition = change_win_condition()
                    print(f"Победная серия изменена на {new_condition}")
                    # Здесь нужно реализовать изменение WIN_CONDITION
                else:
                    break
        else:
            print(Fore.GREEN + "\nСпасибо за игру! До свидания!")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\nИгра прервана пользователем")
    except Exception as e:
        print(Fore.RED + f"\nПроизошла ошибка: {e}")
