from figure import Figure
from bishop import Bishop
from rook import Rook


class Queen(Figure):
    def __init__(self, position):
        super().__init__(position)

    def list_available_moves(self):

        availableMoves = []

        bishop = Bishop(self.translatePositionToChar(self.x, self.y))
        rook = Rook(self.translatePositionToChar(self.x, self.y))

        availableMoves = bishop.list_available_moves() + rook.list_available_moves()

        return sorted(availableMoves)
