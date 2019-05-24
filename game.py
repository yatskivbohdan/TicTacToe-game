from board import Board
import copy

class Game:
    def __init__(self):
        self._board = Board()

    def check_input(self, cell):
        if not 0 <= cell[0] <= 2 or not 0 <= cell[1] <= 2:
            print("Enter a valid input!")
            return False
        if self._board.cells[cell[0]][cell[1]] != 0:
            print("This cell is not empty!")
            return False
        return True

    def main(self):
        has_finished = self._board.has_winner()
        while not has_finished:
            valid = False
            while not valid:
                coords = tuple(map(lambda x: int(x)-1,
                               eval(input("Enter your move coordinates(from 1 to 3)(Example: (1, 2):"))))
                valid = self.check_input(coords)
            self._board.make_move(coords)
            left_board = copy.deepcopy(self._board)
            right_board = copy.deepcopy(self._board)
            left_board.make_random_move()
            right_board.make_random_move()
            if left_board.compute_score() > right_board.compute_score():
                self._board = left_board
            else:
                self._board = right_board
            print(self._board)
            has_finished = self._board.has_winner()
        transform = {Board.DRAW: "A draw", Board.NOUGHT: "Computer won", Board.CROSS: "You won"}
        print("Game has finished")
        print(transform[self._board.has_winner()])


Game().main()