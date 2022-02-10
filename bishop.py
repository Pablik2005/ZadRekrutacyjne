from figure import Figure


class Bishop(Figure):
    def __init__(self, position):
        super().__init__(position)

    def list_available_moves(self):

        availableMoves = []

        jump = 1
        while ((self.x + jump) in self.range) and ((self.y + jump) in self.range):
            availableMoves.append(
                self.translatePositionToChar(self.x + jump, self.y + jump)
            )
            jump += 1

        jump = 1
        while ((self.x - jump) in self.range) and ((self.y - jump) in self.range):
            availableMoves.append(
                self.translatePositionToChar(self.x - jump, self.y - jump)
            )
            jump += 1

        jump = 1
        while ((self.x + jump) in self.range) and ((self.y - jump) in self.range):
            availableMoves.append(
                self.translatePositionToChar(self.x + jump, self.y - jump)
            )
            jump += 1

        jump = 1
        while ((self.x - jump) in self.range) and ((self.y + jump) in self.range):
            availableMoves.append(
                self.translatePositionToChar(self.x - jump, self.y + jump)
            )
            jump += 1

        return sorted(availableMoves)
