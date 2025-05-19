from game.Card import Card # Card 파일에서 Card 클래스 불러옴

class CardSet: # 카드셋 클래스의 도입부
    cards = [] # 카드 배열
    __size = 12 # 카드 개수. 언더스코어 두 개로 프라이빗임을 선언

    def __init__(self): # 클래스 초기화 메서드
        self.set_size() # 카드 개수를 세트
        self.shuffle() # 카드를 섞기

    def set_size(self, size=12): # 카드 개수를 세트하는 메서드. size의 기본값은 12이다
        if size % 2 == 1: # 개수가 홀수라면 
            raise ValueError("size는 2의 배수여야 합니다") # 예외를 던진다
        
        self.__size = size # size 인자를 클래스의 __size 필드에 세트
        self.cards = [Card(i) for i in range(0, self.__size, 2)] # 클래스의 cards필드에 카드들을 사이즈에 맞게 세트

    def shuffle(self): # 카드를 섞는 메서드
        # TODO: 김민규 구현
        pass