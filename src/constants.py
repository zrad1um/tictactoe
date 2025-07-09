from colorama import Fore, Back, Style

# ======== colors and styles =========
PLAYER_COLORS = {
    "X": Fore.LIGHTGREEN_EX, # green for X
    "O": Fore.LIGHTBLUE_EX, # lightblue for O
    "DRAW": Fore.LIGHTYELLOW_EX, # yellow for draw
    "ERROR": Fore.LIGHTRED_EX, # red for errors
    "PROMPT": Fore.CYAN, # cyan for prompts
    "BOARD": Fore.LIGHTWHITE_EX, # board color
    "GRID": Fore.LIGHTBLACK_EX # board lines color 
}

# ======== field settings ========
BOARD_SIZE = 12
WIN_CONDITION = 5
CELL_EMPTY = " "

CELLS = {
    "X": "X", # X symbol
    "O": "O", # O symbol
    "BORDER": "│", 
    "LINE_H": "─",
    "CROSS": "┼",
    "CORNER_TL": "┌",
    "CORNER_TR": "┐",
    "CORNER_BL": "└",
    "CORNER_BR": "┘"
}

# ===== ASCII ГРАФИКА =====
TITLE_ART = r"""
  _______   _____    _____   _______   _____    _____    _____  
 |__   __| |_   _|  / ____| |__   __| |_   _|  / ____|  / ____| 
    | |      | |   | |         | |      | |   | |      | |      
    | |      | |   | |         | |      | |   | |      | |      
    | |     _| |_  | |____     | |     _| |_  | |____  | |____  
    |_|    |_____|  \_____|    |_|    |_____|  \_____|  \_____| 
"""

MENU_ART = [
    "╔════════════════╗",
    "║  TICTAC MAZAFAKA BITCH  ║",
    "╚════════════════╝"
]

# interface text
PROMPTS = {
    "MOVE": f"{PLAYER_COLORS['PROMPT']}Введите номер клетки (1-{BOARD_SIZE**2}): {Style.RESET_ALL}",
    "INVALID_INPUT": f"{PLAYER_COLORS['ERROR']}Ошибка! Введите число от 1 до {BOARD_SIZE**2}.{Style.RESET_ALL}",
    "CELL_TAKEN": f"{PLAYER_COLORS['ERROR']}Клетка уже занята!{Style.RESET_ALL}",
    "WIN": f"{PLAYER_COLORS['PROMPT']}Игрок {{player}} победил!{Style.RESET_ALL}",
    "DRAW": f"{PLAYER_COLORS['DRAW']}Ничья!{Style.RESET_ALL}"
}

# ======== FIELD GENERATION ========
def generate_board_template():
    # upper border
    header = ["   " + CELLS["CORNER_TL"] + (CELLS["LINE_H"]*3 + CELLS["CROSS"])*(BOARD_SIZE-1) + CELLS["LINE_H"]*3 + CELLS["CORNER_TR"]]
    
    # Строки с номерами
    cell_number = 1
    for row in range(BOARD_SIZE):
        # Номера клеток (с выравниванием)
        numbers = []
        for col in range(BOARD_SIZE):
            num_str = f"{cell_number:2d}"
            numbers.append(num_str)
            cell_number += 1
        num_line = " " + " ".join(numbers)
        
        # Линии разделители
        if row < BOARD_SIZE-1:
            divider = "   " + CELLS["BORDER"] + ("   " + CELLS["BORDER"])*(BOARD_SIZE-1)
        
        header.append(num_line)
        if row < BOARD_SIZE-1:
            header.append(divider)
    
    # Нижняя граница
    footer = "   " + CELLS["CORNER_BL"] + (CELLS["LINE_H"]*3 + CELLS["CROSS"])*(BOARD_SIZE-1) + CELLS["LINE_H"]*3 + CELLS["CORNER_BR"]
    header.append(footer)
    
    return "\n".join(header)

BOARD_TEMPLATE = generate_board_template()

# Инициализация colorama
def init_colors():
    from colorama import init
    init(autoreset=True)

# Тестирование отображения
if __name__ == "__main__":
    init_colors()
    print(TITLE_ART)
    print(PROMPTS["MOVE"])
    print(f"{PLAYER_COLORS['GRID']}{BOARD_TEMPLATE}{Style.RESET_ALL}")
    print(f"\nПример хода: {PROMPTS['MOVE']}42")