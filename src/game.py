from colorama import Style
from utils import print_board, check_winner, validate_input, get_player_color
from constants import BOARD_SIZE, CELL_EMPTY, WIN_CONDITION

class TicTacToe:
    def __init__(self):
        self.board = [CELL_EMPTY] * (BOARD_SIZE ** 2)
        self.current_player = "X"
        self.game_active = True

    def make_move(self, position):
        """Обрабатывает ход игрока"""
        if self.board[position] == CELL_EMPTY:
            self.board[position] = self.current_player
            return True
        return False
    
    def switch_player(self):
        """Меняет текущего игрока"""
        self.current_player = "O" if self.current_player == "X" else "X"

    def handle_game_over(self, result):
        """Обрабатывает завершение игры"""
        self.game_active = False
        if result == "DRAW":
            print("\n" + "=" * 40)
            print(f"{get_player_color('DRAW')}Игра окончена! Ничья!{Style.RESET_ALL}")
            print("=" * 40)
        else:
            print("\n" + "=" * 40)
            print(f"{get_player_color(result)}Игрок {result} победил!{Style.RESET_ALL}")
            print("=" * 40)

    def process_turn(self):
        """Обрабатывает один ход игры"""
        print_board(self.board)
        
        while True:
            user_input = input(
                f"{get_player_color(self.current_player)}Игрок {self.current_player}, "
                f"введите номер клетки (1-{BOARD_SIZE**2}): {Style.RESET_ALL}"
            )
            
            is_valid, error_msg = validate_input(user_input, self.board)
            if not is_valid:
                print(error_msg)
                continue
                
            move = int(user_input) - 1
            if self.make_move(move):
                self.switch_player()
                break

    def run(self):
        """Основной игровой цикл"""
        print("\nДобро пожаловать в игру Крестики-Нолики!")
        print(f"Размер поля: {BOARD_SIZE}×{BOARD_SIZE}")
        print(f"Для победы нужно собрать линию из {WIN_CONDITION} символов\n")
        
        while self.game_active:
            self.process_turn()
            
            result = check_winner(self.board)
            if result:
                self.handle_game_over(result)
                print_board(self.board)

if __name__ == "__main__":
    from colorama import init
    init(autoreset=True)
    
    game = TicTacToe()
    game.run()