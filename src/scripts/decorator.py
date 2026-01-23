from PyQt6.QtWidgets import QMessageBox, QApplication

from functools import wraps

def dialog_decorator(title: str):
    def decorator(func):
        @wraps(func)
        def wrapper(self):
            # run logic first (lose: reveal, win: nothing special)
            func(self)

            msg_box = QMessageBox()
            msg_box.setWindowTitle(title)
            msg_box.setText('Would you like restart or cancel game ?')

            restart_button = msg_box.addButton("Restart", QMessageBox.ButtonRole.AcceptRole)
            cancel_button = msg_box.addButton("Cancel", QMessageBox.ButtonRole.RejectRole)

            msg_box.exec()

            if msg_box.clickedButton() == restart_button:
                self.restart_game()
            elif msg_box.clickedButton() == cancel_button:
                QApplication.quit()

        return wrapper
    return decorator