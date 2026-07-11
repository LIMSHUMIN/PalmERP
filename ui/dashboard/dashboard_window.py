from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)


class DashboardWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "PalmERP Dashboard"
        )

        self.resize(
            900,
            600
        )

        self.create_ui()


    def create_ui(self):

        title = QLabel(
            "Welcome to PalmERP Enterprise"
        )

        info = QLabel(
            """
            Dashboard

            Purchase Today:
            RM 0.00

            Outstanding Advance:
            RM 0.00

            Supplier Count:
            0
            """
        )


        layout = QVBoxLayout()

        layout.addWidget(title)

        layout.addWidget(info)

        self.setLayout(layout)