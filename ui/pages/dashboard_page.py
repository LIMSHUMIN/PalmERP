from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGridLayout,
)

from ui.components.info_card import InfoCard


class DashboardPage(QWidget):

    def __init__(self):

        super().__init__()

        self.build_ui()


    def build_ui(self):

        layout = QVBoxLayout(self)

        title = QLabel("Dashboard")
        title.setStyleSheet("""
            font-size:26px;
            font-weight:bold;
        """)

        welcome = QLabel(
            "Welcome back to PalmERP Enterprise"
        )

        welcome.setStyleSheet("""
            color:gray;
            font-size:14px;
        """)

        layout.addWidget(title)
        layout.addWidget(welcome)

        layout.addSpacing(20)

        grid = QGridLayout()

        grid.setHorizontalSpacing(20)
        grid.setVerticalSpacing(20)

        grid.addWidget(
            InfoCard("Suppliers","1250"),
            0,0
        )

        grid.addWidget(
            InfoCard("Today's FFB","320 MT"),
            0,1
        )

        grid.addWidget(
            InfoCard("Advance","RM 25,800"),
            1,0
        )

        grid.addWidget(
            InfoCard("Settlement","RM 80,350"),
            1,1
        )

        layout.addLayout(grid)

        layout.addStretch()