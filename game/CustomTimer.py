import threading

class CustomTimer():
    time = 0

    @property
    def time_formatted(self):
        m, s = divmod(abs(self.time), 60)
        if self.time < 0:
            return f'-{m:02}:{s:02}'
        else:
            return f'{m:02}:{s:02}'

    def __init__(self, widget, time_changed):
        self.widget = widget
        self.time_changed = time_changed

    def reset(self):
        self.stop()
        self.time = -3
    
    def stop(self):
        if hasattr(self, "timer"):
            self.timer.cancel()
        
    def start(self):
        self.timer = threading.Timer(1, self.start)
        self.timer.start()
        self.time += 1
        self.update()

    def update(self):
        self.time_changed(self.time)
        self.widget.value = self.time_formatted