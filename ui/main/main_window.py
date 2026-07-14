from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from ui.components.sidebar import Sidebar
from ui.pages.dashboard_page import DashboardPage
from ui.components.topbar import TopBar


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("PalmERP Enterprise")

        self.resize(1400, 800)

        self.build_ui()

    def build_ui(self):

        central = QWidget()

        self.setCentralWidget(central)

        root = QHBoxLayout(central)

        self.sidebar = Sidebar()

        root.addWidget(self.sidebar)

        right = QVBoxLayout()

        self.topbar = TopBar()
        right.addWidget(self.topbar)
        self.topbar.setObjectName("TopBar")
        self.topbar.setFixedHeight(60)

        top_layout = QHBoxLayout(topbar)

        title = QLabel("🌴 PalmERP Enterprise")
        title.setObjectName("Title")

        top_layout.addWidget(title)
        top_layout.addStretch()

        right.addWidget(topbar)

        self.stack = QStackedWidget()

        self.dashboard = DashboardPage()

        self.stack.addWidget(self.dashboard)

        right.addWidget(self.stack)

        root.addLayout(right)