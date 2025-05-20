from game.Card import Card # Card 파일에서 Card 클래스 불러옴

class CardSet: # 카드셋 클래스의 도입부
    def __init__(self): # 클래스 초기화 메서드
        self.resize() # 카드 개수를 세트
        self.shuffle() # 카드를 섞기

    def resize(self, size=10): # 카드 개수를 세트하는 메서드. size의 기본값은 10이다
        if size % 2 == 1: # 개수가 홀수라면 
            raise ValueError("size는 2의 배수여야 합니다") # 예외를 던진다
        
        self.size = size # size 인자를 클래스의 size 필드에 세트
        self.cards = [Card(i) for i in range(0, self.size, 2)] # 클래스의 cards필드에 카드들을 사이즈에 맞게 세트

    def shuffle(self): # 카드를 섞는 메서드
        # TODO: 김민규 구현
        raise NotImplementedError