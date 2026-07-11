from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox
)

from services.supplier_service import SupplierService


class SupplierWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.service = SupplierService()

        self.selected_id = None

        self.setWindowTitle(
            "PalmERP - Supplier Master"
        )

        self.resize(
            900,
            600
        )

        self.create_ui()

        self.load_suppliers()


    def create_ui(self):

        self.code = QLineEdit()
        self.code.setPlaceholderText(
            "Supplier Code"
        )


        self.name = QLineEdit()
        self.name.setPlaceholderText(
            "Supplier Name"
        )


        self.phone = QLineEdit()
        self.phone.setPlaceholderText(
            "Phone"
        )


        self.address = QLineEdit()
        self.address.setPlaceholderText(
            "Address"
        )


        self.save_button = QPushButton(
            "Save"
        )

        self.new_button = QPushButton(
            "New"
        )


        self.save_button.clicked.connect(
            self.save_supplier
        )

        self.new_button.clicked.connect(
            self.clear_form
        )


        form = QHBoxLayout()

        form.addWidget(self.code)
        form.addWidget(self.name)
        form.addWidget(self.phone)
        form.addWidget(self.address)


        buttons = QHBoxLayout()

        buttons.addWidget(
            self.new_button
        )

        buttons.addWidget(
            self.save_button
        )


        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels(
            [
                "ID",
                "Code",
                "Name",
                "Phone",
                "Address"
            ]
        )


        layout = QVBoxLayout()

        layout.addLayout(form)

        layout.addLayout(buttons)

        layout.addWidget(
            self.table
        )


        self.setLayout(layout)



    def load_suppliers(self):

        suppliers = (
            self.service
            .get_all_suppliers()
        )


        self.table.setRowCount(
            len(suppliers)
        )


        for row, supplier in enumerate(suppliers):

            for col, value in enumerate(supplier[:5]):

                self.table.setItem(
                    row,
                    col,
                    QTableWidgetItem(
                        str(value)
                    )
                )



    def save_supplier(self):

        result = self.service.add_supplier(
            self.code.text(),
            self.name.text(),
            self.phone.text(),
            self.address.text()
        )


        if result:

            QMessageBox.information(
                self,
                "Success",
                "Supplier saved"
            )

            self.load_suppliers()

            self.clear_form()

        else:

            QMessageBox.warning(
                self,
                "Error",
                "Cannot save supplier"
            )



    def clear_form(self):

        self.code.clear()

        self.name.clear()

        self.phone.clear()

        self.address.clear()