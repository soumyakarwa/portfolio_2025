from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QFont, QPainter
from PyQt5.QtCore import Qt

class SudokuCell(QLineEdit):
    def __init__(self, row: int, col: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.row = row
        self.col = col
        self.notes: set[int] = set()
        self.note_mode = False

        # Fonts for display
        self.big_font = QFont('Arial', 24)
        self.note_font = QFont('Arial', 8)
        self.setFont(self.big_font)
        self.setAlignment(Qt.AlignCenter)
        self.setMaxLength(1)
        self.setContextMenuPolicy(Qt.NoContextMenu)

    def toggle_note_mode(self, on: bool):
        self.note_mode = on
        self.setReadOnly(on)
        self.setFont(self.note_font if on else self.big_font)
        self.update()

    def keyPressEvent(self, ev):
        if self.note_mode:
            key = ev.text()
            if key in '123456789':
                if key in self.notes:
                    self.notes.remove(key)
                else:
                    self.notes.add(key)
                self.update()
            elif ev.key() in (Qt.Key_Backspace, Qt.Key_Delete):
                self.notes.clear()
                self.update()
        else:
            super().keyPressEvent(ev)

    def paintEvent(self, ev):
        if self.note_mode and self.notes:
            painter = QPainter(self)
            painter.setFont(self.note_font)
            w = self.width() / 3
            h = self.height() / 3
            for note in self.notes:
                idx = int(note) - 1
                x = (idx % 3) * w
                y = (idx // 3) * h + h * 0.8
                painter.drawText(x, y, note)
            painter.end()
        else:
            super().paintEvent(ev)
