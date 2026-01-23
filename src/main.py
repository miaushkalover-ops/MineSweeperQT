from PyQt6.QtWidgets import QApplication, QDialog

from sys import argv

from scripts.dialog import GameSetupDialog
from scripts.game import Mine_Sweeper


def main() -> None:
    app = QApplication(argv)

    # Show setup first
    dlg = GameSetupDialog(default_rows=13, default_cols=9, default_mines=27)
    if dlg.exec() != QDialog.DialogCode.Accepted:
        return

    r, c, m = dlg.get_values()
    window = Mine_Sweeper(r, c, m)
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
