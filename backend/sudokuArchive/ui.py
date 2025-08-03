from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton
from cells import SudokuCell
# from .solver import solve_sudoku  # once you have it

class SudokuUI(QWidget):
    # … grid setup, toggle_notes, on_solve (calling solve_sudoku) …
    def __init__(self, puzzle=None):
        super().__init__()
        # puzzle: 9×9 list of ints (0 for empty)
        self.puzzle = puzzle or [[0]*9 for _ in range(9)]
        self.note_mode = False
        self.cells: dict[tuple[int,int], SudokuCell] = {}

        # Layouts
        main_layout = QVBoxLayout(self)
        grid_layout = QGridLayout()
        grid_layout.setSpacing(2)

        # Create grid
        for r in range(9):
            for c in range(9):
                cell = SudokuCell(r, c)
                val = self.puzzle[r][c]
                if val:
                    cell.setText(str(val))
                    cell.setReadOnly(True)
                grid_layout.addWidget(cell, r, c)
                self.cells[(r, c)] = cell
        main_layout.addLayout(grid_layout)

        # Buttons
        btn_layout = QHBoxLayout()
        self.note_btn = QPushButton("Note Mode: OFF")
        self.note_btn.clicked.connect(self.toggle_notes)
        btn_layout.addWidget(self.note_btn)

        solve_btn = QPushButton("Solve / Hint")
        solve_btn.clicked.connect(self.on_solve)
        btn_layout.addWidget(solve_btn)

        main_layout.addLayout(btn_layout)

    def toggle_notes(self):
        self.note_mode = not self.note_mode
        self.note_btn.setText(f"Note Mode: {'ON' if self.note_mode else 'OFF'}")
        for cell in self.cells.values():
            cell.toggle_note_mode(self.note_mode)

    def on_solve(self):
        # Gather current grid state
        current = [[0]*9 for _ in range(9)]
        for (r, c), cell in self.cells.items():
            text = cell.text()
            current[r][c] = int(text) if text.isdigit() else 0
        # TODO: integrate your solver here
        print("Grid state:", current)
