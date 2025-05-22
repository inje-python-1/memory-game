import os
import pygame

CARD_SIZE = 110, 110

class Card: # 카드 클래스의 도입부
    coords = 0, 0

    def __init__(self, id: int): # 클래스 초기화 메서드. id는 int형을 받는다.
        self.__id = id # id 인자를 클래스의 __id 필드에 세트
        self.__surface = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "card", f"{self.__id}.png")),
            CARD_SIZE
        )
        self.__cover_surface = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "card", "cover.png")),
            CARD_SIZE
        )

    def __eq__(self, card):
        return isinstance(card, Card) and self.__id == card.__id

    def open(self):
        pygame.display.get_surface().blit(self.__surface, self.coords)
        
    def close(self):
        pygame.display.get_surface().blit(self.__cover_surface, self.coords)