from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
)


class DashboardWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("PalmERP Enterprise")
        self.resize(1200, 700)

        self.create_ui()

    def create_ui(self):

        self.setStyleSheet("""
            QWidget{
                background:white;
                font-size:14px;
                font-family:Segoe UI;
            }

            QLabel#Title{
                font-size:28px;
                font-weight:bold;
                color:#2E7D32;
            }

            QLabel#Subtitle{
                color:#777777;
                font-size:14px;
            }

            QFrame{
                background:white;
                border:1px solid #DDDDDD;
                border-radius:10px;
            }

            QPushButton{
                background:#2E7D32;
                color:white;
                border:none;
                border-radius:8px;
                padding:10px;
                font-size:14px;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#388E3C;
            }
        """)

        main_layout = QVBoxLayout()

        # Title

        title = QLabel("🌴 PalmERP Enterprise")
        title.setObjectName("Title")

        subtitle = QLabel("Palm Oil Purchasing & Settlement ERP")
        subtitle.setObjectName("Subtitle")

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        main_layout.addSpacing(20)

        # Cards

        card_layout = QHBoxLayout()

        supplier_card = self.create_card(
            "Suppliers",
            "1,256"
        )

        purchase_card = self.create_card(
            "Today's FFB",
            "320 MT"
        )

        advance_card = self.create_card(
            "Advance",
            "RM 35,800"
        )

        settlement_card = self.create_card(
            "Settlement",
            "RM 125,000"
        )

        card_layout.addWidget(supplier_card)
        card_layout.addWidget(purchase_card)
        card_layout.addWidget(advance_card)
        card_layout.addWidget(settlement_card)

        main_layout.addLayout(card_layout)

        main_layout.addSpacing(30)

        self.supplier_button = QPushButton("Supplier Master")
        self.supplier_button.setFixedHeight(45)

        self.supplier_button.clicked.connect(
            self.open_supplier
        )

        main_layout.addWidget(self.supplier_button)

        main_layout.addStretch()

        self.setLayout(main_layout)

    def create_card(self, title, value):

        frame = QFrame()

        layout = QVBoxLayout(frame)

        lbl_title = QLabel(title)
        lbl_title.setStyleSheet(
            "font-size:14px;color:gray;"
        )

        lbl_value = QLabel(value)
        lbl_value.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#2E7D32;
        """)

        layout.addWidget(lbl_title)
        layout.addWidget(lbl_value)

        return frame

    def open_supplier(self):

        from ui.supplier.supplier_window import SupplierWindow

        self.supplier = SupplierWindow()
        self.supplier.show()