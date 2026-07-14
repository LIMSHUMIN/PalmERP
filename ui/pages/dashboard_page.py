from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Dashboard")
        title.setObjectName("Title")

        welcome = QLabel("Welcome to PalmERP Enterprise")
        welcome.setObjectName("Subtitle")

        layout.addWidget(title)
        layout.addWidget(welcome)
        layout.addStretch()