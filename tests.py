import pytest
from pieces import Pawn, Knight, Bishop, King, Rook, Queen

class TestPieceMovement:
    def test_pawn_1(self):
        pawn = Pawn(0, 0)
        assert pawn.get_valid_moves(set()) == {
            (1, 1)
        }
    
    def test_pawn_2(self):
        pawn = Pawn(2, 2)
        assert pawn.get_valid_moves(set()) == {
            (1, 3),
            (3, 3)
        }
    
    def test_pawn_3(self):
        pawn = Pawn(2, 3)
        assert pawn.get_valid_moves(set()) == set()
    
    def test_knight_1(self):
        knight = Knight(1, 1)
        assert knight.get_valid_moves(set()) == {
            (0, 3),
            (2, 3),
            (3, 2),
            (3, 0)
        }
    
    def test_knight_2(self):
        knight = Knight(0, 0)
        assert knight.get_valid_moves(set()) == {
            (1, 2),
            (2, 1)
        }
    
    def test_knight_3(self):
        knight = Knight(3, 3)
        assert knight.get_valid_moves(set()) == {
            (1, 2),
            (2, 1)
        }
    
    def test_knight_4(self):
        knight = Knight(1, 2)
        pieces = {
            Rook(3, 3),
            Rook(2, 0),
            Pawn(0, 1),
            Knight(1, 2),
            Queen(2, 1),
            Bishop(3, 2)
        }
        assert knight.get_valid_moves(pieces) == {
            (3, 3),
            (3, 1),
            (2, 0),
            (0, 0)
        }
    
    def test_bishop_1(self):
        bishop = Bishop(0, 0)
        assert bishop.get_valid_moves(set()) == {
            (1, 1),
            (2, 2),
            (3, 3)
        }
    
    def test_bishop_2(self):
        bishop = Bishop(2, 1)
        assert bishop.get_valid_moves(set()) == {
            (0, 3),
            (1, 2),
            (3, 0),
            (1, 0),
            (3, 2)
        }
    
    def test_bishop_3(self):
        bishop = Bishop(3, 3)
        assert bishop.get_valid_moves(set()) == {
            (2, 2),
            (1, 1),
            (0, 0)
        }
    
    def test_bishop_4(self):
        bishop = Bishop(3, 3)
        assert bishop.get_valid_moves({Pawn(1, 1)}) == {
            (2, 2),
            (1, 1)
        }
    
    def test_rook_1(self):
        rook = Rook(0, 0)
        assert rook.get_valid_moves(set()) == {
            (1, 0),
            (2, 0),
            (3, 0),
            (0, 1),
            (0, 2),
            (0, 3)
        }
    
    def test_rook_2(self):
        rook = Rook(2, 1)
        assert rook.get_valid_moves(set()) == {
            (0, 1),
            (1, 1),
            (3, 1),
            (2, 0),
            (2, 2),
            (2, 3)
        }
    
    def test_rook_3(self):
        rook = Rook(3, 3)
        assert rook.get_valid_moves(set()) == {
            (0, 3),
            (1, 3),
            (2, 3),
            (3, 0),
            (3, 1),
            (3, 2)
        }
    
    def test_rook_4(self):
        rook = Rook(3, 3)
        assert rook.get_valid_moves({Pawn(3, 2)}) == {
            (0, 3),
            (1, 3),
            (2, 3),
            (3, 2)
        }

    def test_queen_1(self):
        queen = Queen(0, 0)
        assert queen.get_valid_moves(set()) == {
            (1, 0),
            (2, 0),
            (3, 0),
            (0, 1),
            (0, 2),
            (0, 3),
            (1, 1),
            (2, 2),
            (3, 3)
        }
    
    def test_queen_2(self):
        queen = Queen(2, 1)
        assert queen.get_valid_moves(set()) == {
            (0, 1),
            (1, 1),
            (3, 1),
            (2, 0),
            (2, 2),
            (2, 3),
            (0, 3),
            (1, 2),
            (3, 0),
            (1, 0),
            (3, 2)
        }
    
    def test_queen_3(self):
        queen = Queen(3, 3)
        assert queen.get_valid_moves(set()) == {
            (0, 3),
            (1, 3),
            (2, 3),
            (3, 0),
            (3, 1),
            (3, 2),
            (2, 2),
            (1, 1),
            (0, 0)
        }

    def test_king_1(self):
        king = King(0, 0)
        assert king.get_valid_moves(set()) == {
            (0, 1),
            (1, 0),
            (1, 1)
        }
    
    def test_king_2(self):
        king = King(2, 1)
        assert king.get_valid_moves(set()) == {
            (1, 0),
            (1, 1),
            (1, 2),
            (2, 0),
            (2, 2),
            (3, 0),
            (3, 1),
            (3, 2)
        }
    
    def test_king_3(self):
        king = King(3, 3)
        assert king.get_valid_moves(set()) == {
            (2, 2),
            (2, 3),
            (3, 2)
        }