import threading

class CustomTimer():
    time = 0

    @property
    def time_formatted(self):
        m, s = divmod(self.time, 60)
        return f'{m:02}:{s:02}'

    def __init__(self, widget):
        self.widget = widget

    def reset(self):
        self.stop()
        self.time = 0
    
    def stop(self):
        if hasattr(self, "timer"):
            self.timer.cancel()
        
    def start(self):
        self.timer = threading.Timer(1, self.start)
        self.timer.start()
        self.time += 1
        self.update()

    def update(self):
        self.widget.value = self.time_formatted