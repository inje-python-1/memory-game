from enum import Enum
from PySide6.QtWidgets import QMainWindow, QMenuBar, QMenu, QWidget, QHBoxLayout, QVBoxLayout, QMessageBox
from PySide6.QtTest import QTest
from PySide6.QtCore import Qt

from game.Util import Util
from game.Difficulty import Difficulty
from game.CustomTimer import CustomTimer
from game.CardSet import CardSet
from game.StatusLayout import StatusLayout
from game.Card import Card

class OpeningStatus(Enum):
    READY = 0
    FIRST_CARD_OPENED = 1
    SECOND_CARD_OPENED = 2

class MainWindow(QMainWindow):
    __difficulty = Difficulty.BEGINNER
    difficulty_actions = []
    opening_status = OpeningStatus.READY
    opening_slot: list[Card] = []

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Memory Game")
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setStyleSheet("background: white;")

        menubar = QMenuBar()
        self.setMenuBar(menubar)

        self.game_menu = QMenu("Game")
        menubar.addMenu(self.game_menu)

        self.game_menu.addAction("New Game").triggered.connect(self.new_game)
        self.game_menu.addSeparator()
        for difficulty in Difficulty:
            action = self.game_menu.addAction(difficulty.name.capitalize())
            action.setObjectName(difficulty.name)
            action.setCheckable(True)
            action.triggered.connect(self.difficulty_triggered)
            self.difficulty_actions.append(action)
        self.difficulty_actions[0].setChecked(True)
        self.game_menu.addSeparator()
        self.game_menu.addAction("Exit").triggered.connect(self.close)

        widget = QWidget()
        self.setCentralWidget(widget)
        
        self.layout = QVBoxLayout()
        widget.setLayout(self.layout)

        status_layout = QHBoxLayout()
        self.layout.addLayout(status_layout)

        time_status = StatusLayout("Time", "00:00")
        status_layout.addLayout(time_status)
        self.timer = CustomTimer(time_status)

        self.tries_status = StatusLayout("Tries", 0)
        status_layout.addLayout(self.tries_status)

        self.set_difficulty(Difficulty.BEGINNER)

    def closeEvent(self, event):
        if self.timer:
            self.timer.stop()
        return super().closeEvent(event)

    def card_clicked(self):
        card = self.sender()
        if card.is_opened:
            return
        match self.opening_status:
            case OpeningStatus.READY:
                card.show()
                self.opening_slot.append(card)
                self.opening_status = OpeningStatus.FIRST_CARD_OPENED
            case OpeningStatus.FIRST_CARD_OPENED:
                self.opening_status = OpeningStatus.SECOND_CARD_OPENED
                card.show()
                for opening_card in self.opening_slot:
                    if card is opening_card:
                        self.opening_status = OpeningStatus.FIRST_CARD_OPENED
                        return
                    if card != opening_card:
                        QTest.qWait(1000)
                        card.hide()
                        [opening_card.hide() for opening_card in self.opening_slot]
                        break
                else:
                    self.check_end()

                self.opening_slot.clear()
                
                self.opening_status = OpeningStatus.READY

                self.tries_status.value += 1
    
    def check_end(self):
        if self.card_set.end:
            self.timer.stop()
            QMessageBox(text=f"You win in {self.tries_status.value} tries and {self.timer.time_formatted}").exec()

    def new_game(self):
        self.timer.reset()
        self.timer.start()
        if hasattr(self, "card_set"):
            Util.deleteItemsOfLayout(self.card_set)

        self.card_set = CardSet(self.__difficulty, self.card_clicked)
        self.layout.addLayout(self.card_set)
        self.tries_status.value = 0

        QTest.qWait(10)
        self.resize(0, 0)

    def set_difficulty(self, difficulty: Difficulty):
        self.__difficulty = difficulty
        self.new_game()

    def difficulty_triggered(self):
        for action in self.difficulty_actions:
            action.setChecked(False)
        action = self.sender()
        action.setChecked(True)
        self.set_difficulty(Difficulty[action.objectName()])