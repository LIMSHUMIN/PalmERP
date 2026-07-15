from PySide6.QtWidgets import QPushButton


class ActionButton(QPushButton):

    def __init__(self, text):

        super().__init__(text)

        self.setMinimumHeight(45)

        self.setStyleSheet("""
        QPushButton{
            background:#2E7D32;
            color:white;
            border:none;
            border-radius:8px;
            font-size:14px;
            font-weight:bold;
            padding:10px;
        }

        QPushButton:hover{
            background:#388E3C;
        }

        QPushButton:pressed{
            background:#1B5E20;
        }
        """)