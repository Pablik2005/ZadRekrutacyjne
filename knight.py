from figure import Figure


class Knight(Figure):
    def __init__(self, position):
        super().__init__(position)

    def list_available_moves(self):

        availableMoves = []

        if self.x + 2 in self.range:
            if self.y + 1 in self.range:
                availableMoves.append(
                    self.translatePositionToChar(self.x + 2, self.y + 1)
                )
        if self.x + 1 in self.range:
            if self.y + 2 in self.range:
                availableMoves.append(
                    self.translatePositionToChar(self.x + 1, self.y + 2)
                )
        if self.x - 1 in self.range:
            if self.y + 2 in self.range:
                availableMoves.append(
                    self.translatePositionToChar(self.x - 1, self.y + 2)
                )
        if self.x - 2 in self.range:
            if self.y + 1 in self.range:
                availableMoves.append(
                    self.translatePositionToChar(self.x - 2, self.y + 1)
                )
        if self.x - 2 in self.range:
            if self.y - 1 in self.range:
                availableMoves.append(
                    self.translatePositionToChar(self.x - 2, self.y - 1)
                )
        if self.x - 1 in self.range:
            if self.y - 2 in self.range:
                availableMoves.append(
                    self.translatePositionToChar(self.x - 1, self.y - 2)
                )

        return sorted(availableMoves)
