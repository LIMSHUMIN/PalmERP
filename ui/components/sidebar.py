from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout
)


class Sidebar(QFrame):

    def __init__(self):

        super().__init__()

        self.setObjectName("Sidebar")
        self.setFixedWidth(220)

        layout = QVBoxLayout(self)

        # ==========================
        # Logo
        # ==========================

        logo = QLabel("🌴")
        logo.setAlignment(Qt.AlignCenter)
        logo.setStyleSheet("""
            font-size:42px;
            margin-top:20px;
        """)

        title = QLabel("PalmERP")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
            color:#2E7D32;
            margin-bottom:20px;
        """)

        layout.addWidget(logo)
        layout.addWidget(title)

        # ==========================
        # Menu Buttons
        # ==========================

        self.btn_dashboard = QPushButton("🏠 Dashboard")
        self.btn_supplier = QPushButton("👨 Supplier")
        self.btn_purchase = QPushButton("🚛 Purchase")
        self.btn_harvest = QPushButton("🌱 Harvest")
        self.btn_fertiliser = QPushButton("🧪 Fertiliser")
        self.btn_advance = QPushButton("💰 Advance")
        self.btn_settlement = QPushButton("📄 Settlement")
        self.btn_reports = QPushButton("📊 Reports")
        self.btn_settings = QPushButton("⚙ Settings")
        self.btn_logout = QPushButton("🚪 Logout")

        buttons = [
            self.btn_dashboard,
            self.btn_supplier,
            self.btn_purchase,
            self.btn_harvest,
            self.btn_fertiliser,
            self.btn_advance,
            self.btn_settlement,
            self.btn_reports,
            self.btn_settings,
            self.btn_logout,
        ]

        for button in buttons:
            button.setCheckable(True)
            button.setMinimumHeight(45)
            layout.addWidget(button)

        self.btn_dashboard.setChecked(True)

        layout.addStretch()