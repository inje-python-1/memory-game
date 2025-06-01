import random
from game.Card import Card # Card 파일에서 Card 클래스 불러옴
from game.Difficulty import Difficulty

from PySide6.QtWidgets import QGridLayout

class CardSet(QGridLayout): # 카드셋 클래스의 도입부
    difficulty = Difficulty.BEGINNER
    cards = []

    def __init__(self, difficulty: Difficulty, card_clicked: callable): # 클래스 초기화 메서드
        super().__init__()
        
        self.card_clicked = card_clicked
        self.difficulty = difficulty

        self.reset() # 카드를 세트
        self.shuffle() # 카드를 섞기
    
    def unregister(self):
        for card in self.cards:
            self.removeWidget(card)

    def register(self):
        for idx, card in enumerate(self.cards):
            row, col = divmod(idx, self.difficulty.value[1])
            self.addWidget(card, row, col)

    def reset(self): # 카드를 세트하는 메서드        
        self.unregister()
        self.cards = [Card(i, lambda card: self.card_clicked(card)) for _ in range(2) for i in range(0, self.difficulty.value[0])] # 클래스의 cards필드에 카드들을 사이즈에 맞게 세트
        self.register()

    def shuffle(self): # 카드를 섞는 메서드
        self.unregister()
        random.shuffle(self.cards)
        self.register()

    @property
    def end(self):
        return all(card.is_opened for card in self.cards)