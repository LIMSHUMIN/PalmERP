from PySide6.QtCore import Qt, QTimer, QDateTime
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QHBoxLayout,
    QVBoxLayout
)


class TopBar(QFrame):

    def __init__(self):

        super().__init__()

        self.setObjectName("TopBar")
        self.setFixedHeight(90)

        self.build_ui()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)

        self.update_datetime()


    def build_ui(self):

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(20, 10, 20, 10)

        # Left Side
        left_layout = QVBoxLayout()

        self.company = QLabel("🌴 PalmERP Enterprise")
        self.company.setObjectName("Title")

        self.branch = QLabel("ABC Palm Oil Sdn Bhd")
        self.branch.setStyleSheet("""
            background:white;
            border-bottom:1px solid #dddddd;
            font-size:13px;
        """)

        left_layout.addWidget(self.company)
        left_layout.addWidget(self.branch)

        # Right Side
        right_layout = QVBoxLayout()

        self.date = QLabel()
        self.time = QLabel()
        self.user = QLabel("Welcome, ADMIN")

        self.date.setAlignment(Qt.AlignRight)
        self.time.setAlignment(Qt.AlignRight)
        self.user.setAlignment(Qt.AlignRight)

        right_layout.addWidget(self.date)
        right_layout.addWidget(self.time)
        right_layout.addWidget(self.user)

        main_layout.addLayout(left_layout)
        main_layout.addStretch()
        main_layout.addLayout(right_layout)


    def update_datetime(self):

        now = QDateTime.currentDateTime()

        self.date.setText(
            now.toString("dddd, dd MMMM yyyy")
        )

        self.time.setText(
            now.toString("hh:mm:ss AP")
        )