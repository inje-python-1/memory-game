class Card: # 카드 클래스의 도입부
    is_opened = False # 카드가 오픈되었는지 여부

    def __init__(self, id: int): # 클래스 초기화 메서드. id는 int형을 받는다.
        self.id = id # id 인자를 클래스의 id 필드에 세트