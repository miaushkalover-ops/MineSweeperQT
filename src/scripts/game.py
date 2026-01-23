from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout
from PyQt6.QtCore import QSize

from random import randint
from collections import deque

from scripts.decorator import dialog_decorator
from scripts.cell import Cell
from scripts.sound import SoundManager
from scripts.styles import Styles


class Mine_Sweeper(QMainWindow):
    def __init__(self, rows_, cols_, mines_) -> None:
        super().__init__()

        self.sounds = SoundManager()

        self.rows = rows_
        self.columns = cols_
        self.mines = mines_

        self.counter = 0
        self.first_click = True
        self.game_active = True

        self.set_UI()
        self.reset_field_empty()
        self.connect_signals()

    def set_UI(self) -> None:
        widget = QWidget()
        main_layout = QGridLayout()

        self.setFixedSize(QSize(self.columns * 40, self.rows * 40))
        self.setWindowTitle('MineSweeper QT')

        self.field: list[list[Cell]] = [
            [Cell(is_barier=True) for _ in range(self.columns + 2)],
            *[[Cell(is_barier=True), *[Cell() for _ in range(self.columns)],
                Cell(is_barier=True)] for _ in range(self.rows)],
            [Cell(is_barier=True) for _ in range(self.columns + 2)],
        ]

        for i in range(1, self.rows + 1):
            for j in range(1, self.columns + 1):
                main_layout.addWidget(self.field[i][j], i, j)
                self.field[i][j].position = (i, j)

        self.setStyleSheet(Styles.main_window_style.value)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def reset_field_empty(self) -> None:
        self.counter = 0
        self.first_click = True
        self.game_active = True

        for i in range(1, self.rows + 1):
            for j in range(1, self.columns + 1):
                c = self.field[i][j]
                c.is_mine = False
                c.is_open = False
                c.value = '0'
                c.setText('')
                c.setDisabled(False)
                c.setStyleSheet(Styles.button_style_1.value)

    def connect_signals(self) -> None:
        for i in range(1, self.rows + 1):
            for j in range(1, self.columns + 1):
                cell = self.field[i][j]
                cell.game_over_signal.connect(self.show_game_over_dialog)
                cell.run_bfs_sinal.connect(self.breadth_first_search)
                cell.cell_opened.connect(self.on_cell_opened)
                cell.left_clicked.connect(self.on_left_click)

    def on_left_click(self, pos: tuple[int, int]) -> None:
        if not self.game_active:
            return

        if self.first_click:
            self.first_click = False
            self.place_mines_avoiding(pos)
            self.compute_numbers()

        self.field[pos[0]][pos[1]].open_cell_normal()

    def place_mines_avoiding(self, click_pos: tuple[int, int]) -> None:
        ci, cj = click_pos
        forbidden = set()
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                ni, nj = ci + di, cj + dj
                if 1 <= ni <= self.rows and 1 <= nj <= self.columns:
                    forbidden.add((ni, nj))

        mines_set = set()
        while len(mines_set) < self.mines:
            m = (randint(1, self.rows), randint(1, self.columns))
            if m in forbidden:
                continue
            mines_set.add(m)

        for mi, mj in mines_set:
            self.field[mi][mj].is_mine = True
            self.field[mi][mj].value = '*'

    def compute_numbers(self) -> None:
        for i in range(1, self.rows + 1):
            for j in range(1, self.columns + 1):
                if self.field[i][j].is_mine:
                    continue
                self.field[i][j].value = str([
                    self.field[i - 1][j - 1].is_mine, self.field[i - 1][j].is_mine,
                    self.field[i - 1][j + 1].is_mine, self.field[i][j - 1].is_mine,
                    self.field[i][j + 1].is_mine, self.field[i + 1][j - 1].is_mine,
                    self.field[i + 1][j].is_mine, self.field[i + 1][j + 1].is_mine
                ].count(True))

    def on_cell_opened(self, cell: Cell) -> None:
        if not self.game_active:
            return

        self.counter += 1
        if self.counter == self.rows * self.columns - self.mines:
            self.show_winner_dialog()

    @dialog_decorator(title='You lost !')
    def show_game_over_dialog(self) -> None:
        self.game_active = False
        self.reveal_full_field()

    @dialog_decorator(title='You won !')
    def show_winner_dialog(self) -> None:
        self.game_active = False

    def restart_game(self) -> None:
        self.reset_field_empty()

    def breadth_first_search(self, position: tuple[int, int]) -> None:
        if not self.game_active:
            return

        q = deque([position])
        visited = {position}

        while q:
            i, j = q.popleft()
            current = self.field[i][j]

            if current.is_open:
                continue

            current.open_by_bfs()

            if current.value != '0':
                continue

            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if not (1 <= ni <= self.rows and 1 <= nj <= self.columns):
                        continue
                    if (ni, nj) in visited:
                        continue

                    neighbor = self.field[ni][nj]
                    if neighbor.is_mine or neighbor.is_barier:
                        continue

                    visited.add((ni, nj))
                    q.append((ni, nj))

    def reveal_full_field(self) -> None:
        for i in range(1, self.rows + 1):
            for j in range(1, self.columns + 1):
                self.field[i][j].reveal()
