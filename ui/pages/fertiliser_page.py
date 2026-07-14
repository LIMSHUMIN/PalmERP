from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)


class FertiliserPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Fertiliser Services")
        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        layout.addStretch()