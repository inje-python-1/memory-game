import sys
from PySide6.QtWidgets import QApplication
from game.MainWindow import MainWindow

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())