# 레이아웃 내 위젯/아이템 정리 유틸
class Util:
    def deleteItemsOfLayout(layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)           # 위젯 정리
                else:
                    Util.deleteItemsOfLayout(item.layout())   # 재귀적으로 내부 레이아웃 정리