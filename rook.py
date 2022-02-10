from figure import Figure


class Rook(Figure):
    def __init__(self, position):
        super().__init__(position)

    def list_available_moves(self):

        availableMoves = []

        if self.y in self.range:

            jump = 1
            while (self.x + jump) in self.range:
                availableMoves.append(
                    self.translatePositionToChar(self.x + jump, self.y)
                )
                jump += 1

            jump = 1
            while (self.x - jump) in self.range:
                availableMoves.append(
                    self.translatePositionToChar(self.x - jump, self.y)
                )
                jump += 1

        if self.x in self.range:

            jump = 1
            while (self.y + jump) in self.range:
                availableMoves.append(
                    self.translatePositionToChar(self.x, self.y + jump)
                )
                jump += 1

            jump = 1
            while (self.y - jump) in self.range:
                availableMoves.append(
                    self.translatePositionToChar(self.x, self.y - jump)
                )
                jump += 1

            return sorted(availableMoves)
