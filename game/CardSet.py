import random
import pygame
from game.Card import Card # Card 파일에서 Card 클래스 불러옴

DEFAULT_CARD_SET_SIZE = 10

class CardSet: # 카드셋 클래스의 도입부
    def __init__(self): # 클래스 초기화 메서드
        self.resize() # 카드 개수를 세트
        self.shuffle() # 카드를 섞기
        self.draw()
    
    def draw(self):
        for idx, card in enumerate(self.cards):
            card.coords = 90 + idx % 5 * 150, 90 + idx // 5 * 150
            card.close()
        
        pygame.display.flip()

    def resize(self, size=DEFAULT_CARD_SET_SIZE): # 카드 개수를 세트하는 메서드
        self.size = size # size 인자를 클래스의 size 필드에 세트
        self.cards = [Card(i) for _ in range(1) for i in range(0, self.size)] # 클래스의 cards필드에 카드들을 사이즈에 맞게 세트

    def shuffle(self): # 카드를 섞는 메서드
        random.shuffle(self.cards)