from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtWidgets import QDialog, QSpinBox, QDialogButtonBox


class GameSetupDialog(QDialog):
    def __init__(self, default_rows=13, default_cols=9, default_mines=27, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Game Setup")

        layout = QVBoxLayout()

        row_line = QHBoxLayout()
        row_line.addWidget(QLabel("Rows:"))
        self.rows_spin = QSpinBox()
        self.rows_spin.setRange(5, 40)
        self.rows_spin.setValue(default_rows)
        row_line.addWidget(self.rows_spin)
        layout.addLayout(row_line)

        col_line = QHBoxLayout()
        col_line.addWidget(QLabel("Columns:"))
        self.cols_spin = QSpinBox()
        self.cols_spin.setRange(5, 30)
        self.cols_spin.setValue(default_cols)
        col_line.addWidget(self.cols_spin)
        layout.addLayout(col_line)

        mines_line = QHBoxLayout()
        mines_line.addWidget(QLabel("Mines:"))
        self.mines_spin = QSpinBox()
        self.mines_spin.setRange(1, 9999)
        self.mines_spin.setValue(default_mines)
        mines_line.addWidget(self.mines_spin)
        layout.addLayout(mines_line)

        self.hint_label = QLabel("")
        layout.addWidget(self.hint_label)

        self.rows_spin.valueChanged.connect(self._update_mines_limit)
        self.cols_spin.valueChanged.connect(self._update_mines_limit)
        self._update_mines_limit()

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)

    def _update_mines_limit(self):
        r = self.rows_spin.value()
        c = self.cols_spin.value()

        max_mines = max(1, r * c - 9)
        self.mines_spin.setMaximum(max_mines)
        if self.mines_spin.value() > max_mines:
            self.mines_spin.setValue(max_mines)

        self.hint_label.setText(f"Max mines for this size: {max_mines}")

    def get_values(self):
        return self.rows_spin.value(), self.cols_spin.value(), self.mines_spin.value()