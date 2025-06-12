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

# 카드 오픈 상태를 나타내는 Enum 클래스
class OpeningStatus(Enum):
    READY = 0                  # 아직 아무 카드도 안 연 상태
    FIRST_CARD_OPENED = 1      # 첫 번째 카드를 연 상태
    SECOND_CARD_OPENED = 2     # 두 번째 카드를 연 상태

# 메인 윈도우 클래스 (게임의 메인 UI)
class MainWindow(QMainWindow):
    __difficulty = Difficulty.BEGINNER       # 현재 난이도 (초기값: 초급)
    difficulty_actions = []                  # 난이도별 메뉴 액션들 저장
    opening_status = OpeningStatus.READY     # 현재 카드 오픈 상태
    opening_slot: list[Card] = []           # 현재 오픈된 카드들 저장

    def __init__(self):
        super().__init__()
        
        # 윈도우 타이틀 및 스타일 설정
        self.setWindowTitle("Memory Game")
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setStyleSheet("background: white; font-size: 13pt;")

        # 메뉴바 및 게임 메뉴 생성
        menubar = QMenuBar(self)
        menubar.setStyleSheet("background: #efefef;")
        self.setMenuBar(menubar)

        self.game_menu = QMenu("Game", menubar)
        menubar.addMenu(self.game_menu)

        # 새 게임 메뉴 액션
        self.game_menu.addAction("New Game").triggered.connect(self.new_game)
        self.game_menu.addSeparator()

        # 난이도 메뉴 액션 동적으로 생성 및 연결
        for difficulty in Difficulty:
            action = self.game_menu.addAction(difficulty.name.capitalize())
            action.setObjectName(difficulty.name)
            action.setCheckable(True)
            action.triggered.connect(self.difficulty_triggered)
            self.difficulty_actions.append(action)
        self.difficulty_actions[0].setChecked(True)  # 첫 번째(초급) 선택

        # 종료 메뉴 액션
        self.game_menu.addSeparator()
        self.game_menu.addAction("Exit").triggered.connect(self.close)

        # 메인 레이아웃 설정 (상단 상태바 + 카드판)
        widget = QWidget()
        self.setCentralWidget(widget)
        
        self.layout = QVBoxLayout()
        widget.setLayout(self.layout)

        status_layout = QHBoxLayout()
        self.layout.addLayout(status_layout)

        # 시간 상태바 (타이머 표시)
        time_status = StatusLayout("Time", "00:00")
        status_layout.addLayout(time_status)
        self.timer = CustomTimer(time_status, self.time_changed)

        # 시도 횟수 상태바
        self.tries_status = StatusLayout("Tries", 0)
        status_layout.addLayout(self.tries_status)

        # 첫 게임 세팅 (난이도: 초급)
        self.set_difficulty(Difficulty.BEGINNER)

    def closeEvent(self, event):
        # 윈도우 닫을 때 타이머 멈춤
        if self.timer:
            self.timer.stop()
        return super().closeEvent(event)

    # 카드 클릭 시 호출되는 메서드
    def card_clicked(self):
        card = self.sender()
        if card.is_opened:
            return  # 이미 열린 카드는 무시

        match self.opening_status:
            case OpeningStatus.READY:
                # 첫 번째 카드 오픈
                card.show()
                self.opening_slot.append(card)
                self.opening_status = OpeningStatus.FIRST_CARD_OPENED
            case OpeningStatus.FIRST_CARD_OPENED:
                # 두 번째 카드 오픈
                self.opening_status = OpeningStatus.SECOND_CARD_OPENED
                card.show()
                for opening_card in self.opening_slot:
                    if card is opening_card:
                        # 같은 카드를 두 번 클릭하면 무시
                        self.opening_status = OpeningStatus.FIRST_CARD_OPENED
                        return
                    if card != opening_card:
                        # 다른 카드이면서 짝이 안 맞음 -> 1초 후 뒤집힘
                        QTest.qWait(1000)
                        card.hide()
                        [opening_card.hide() for opening_card in self.opening_slot]
                        break
                else:
                    # 모든 카드가 맞았으면 게임 끝났는지 체크
                    self.check_end()

                self.opening_slot.clear()
                self.opening_status = OpeningStatus.READY
                self.tries_status.value += 1  # 시도 횟수 증가
    
    # 게임 끝났는지(모든 카드가 열렸는지) 체크. 클리어 시 메시지 띄움
    def check_end(self):
        if self.card_set.end:
            self.timer.stop()
            msgbox = QMessageBox(self)
            msgbox.setWindowTitle("Congratulations!!")
            msgbox.setText(f"You win in {self.tries_status.value} tries and {self.timer.time_formatted}")
            msgbox.exec()
            self.tries_status.value -= 1  # 시도 횟수 보정

    # 새 게임 시작: 상태 초기화, 카드 세팅/섞기
    def new_game(self):
        self.opening_status = OpeningStatus.READY
        self.opening_slot.clear()
        self.timer.reset()
        self.timer.start()
        if hasattr(self, "card_set"):
            Util.deleteItemsOfLayout(self.card_set)  # 이전 카드 삭제

        self.card_set = CardSet(self.__difficulty, self.card_clicked)
        self.layout.addLayout(self.card_set)
        self.tries_status.value = 0

        QTest.qWait(10)
        self.resize(0, 0)  # 창 크기 재조정

    # 난이도 변경 및 새 게임 시작
    def set_difficulty(self, difficulty: Difficulty):
        self.__difficulty = difficulty
        self.new_game()

    # 난이도 메뉴 액션 클릭 핸들러
    def difficulty_triggered(self):
        for action in self.difficulty_actions:
            action.setChecked(False)
        action = self.sender()
        action.setChecked(True)
        self.set_difficulty(Difficulty[action.objectName()])

    # 시간이 바뀌었을때(1초마다 호출되겠죠?)
    def time_changed(self, time):
        # time이 0초가 되면, 카드를 모두 가림.
        # 마이너스 시간 동안 카드를 기억할 수 있게 하기 위함.
        if time == 0:
            for card in self.card_set.cards:
                card.hide()
            self.update()