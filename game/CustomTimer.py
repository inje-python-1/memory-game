import threading

# 커스텀 타이머 클래스 (1초마다 시간 갱신)
class CustomTimer():
    time = 0  # 타이머 값(초)
    time = 0

    @property
    def time_formatted(self):
        # 시간(초) -> 문자열 포맷(MM:SS)
        m, s = divmod(abs(self.time), 60)
        if self.time < 0:
            return f'-{m:02}:{s:02}'
        else:
            return f'{m:02}:{s:02}'

    def __init__(self, widget, time_changed):
        self.widget = widget
        self.time_changed = time_changed

    def reset(self):
        # 타이머 초기화 (카운트다운 -3부터 시작)
        self.stop()
        self.time = -3
    
    def stop(self):
        if hasattr(self, "timer"):
            self.timer.cancel()  # 타이머 멈춤
        
    def start(self):
        # 1초마다 start 재호출 (재귀적)
        self.timer = threading.Timer(1, self.start)
        self.timer.start()
        self.time += 1
        self.update()

    def update(self):
        # 시간변경 콜백호출, 시간 텍스트설정
        self.time_changed(self.time)
        self.widget.value = self.time_formatted