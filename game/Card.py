import os
from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize

CARD_SIZE = 110, 110

class Card(QPushButton): # 카드 클래스의 도입부
    is_opened = False

    def __init__(self, id: int, clicked: callable): # 클래스 초기화 메서드. id는 int형을 받는다.
        super().__init__()

        self.__id = id # id 인자를 클래스의 __id 필드에 세트
        self.clicked.connect(clicked)
        
        self.cover_pixmap = QPixmap(os.path.join("assets", "card", f"cover.png"))
        self.picture_pixmap = QPixmap(os.path.join("assets", "card", f"{self.__id}.png"))
        
        self.setIconSize(QSize(100, 100))
        
        self.hide()

    def __eq__(self, card):
        return isinstance(card, Card) and self.__id == card.__id
    
    def hide(self):
        self.is_opened = False
        self.setIcon(self.cover_pixmap)

    def show(self):
        self.is_opened = True
        self.setIcon(self.picture_pixmap)