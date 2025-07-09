from colorama import Fore, Style
from constants import PLAYER_COLORS, BOARD_SIZE, WIN_CONDITION, CELLS

def print_board(board):
    """Выводит цветное поле 12х12 с номерами клеток и текущими ходами"""
    # разделительная линия
    def create_divider():
        line = " " + CELLS["CORNER_TL"]
        for i in range(BOARD_SIZE):
            line += CELLS["LINE_H"]*3
            if i < BOARD_SIZE - 1:
                line += CELLS["CROSS"]
        line += CELLS["CORNER_TR"]
        return line
    
    # строка с содержимым клеток
    def create_content_row(row_num):
        # cells numbers
        start = row_num * BOARD_SIZE + 1
        numbers = [f"{n:2d}" for n in range(start, start + BOARD_SIZE)]
        num_line = " " + " ".join(numbers)

        # player symbols
        symbols = []
        for col in range(BOARD_SIZE):
            cell = board[row_num * BOARD_SIZE + col]
            color = PLAYER_COLORS.get(cell, Fore.WHITE)
            symbols.append(f"{color}{cell if cell != ' ' else ' '}{Style.RESET_ALL}")
        
        symbol_line = "   " + CELLS["BORDER"] + (" " + CELLS["BORDER"] + " ").join(symbols)
        
        return num_line + "\n" + symbol_line
    
    # all field building
    output = []
    output.append(create_divider())

    for row in range(BOARD_SIZE):
        output.append(create_content_row(row))
        if row < BOARD_SIZE - 1:
            # линия разделитель между рядами
            divider = " " + CELLS["BORDER"]
            for _ in range(BOARD_SIZE):
                divider += " " + CELLS["BORDER"]
            output.append(divider)
    
    output.append(create_divider().replace(CELLS["CORNER_TL"], CELLS["CORNER_BL"]).replace(CELLS["CORNER_TR"], CELLS["CORNER_BR"]))
    print("\n".join(output))

def check_winner(board):
    """проверяет наличие победителя на поле 12х12"""
    directions = [
        (1, 0), # horizontal
        (0, 1), # vertical
        (1, 1),    # Диагональ ↘
        (1, -1)    # Диагональ ↙
    ]

    def check_line(x, y, dx, dy, symbol):
        """проверяет линию из WIN_CONDITION символов"""
        for _ in range(WIN_CONDITION - 1):
            x += dx
            y += dy
            if x >= BOARD_SIZE or y >= BOARD_SIZE or x < 0 or y < 0:
                return False
            if board[y * BOARD_SIZE + x] != symbol:
                return False
        return True
    
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            cell = board[y * BOARD_SIZE + x]
            if cell == ' ':
                continue

            for dx, dy in directions:
                if check_line(x, y, dx, dy, cell):
                    return cell
                
    return None if ' ' in board else 'DRAW'
        
def validate_input(input_str, board):
    """Проверяет корректность ввода пользователя"""
    try:
        move = int(input_str)
        if not 1 <= move <= BOARD_SIZE ** 2:
            return False, "Введите число от 1 до {}".format(BOARD_SIZE ** 2)
        
        if board[move - 1] != ' ':
            return False, "Эта клетка уже занята"
        
        return True, ""
    except ValueError:
        return False, "Пожалуйста, введите число"
    
def get_player_color(player):
    """Возвращает цветовой код для игрока"""
    return PLAYER_COLORS.get(player, Fore.WHITE)