from PySide6.QtWidgets import (
    QWidget,
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
            1000,
            600
        )


        self.create_ui()

        self.load_suppliers()



    def create_ui(self):


        # =====================
        # Search
        # =====================

        self.search_box = QLineEdit()

        self.search_box.setPlaceholderText(
            "Search supplier..."
        )


        self.search_button = QPushButton(
            "Search"
        )


        self.search_button.clicked.connect(
            self.search_supplier
        )


        search_layout = QHBoxLayout()

        search_layout.addWidget(
            self.search_box
        )

        search_layout.addWidget(
            self.search_button
        )



        # =====================
        # Supplier Form
        # =====================

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



        # =====================
        # Buttons
        # =====================

        self.new_button = QPushButton(
            "New"
        )


        self.save_button = QPushButton(
            "Save New"
        )


        self.update_button = QPushButton(
            "Update"
        )


        self.delete_button = QPushButton(
            "Delete"
        )


        self.deactivate_button = QPushButton(
            "Deactivate"
        )



        self.new_button.clicked.connect(
            self.clear_form
        )


        self.save_button.clicked.connect(
            self.save_supplier
        )


        self.update_button.clicked.connect(
            self.update_supplier
        )


        self.delete_button.clicked.connect(
            self.delete_supplier
        )


        self.deactivate_button.clicked.connect(
            self.deactivate_supplier
        )



        button_layout = QHBoxLayout()


        button_layout.addWidget(
            self.new_button
        )


        button_layout.addWidget(
            self.save_button
        )


        button_layout.addWidget(
            self.update_button
        )


        button_layout.addWidget(
            self.delete_button
        )


        button_layout.addWidget(
            self.deactivate_button
        )



        # =====================
        # Table
        # =====================

        self.table = QTableWidget()

        self.table.setColumnCount(6)


        self.table.setHorizontalHeaderLabels(
            [
                "ID",
                "Code",
                "Name",
                "Phone",
                "Address",
                "Active"
            ]
        )


        self.table.cellClicked.connect(
            self.select_supplier
        )



        # =====================
        # Layout
        # =====================

        layout = QVBoxLayout()


        layout.addLayout(
            search_layout
        )


        layout.addWidget(
            self.code
        )


        layout.addWidget(
            self.name
        )


        layout.addWidget(
            self.phone
        )


        layout.addWidget(
            self.address
        )


        layout.addLayout(
            button_layout
        )


        layout.addWidget(
            self.table
        )


        self.setLayout(
            layout
        )



    # =====================
    # Load Supplier Data
    # =====================

    def load_suppliers(self):

        suppliers = (
            self.service
            .get_all_suppliers()
        )


        self.show_data(
            suppliers
        )



    def show_data(
        self,
        suppliers
    ):

        self.table.setRowCount(
            len(suppliers)
        )


        for row, supplier in enumerate(suppliers):

            for col, value in enumerate(supplier):

                self.table.setItem(
                    row,
                    col,
                    QTableWidgetItem(
                        str(value)
                    )
                )



    # =====================
    # Select Row
    # =====================

    def select_supplier(
        self,
        row,
        column
    ):


        self.selected_id = (
            self.table
            .item(row,0)
            .text()
        )


        self.code.setText(
            self.table.item(row,1).text()
        )


        self.name.setText(
            self.table.item(row,2).text()
        )


        self.phone.setText(
            self.table.item(row,3).text()
        )


        self.address.setText(
            self.table.item(row,4).text()
        )



    # =====================
    # Add New Supplier
    # =====================

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



    # =====================
    # Update Supplier
    # =====================

    def update_supplier(self):

        if self.selected_id is None:

            QMessageBox.warning(
                self,
                "Warning",
                "Please select supplier first"
            )

            return



        result = self.service.update_supplier(

            self.selected_id,

            self.code.text(),

            self.name.text(),

            self.phone.text(),

            self.address.text()

        )


        if result:

            QMessageBox.information(
                self,
                "Success",
                "Supplier updated"
            )


            self.load_suppliers()



    # =====================
    # Permanent Delete
    # =====================

    def delete_supplier(self):


        if self.selected_id is None:

            QMessageBox.warning(
                self,
                "Warning",
                "Please select supplier first"
            )

            return



        confirm = QMessageBox.question(
            self,
            "Confirm Delete",
            "Delete this supplier permanently?"
        )


        if confirm == QMessageBox.Yes:


            result = self.service.hard_delete_supplier(
                self.selected_id
            )


            if result:

                QMessageBox.information(
                    self,
                    "Success",
                    "Supplier deleted"
                )


                self.load_suppliers()

                self.clear_form()



    # =====================
    # Deactivate Supplier
    # =====================

    def deactivate_supplier(self):


        if self.selected_id is None:

            QMessageBox.warning(
                self,
                "Warning",
                "Please select supplier first"
            )

            return



        self.service.delete_supplier(
            self.selected_id
        )


        QMessageBox.information(
            self,
            "Success",
            "Supplier deactivated"
        )


        self.load_suppliers()

        self.clear_form()



    # =====================
    # Search
    # =====================

    def search_supplier(self):


        keyword = self.search_box.text()


        result = (
            self.service
            .search_supplier(keyword)
        )


        self.show_data(
            result
        )



    # =====================
    # Clear
    # =====================

    def clear_form(self):

        self.selected_id = None

        self.code.clear()

        self.name.clear()

        self.phone.clear()

        self.address.clear()