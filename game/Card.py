import os
from PySide6.QtWidgets import QPushButton 

# 카드 클래스 (1장 카드의 모양, 상태 등)
class Card(QPushButton):
    is_opened = False

    def __init__(self, id: int, clicked: callable):
        super().__init__()

        self.__id = id  # 카드 번호
        self.clicked.connect(clicked)  # 클릭 시 콜백 호출
        
        # 스타일시트(카드 이미지) 설정
        self.cover_stylesheet = f"border-image: url('assets/card/cover.jpg');"
        self.picture_stylesheet = f"border-image: url('assets/card/{os.path.basename(str(self.__id))}.png');"

        self.setFixedSize(154, 214)
        
        self.show()  # 시작 시 일단 카드를 열어 보여주기

    def __eq__(self, card):
        # 카드 비교
        return isinstance(card, Card) and self.__id == card.__id
    
    def hide(self):
        # 카드 뒷면(덮기)
        self.is_opened = False
        self.setStyleSheet(self.cover_stylesheet)

    def show(self):
        # 카드 앞면(보이기)
        self.is_opened = True
        self.setStyleSheet(self.picture_stylesheet)