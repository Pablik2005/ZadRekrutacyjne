from rook import Rook
from queen import Queen
from pawn import Pawn
from knight import Knight
from bishop import Bishop
from king import King


class TestBishop:
    def test_list_available_moves(self):
        bishop = Bishop("D4")
        result = bishop.list_available_moves()
        assert result == [
            "A1",
            "A7",
            "B2",
            "B6",
            "C3",
            "C5",
            "E3",
            "E5",
            "F2",
            "F6",
            "G1",
            "G7",
            "H8",
        ]

    def test_validate_move(self):
        bishop = Bishop("D4")
        result = bishop.validate_move("A1")
        assert result == True


class TestKing:
    def test_list_available_moves(self):
        king = King("D4")
        result = king.list_available_moves()
        assert result == ["C3", "C4", "C5", "D3", "D5", "E3", "E4", "E5"]

    def test_validate_move(self):
        king = King("D4")
        result = king.validate_move("C3")
        assert result == True


class TestKnight:
    def test_list_available_moves(self):
        knight = Knight("D4")
        result = knight.list_available_moves()
        assert result == ["B3", "B5", "C2", "C6", "E6", "F5"]

    def test_validate_move(self):
        knight = Knight("D4")
        result = knight.validate_move("B3")
        assert result == True


class TestPawn:
    def test_list_available_moves(self):
        pawn = Pawn("D4")
        result = pawn.list_available_moves()
        assert result == ["D5", "D6"]

    def test_validate_move(self):
        pawn = Pawn("D4")
        result = pawn.validate_move("D5")
        assert result == True


class TestQueen:
    def test_list_available_moves(self):
        queen = Queen("D4")
        result = queen.list_available_moves()
        assert result == [
            "A1",
            "A4",
            "A7",
            "B2",
            "B4",
            "B6",
            "C3",
            "C4",
            "C5",
            "D1",
            "D2",
            "D3",
            "D5",
            "D6",
            "D7",
            "D8",
            "E3",
            "E4",
            "E5",
            "F2",
            "F4",
            "F6",
            "G1",
            "G4",
            "G7",
            "H4",
            "H8",
        ]

    def test_validate_move(self):
        queen = Queen("D4")
        result = queen.validate_move("A1")
        assert result == True


class TestRook:
    def test_list_available_moves(self):
        rook = Rook("D4")
        result = rook.list_available_moves()
        assert result == [
            "A4",
            "B4",
            "C4",
            "D1",
            "D2",
            "D3",
            "D5",
            "D6",
            "D7",
            "D8",
            "E4",
            "F4",
            "G4",
            "H4",
        ]

    def test_validate_move(self):
        rook = Rook("D4")
        result = rook.validate_move("A4")
        assert result == True


class TestFigure:
    def test_translatePositionToNumeric(self):
        figure = King("D4")
        result = figure.translatePositionToNumeric("D4")
        assert result == [4, 4]

    def test_translatePositionToChar(self):
        figure = King("D4")
        result = figure.translatePositionToChar(4, 4)
        assert result == "D4"
