from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class HarvestPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Harvest Module")
        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            color:#2E7D32;
        """)

        layout.addStretch()
        layout.addWidget(title)
        layout.addStretch()