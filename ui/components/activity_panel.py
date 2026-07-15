from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout
)


class ActivityPanel(QFrame):

    def __init__(self):

        super().__init__()

        self.setStyleSheet("""
        QFrame{
            background:white;
            border:1px solid #DDDDDD;
            border-radius:10px;
        }
        """)

        layout = QVBoxLayout(self)

        title = QLabel("Recent Activities")

        title.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        activities = [
            "Supplier S0001 created",
            "Purchase P00001 saved",
            "Advance RM500 approved",
            "Settlement completed"
        ]

        for item in activities:
            layout.addWidget(QLabel("• " + item))