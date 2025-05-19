import pygame # pygame을 불러온다
from game.CardSet import CardSet # CardSet 파일에서 CardSet 클래스 불러옴

pygame.init() # pygame 초기화 함수 호출
window = pygame.display.set_mode((1000, 700)) # pygame 디스플레이 초기화와 크기 설정한 인스턴스를 window 변수에 세트
pygame.display.set_caption("Memory Game") # 창 제목 설정

card_set = CardSet() # 카드셋 클래스를 초기화 한 인스턴스를 card_set 변수에 세트

# 이벤트 루프 도입부
running = True # 실행중 여부
while running: # 실행중이면
    for event in pygame.event.get(): # 이벤트 리스트 다 돌기
        if event.type == pygame.QUIT: # 게임을 나가고 싶어하면
            running = False # 실행중 여부를 False로 세트
            break # for 탈출

    pygame.display.update() # 화면 업데이트

pygame.quit() # 나가기 함수 호출