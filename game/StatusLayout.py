from PySide6.QtWidgets import QVBoxLayout, QLabel
from PySide6.QtCore import Qt

# 상태바용 레이아웃 (이름+값)
class StatusLayout(QVBoxLayout):
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
        self.name_widget.setText(str(self.__name))
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value
        self.value_widget.setText(str(self.__value))
    
    def __init__(self, name, value):
        super().__init__()
        
        self.__name = name
        self.__value = value

        self.name_widget = QLabel(str(self.__name), alignment=Qt.AlignmentFlag.AlignHCenter)
        self.value_widget = QLabel(str(self.__value), alignment=Qt.AlignmentFlag.AlignHCenter)
        self.addWidget(self.name_widget)
        self.addWidget(self.value_widget)