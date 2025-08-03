import sys
from PyQt5.QtWidgets import QApplication
from ui import SudokuUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SudokuUI()
    window.show()
    sys.exit(app.exec_())
