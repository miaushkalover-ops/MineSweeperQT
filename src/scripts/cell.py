from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt, pyqtSignal 

from scripts.styles import Styles

class Cell(QPushButton):
    game_over_signal = pyqtSignal()
    run_bfs_signal = pyqtSignal(tuple)
    cell_opened = pyqtSignal(object)     # count safe opened cells
    left_clicked = pyqtSignal(tuple)     # window handles left click (first-click-safe)

    def __init__(
        self,
        position: tuple[int, int] = (0, 0),
        is_mine: bool = False,
        is_open: bool = False,
        value: str = '0',
        is_barrier: bool = False,
    ) -> None:
        super().__init__()
        self.position = position
        self.is_mine = is_mine
        self.is_open = is_open
        self.value = value
        self.is_barrier = is_barrier
        self.setStyleSheet(Styles.button_style_1.value)

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            if not self.is_open and self.text() != '🚩':
                self.left_clicked.emit(self.position)
            return

        if event.button() == Qt.MouseButton.RightButton:
            self.set_flag()
            return

    def set_flag(self) -> None:
        if self.is_open:
            return

        w = self.window()
        if hasattr(w, "sounds"):
            w.sounds.play_flag()
        self.setText('' if self.text() == '🚩' else '🚩')

    def open_cell_normal(self) -> None:
        if self.is_open or self.text() == '🚩':
            return

        if self.is_mine:
            self.setText('🧨')
            self.setStyleSheet(Styles.button_style_2.value)
            self.is_open = True
            self.setDisabled(True)
            w = self.window()
            if hasattr(w, "sounds"):
                w.sounds.play_boom()
            self.game_over_signal.emit()
            return

        if self.value == '0':
            self.run_bfs_signal.emit(self.position)
            return

        self.setText(self.value)
        self.is_open = True
        self.setDisabled(True)
        self.set_value_style()
        w = self.window()
        if hasattr(w, "sounds"):
            w.sounds.play_open()
        self.cell_opened.emit(self)

    def open_by_bfs(self) -> None:
        if self.is_open or self.text() == '🚩' or self.is_mine:
            return

        self.setText(self.value if self.value != '0' else '')
        self.is_open = True
        self.setDisabled(True)
        self.set_value_style()
        w = self.window()
        if hasattr(w, "sounds"):
            w.sounds.play_open()
        self.cell_opened.emit(self)

    def reveal(self) -> None:
        if self.is_open:
            return
        if self.is_mine:
            self.setText('🧨')
            self.setStyleSheet(Styles.button_style_2.value)
        else:
            self.setText(self.value if self.value != '0' else '')
            self.set_value_style()

        self.is_open = True
        self.setDisabled(True)

    def set_value_style(self) -> None:
        if self.value not in '0*':
            self.setStyleSheet(Styles.value_styles.value[self.value])