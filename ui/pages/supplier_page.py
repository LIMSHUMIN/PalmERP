from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)


class SupplierPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Supplier Management")
        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        layout.addStretch()