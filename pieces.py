from typing import Tuple, Set, List
from enum import Enum
from abc import ABC, abstractmethod

class PieceType(Enum):
    ROOK = 1
    KNIGHT = 2
    BISHOP = 3
    QUEEN = 4
    KING = 5
    PAWN = 6

enum_to_string = {
    PieceType.ROOK: "Rook",
    PieceType.KNIGHT: "Knight", 
    PieceType.BISHOP: "Bishop",
    PieceType.QUEEN: "Queen",
    PieceType.KING: "King",
    PieceType.PAWN: "Pawn"
}

class Piece(ABC):
    def _is_valid_position(self, position: Tuple[int, int]) -> bool:
        return position[0] < 4 and \
                position[0] >= 0 and \
                position[1] < 4 and \
                position[1] >= 0

    @abstractmethod
    def get_valid_moves(self) -> Set[Tuple[int, int]]:
        return NotImplemented


class Pawn(Piece):
    def __init__(self, x: int, y: int):
        self.position = (x, y)
        self.piece_type = PieceType.PAWN

    def get_valid_moves(self, pieces: List[Piece]):
        all_positions = [
            (self.position[0] - 1, self.position[1] + 1),
            (self.position[0] + 1, self.position[1] + 1),
        ]

        return {position for position in all_positions if self._is_valid_position(position)}

    def __str__(self):
        return f"{enum_to_string[self.piece_type]} at position {self.position}"


class Knight(Piece):
    def __init__(self, x: int, y: int):
        self.position = (x, y)
        self.piece_type = PieceType.KNIGHT
    
    def get_valid_moves(self, pieces: List[Piece]):
        all_positions = []
        all_positions.append((self.position[0] + 2, self.position[1] + 1))
        all_positions.append((self.position[0] + 2, self.position[1] - 1))
        
        all_positions.append((self.position[0] - 2, self.position[1] + 1))
        all_positions.append((self.position[0] - 2, self.position[1] - 1))

        all_positions.append((self.position[0] + 1, self.position[1] + 2))
        all_positions.append((self.position[0] - 1, self.position[1] + 2))

        all_positions.append((self.position[0] + 1, self.position[1] - 2))
        all_positions.append((self.position[0] - 1, self.position[1] - 2))
        
        return {position for position in all_positions if self._is_valid_position(position)}

    def __str__(self):
        return f"{enum_to_string[self.piece_type]} at position {self.position}"


class Bishop(Piece):
    def __init__(self, x: int, y: int):
        self.position = (x, y)
        self.piece_type = PieceType.BISHOP
    
    def get_valid_moves(self, pieces: List[Piece]):
        all_positions = []
        piece_positions = {piece.position for piece in pieces if piece.position != self.position}
        
        # Check each diagonal direction
        for dx, dy in [(1,1), (1,-1), (-1,1), (-1,-1)]:
            for i in range(1, 4):
                new_pos = (self.position[0] + i*dx, self.position[1] + i*dy)
                if not self._is_valid_position(new_pos):
                    break

                all_positions.append(new_pos)
                if new_pos in piece_positions:
                    break
                
        
        return {position for position in all_positions if self._is_valid_position(position)}

    def __str__(self):
        return f"{enum_to_string[self.piece_type]} at position {self.position}"


class Rook(Piece):
    def __init__(self, x: int, y: int):
        self.position = (x, y)
        self.piece_type = PieceType.ROOK
    
    def get_valid_moves(self, pieces: List[Piece]):
        all_positions = []
        piece_positions = {piece.position for piece in pieces if piece.position != self.position}
        
        # Check each orthogonal direction
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            for i in range(1, 4):
                new_pos = (self.position[0] + i*dx, self.position[1] + i*dy)
                if not self._is_valid_position(new_pos):
                    break
                
                all_positions.append(new_pos)
                if new_pos in piece_positions:
                    break

        
        return {position for position in all_positions if self._is_valid_position(position)}

    def __str__(self):
        return f"{enum_to_string[self.piece_type]} at position {self.position}"


class Queen(Piece):
    def __init__(self, x: int, y: int):
        self.position = (x, y)
        self.piece_type = PieceType.QUEEN
    
    def get_valid_moves(self, pieces: List[Piece]):
        bishop = Bishop(*self.position)
        rook = Rook(*self.position)
        return bishop.get_valid_moves(pieces) | rook.get_valid_moves(pieces)
        
    def __str__(self):
        return f"{enum_to_string[self.piece_type]} at position {self.position}"


class King(Piece):
    def __init__(self, x: int, y: int):
        self.position = (x, y)
        self.piece_type = PieceType.KING
    
    def get_valid_moves(self, pieces: List[Piece]):
        all_positions = []
        # King moves one square in any direction
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                all_positions.append((self.position[0] + dx, self.position[1] + dy))
        
        return {position for position in all_positions if self._is_valid_position(position)}

    def __str__(self):
        return f"{enum_to_string[self.piece_type]} at position {self.position}"

