from PySide6.QtWidgets import QApplication

from ui.login.login_window import LoginWindow


app = QApplication([])


window = LoginWindow()

window.show()


app.exec()