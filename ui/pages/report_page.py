from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)


class ReportPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Reports")
        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        layout.addStretch()