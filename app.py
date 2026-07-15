import sys

from PySide6.QtWidgets import QApplication

from ui.auth.login_window import LoginWindow


def main():

    app = QApplication(sys.argv)

    window = LoginWindow()

    with open("resources/style/style.qss", "r") as f:
    app.setStyleSheet(f.read())
    
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":

    main()