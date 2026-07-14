from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout
)


class InfoCard(QFrame):

    def __init__(self, title, value):

        super().__init__()

        self.setMinimumSize(220,120)

        self.setStyleSheet("""
        QFrame{
            background:white;
            border:1px solid #DDDDDD;
            border-radius:10px;
        }

        QLabel#Title{
            color:gray;
            font-size:14px;
        }

        QLabel#Value{
            color:#2E7D32;
            font-size:28px;
            font-weight:bold;
        }
        """)

        layout = QVBoxLayout(self)

        titleLabel = QLabel(title)
        titleLabel.setObjectName("Title")

        valueLabel = QLabel(value)
        valueLabel.setObjectName("Value")

        valueLabel.setAlignment(Qt.AlignCenter)

        layout.addWidget(titleLabel)
        layout.addStretch()
        layout.addWidget(valueLabel)