from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl

import os

class SoundManager:
    def __init__(self) -> None:
        base = os.path.dirname(os.path.abspath(__file__))

        self.flag = QSoundEffect()
        self.flag.setVolume(0.99)
        self.flag.setSource(QUrl.fromLocalFile(
            os.path.join(base, '../assets/flag.wav')
        ))

        self.open = QSoundEffect()
        self.open.setVolume(0.55)
        self.open.setSource(QUrl.fromLocalFile(
            os.path.join(base, '../assets/shovel.wav')
        ))

        self.boom = QSoundEffect()
        self.boom.setVolume(0.55)
        self.boom.setSource(QUrl.fromLocalFile(
            os.path.join(base, '../assets/boom.wav')
        ))

    def play_flag(self) -> None:
        self.flag.stop()
        self.flag.play()

    def play_open(self) -> None:
        self.open.stop()
        self.open.play()

    def play_boom(self) -> None:
        self.boom.stop()
        self.boom.play()