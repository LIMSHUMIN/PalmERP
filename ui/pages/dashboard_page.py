from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout
)

from ui.components.info_card import InfoCard
from ui.components.action_button import ActionButton
from ui.components.activity_panel import ActivityPanel


class DashboardPage(QWidget):

    def __init__(self):

        super().__init__()

        self.build_ui()


    def build_ui(self):

        main_layout = QVBoxLayout(self)

        title = QLabel("Dashboard")

        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        subtitle = QLabel(
            "Welcome back, Administrator"
        )

        subtitle.setStyleSheet("""
            color:gray;
            font-size:14px;
        """)

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        main_layout.addSpacing(20)

        # Cards

        cards = QGridLayout()

        cards.addWidget(
            InfoCard("Suppliers","1250"),
            0,0
        )

        cards.addWidget(
            InfoCard("Today's FFB","320 MT"),
            0,1
        )

        cards.addWidget(
            InfoCard("Advance","RM25,800"),
            0,2
        )

        cards.addWidget(
            InfoCard("Settlement","RM80,350"),
            0,3
        )

        main_layout.addLayout(cards)

        main_layout.addSpacing(25)

        # Quick Actions

        quick = QLabel("Quick Actions")

        quick.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
        """)

        main_layout.addWidget(quick)

        button_layout = QHBoxLayout()

        button_layout.addWidget(ActionButton("New Supplier"))
        button_layout.addWidget(ActionButton("New Purchase"))
        button_layout.addWidget(ActionButton("Settlement"))

        button_layout.addStretch()

        main_layout.addLayout(button_layout)

        main_layout.addSpacing(20)

        main_layout.addWidget(ActivityPanel())

        main_layout.addStretch()