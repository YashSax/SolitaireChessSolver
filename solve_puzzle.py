from pieces import *
from typing import List
import tkinter as tk
from tkinter import ttk

class Board:
    def __init__(self, board: List[List[PieceType]]):
        self.pieces = []
        for i in range(4):
            for j in range(4):
                if board[i][j] == PieceType.ROOK:
                    self.pieces.append(Rook(j, 3 - i))
                elif board[i][j] == PieceType.QUEEN:
                    self.pieces.append(Queen(j, 3 - i))
                elif board[i][j] == PieceType.PAWN:
                    self.pieces.append(Pawn(j, 3 - i))
                elif board[i][j] == PieceType.KNIGHT:
                    self.pieces.append(Knight(j, 3 - i))
                elif board[i][j] == PieceType.BISHOP:
                    self.pieces.append(Bishop(j, 3 - i))
                elif board[i][j] == PieceType.KING:
                    self.pieces.append(King(j, 3 - i))

    def show(self):
        display_board = [['.'] * 4 for _ in range(4)]
        
        for piece in self.pieces:
            x, y = piece.position
            display_board[3 - y][x] = enum_to_string[piece.piece_type]
        
        for row in display_board:
            aligned_row = [str(cell).rjust(6) for cell in row]
            print(' '.join(aligned_row))
        print()
    
    def solve(self):
        self.solution_found = False
        return self.solve_helper(self.pieces, "")
    
    def solve_helper(self, pieces: List[Piece], logs: str):
        if self.solution_found:
            return
        
        if len(pieces) == 1:
            print(logs)
            self.solution_found = True
            return
        
        piece_locations = {piece.position : piece for piece in pieces}
        for piece in pieces:
            potential_moves = piece.get_valid_moves(pieces)
            potential_captures = set(piece_locations.keys()).intersection(potential_moves)
            
            for capture in potential_captures:
                taken_piece = piece_locations[capture]
                taken_piece_idx = pieces.index(taken_piece)
                pieces.pop(taken_piece_idx)
                prev_position, prev_string = piece.position, str(piece)
                piece.position = capture
                self.solve_helper(pieces, logs + f"\n {prev_string} takes {str(taken_piece)}")
                piece.position = prev_position
                pieces.insert(taken_piece_idx, taken_piece)
    
def create_board():
    board_state = [[None]*4 for _ in range(4)]
    result = None
    
    def on_cell_click(row, col):
        # Create popup with piece selection
        popup = tk.Toplevel(root)
        popup.title("Select Piece")
        
        def set_piece(piece_type):
            board_state[row][col] = piece_type
            buttons[row][col].config(text=enum_to_string.get(piece_type, ''))
            popup.destroy()
        
        def clear_cell():
            board_state[row][col] = None
            buttons[row][col].config(text='')
            popup.destroy()
            
        for piece_type in PieceType:
            btn = ttk.Button(popup, text=enum_to_string[piece_type],
                            command=lambda p=piece_type: set_piece(p))
            btn.pack(fill='x')
            
        clear_btn = ttk.Button(popup, text="Clear", command=clear_cell)
        clear_btn.pack(fill='x')
        
    root = tk.Tk()
    root.title("Solitaire Chess Setup")
    
    buttons = []
    for i in range(4):
        row = []
        for j in range(4):
            btn = ttk.Button(root, text='', width=10,
                            command=lambda r=i,c=j: on_cell_click(r,c))
            btn.grid(row=i, column=j, padx=2, pady=2)
            row.append(btn)
        buttons.append(row)
        
    def create_board_obj():
        nonlocal result
        result = Board(board_state)
        root.destroy()
        
    create_btn = ttk.Button(root, text="Create Board", 
                            command=create_board_obj)
    create_btn.grid(row=4, columnspan=4, pady=10)
    
    root.mainloop()
    return result


if __name__ == "__main__":
    board = create_board()

    if board:
        board.show()
        board.solve()

