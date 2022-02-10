from figure import Figure


class King(Figure):
    def __init__(self, position):
        super().__init__(position)

    def list_available_moves(self):

        availableMoves = []

        if self.x + 1 in self.range:
            if self.y + 1 in self.range:
                availableMoves.append(
                    self.translatePositionToChar(self.x + 1, self.y + 1)
                )
            if self.y in self.range:
                availableMoves.append(self.translatePositionToChar(self.x + 1, self.y))
            if self.y - 1 in self.range:
                availableMoves.append(
                    self.translatePositionToChar(self.x + 1, self.y - 1)
                )

        if self.x in self.range:
            if self.y + 1 in self.range:
                availableMoves.append(self.translatePositionToChar(self.x, self.y + 1))
            if self.y - 1 in self.range:
                availableMoves.append(self.translatePositionToChar(self.x, self.y - 1))

        if self.x - 1 in self.range:
            if self.y + 1 in self.range:
                availableMoves.append(
                    self.translatePositionToChar(self.x - +1, self.y + 1)
                )
            if self.y in self.range:
                availableMoves.append(self.translatePositionToChar(self.x - +1, self.y))
            if self.y - 1 in self.range:
                availableMoves.append(
                    self.translatePositionToChar(self.x - 1, self.y - 1)
                )

        return sorted(availableMoves)
