import sys
from PySide6.QtWidgets import QApplication
from game.MainWindow import MainWindow

# QApplication 객체 생성 (모든 Qt 애플리케이션은 반드시 필요)
app = QApplication(sys.argv)

# 메인 윈도우(게임 창) 생성
main_window = MainWindow()

# 메인 윈도우를 화면에 표시
main_window.show()

# 이벤트 루프 실행 (프로그램 종료 시까지 계속 실행)
sys.exit(app.exec())