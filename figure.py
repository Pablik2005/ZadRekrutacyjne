from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, position):
        self.range = range(1, 9)
        self.x = 0
        self.y = 0

        tPosition = self.translatePositionToNumeric(position)
        self.x = tPosition[0]
        self.y = tPosition[1]

    @abstractmethod
    def list_available_moves():
        pass

    def validate_move(self, dest_field):
        if str(dest_field) in self.list_available_moves():
            return True
        else:
            return False

    def translatePositionToNumeric(self, position):

        positionUpper = str(position).upper()
        x = "ABCDEFGH".find(positionUpper[0])

        if x != -1:
            x += 1

        if int(positionUpper[1:]) in self.range:
            y = int(positionUpper[1:])
        else:
            y = -1

        return [x, y]

    def translatePositionToChar(self, x, y):
        chars = "ABCDEFGH"
        return str(chars[x - 1]) + str(y)
