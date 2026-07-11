from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
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
            "PalmERP Enterprise Dashboard"
        )


        self.supplier_button = QPushButton(
            "Supplier Master"
        )


        self.supplier_button.clicked.connect(
            self.open_supplier
        )


        layout = QVBoxLayout()


        layout.addWidget(title)

        layout.addWidget(
            self.supplier_button
        )


        self.setLayout(layout)



    def open_supplier(self):

        from ui.supplier.supplier_window import SupplierWindow


        self.supplier = SupplierWindow()


        self.supplier.show()