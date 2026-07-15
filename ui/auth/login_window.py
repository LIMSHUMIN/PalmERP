from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QVBoxLayout,
    QCheckBox
)

from services.user_service import UserService


class LoginWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.user_service = UserService()

        self.build_ui()

    def build_ui(self):

        self.setWindowTitle("PalmERP Login")

        self.resize(420, 520)

        layout = QVBoxLayout(self)

        layout.setSpacing(15)

        layout.setContentsMargins(50,40,50,40)

        logo = QLabel("🌴")

        logo.setAlignment(Qt.AlignCenter)

        logo.setStyleSheet("""
            font-size:60px;
        """)

        title = QLabel("PalmERP Enterprise")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#2E7D32;
        """)

        subtitle = QLabel("Palm Oil ERP Management System")

        subtitle.setAlignment(Qt.AlignCenter)

        subtitle.setStyleSheet("""
            color:gray;
        """)

        self.username = QLineEdit()

        self.username.setPlaceholderText("Username")

        self.password = QLineEdit()

        self.password.setPlaceholderText("Password")

        self.password.setEchoMode(QLineEdit.Password)

        self.remember = QCheckBox("Remember Me")

        self.login_button = QPushButton("Login")

        self.login_button.clicked.connect(
            self.login
        )

        layout.addWidget(logo)

        layout.addWidget(title)

        layout.addWidget(subtitle)

        layout.addSpacing(20)

        layout.addWidget(self.username)

        layout.addWidget(self.password)

        layout.addWidget(self.remember)

        layout.addWidget(self.login_button)

        layout.addStretch()

        self.setStyleSheet("""

        QWidget{

            background:white;

            font-size:14px;

        }

        QLineEdit{

            padding:10px;

            border:1px solid #cccccc;

            border-radius:8px;

        }

        QPushButton{

            background:#2E7D32;

            color:white;

            border:none;

            border-radius:8px;

            padding:12px;

            font-weight:bold;

        }

        QPushButton:hover{

            background:#43A047;

        }

        """)

    def login(self):

        username = self.username.text()

        password = self.password.text()

        user = self.user_service.login(
            username,
            password
        )

        if user is None:

            QMessageBox.warning(
                self,
                "Login",
                "Invalid username or password."
            )

            return

        from ui.main.main_window import MainWindow

        self.main = MainWindow()

        self.main.show()

        self.close()