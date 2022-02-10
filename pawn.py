from figure import Figure


class Pawn(Figure):
    def __init__(self, position):
        super().__init__(position)

    def list_available_moves(self):

        availableMoves = []

        if self.x in self.range:

            if (self.y + 1) in self.range:
                availableMoves.append(self.translatePositionToChar(self.x, self.y + 1))

            if (self.y + 2) in self.range:
                availableMoves.append(self.translatePositionToChar(self.x, self.y + 2))

        return sorted(availableMoves)


a = Pawn("D4")
print(a.list_available_moves())
