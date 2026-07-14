from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout
)


class InfoCard(QFrame):

    def __init__(self, title, value):

        super().__init__()

        self.setStyleSheet("""
            QFrame{
                background:white;
                border:1px solid #DDDDDD;
                border-radius:10px;
            }
        """)

        layout = QVBoxLayout(self)

        lbl_title = QLabel(title)
        lbl_title.setStyleSheet("""
            color:gray;
            font-size:14px;
        """)

        lbl_value = QLabel(value)
        lbl_value.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#2E7D32;
        """)

        layout.addWidget(lbl_title)
        layout.addWidget(lbl_value)