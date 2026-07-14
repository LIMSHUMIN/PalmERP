from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QHBoxLayout
)


class TopBar(QFrame):

    def __init__(self):

        super().__init__()

        self.setObjectName("TopBar")
        self.setFixedHeight(60)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 10, 20, 10)

        self.title = QLabel("🌴 PalmERP Enterprise")
        self.title.setObjectName("Title")

        self.user = QLabel("Welcome, ADMIN")

        layout.addWidget(self.title)
        layout.addStretch()
        layout.addWidget(self.user)