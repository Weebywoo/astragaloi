import random
import itertools


class Astragaloi:
    def __init__(self) -> None:
        self.board_p1 = [' '] * 9
        self.board_p2 = [' '] * 9

    def run(self) -> None:
        self.print_gameboard()
        player_order = random.sample([self.board_p1, self.board_p2], 2)
        for player in itertools.cycle(player_order):

            self.random_number_p1 = random.randint(1, 6)
            self.random_number_p2 = random.randint(1, 6)
            self.print_gameboard()

    def print_gameboard(self) -> None:
        print(f'''
        ╔═════════════════════╗
        ║ ┌───┬───┬───┐ ┌───┐ ║
        ║ │ {self.board_p1[0]} │ {self.board_p1[1]} │ {self.board_p1[2]} │ │ {self.random_number_p1} │ ║
        ║ ├───┼───┼───┤ └───┘ ║
        ║ │ {self.board_p1[3]} │ {self.board_p1[4]} │ {self.board_p1[5]} │       ║
        ║ ├───┼───┼───┤       ║
        ║ │ {self.board_p1[6]} │ {self.board_p1[7]} │ {self.board_p1[8]} │       ║
        ║ └───┴───┴───┘       ║
        ╠═════════════════════╣
        ║ ┌───┐ ┌───┬───┬───┐ ║
        ║ │ {self.random_number_p2} │ │ {self.board_p2[0]} │ {self.board_p2[1]} │ {self.board_p2[2]} │ ║
        ║ └───┘ ├───┼───┼───┤ ║
        ║       │ {self.board_p2[3]} │ {self.board_p2[4]} │ {self.board_p2[5]} │ ║
        ║       ├───┼───┼───┤ ║
        ║       │ {self.board_p2[6]} │ {self.board_p2[7]} │ {self.board_p2[8]} │ ║
        ║       └───┴───┴───┘ ║
        ╚═════════════════════╝
        ''')
