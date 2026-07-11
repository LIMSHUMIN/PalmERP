from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox
)

from database.connection import get_connection


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("PalmERP Login")
        self.setFixedSize(400, 300)

        self.create_ui()


    def create_ui(self):

        self.title = QLabel("PalmERP Enterprise")
        
        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")

        self.login_button.clicked.connect(self.login)


        layout = QVBoxLayout()

        layout.addWidget(self.title)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.login_button)

        self.setLayout(layout)


    def login(self):

        username = self.username.text()
        password = self.password.text()


        if username == "" or password == "":
            QMessageBox.warning(
                self,
                "Login",
                "Please enter username and password"
            )
            return


        conn = get_connection()

        if conn:

            cursor = conn.cursor()

            sql = """
            SELECT *
            FROM Users
            WHERE UserName = ?
            AND PasswordHash = ?
            AND Active = 1
            """

            cursor.execute(
                sql,
                username,
                password
            )

            user = cursor.fetchone()


            if user:

                QMessageBox.information(
                    self,
                    "Login",
                    "Login Successful"
                )

                self.open_dashboard()

            else:

                QMessageBox.warning(
                    self,
                    "Login Failed",
                    "Invalid username or password"
                )

            conn.close()


    def open_dashboard(self):

        from ui.dashboard.dashboard_window import DashboardWindow

        self.dashboard = DashboardWindow()

        self.dashboard.show()

        self.hide()