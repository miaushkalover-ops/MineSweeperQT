from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl

import os

class SoundManager:
    def __init__(self):
        base = os.path.dirname(os.path.abspath(__file__))

        self.flag = QSoundEffect()
        self.flag.setSource(QUrl.fromLocalFile(os.path.join(base, "../assets/flag.wav")))
        self.flag.setVolume(0.99)

        self.open = QSoundEffect()
        self.open.setSource(QUrl.fromLocalFile(os.path.join(base, "../assets/shovel.wav")))
        self.open.setVolume(0.55)

        self.boom = QSoundEffect()
        self.boom.setSource(QUrl.fromLocalFile(os.path.join(base, "../assets/boom.wav")))
        self.boom.setVolume(0.55)

    def play_flag(self):
        self.flag.stop()
        self.flag.play()

    def play_open(self):
        self.open.stop()
        self.open.play()

    def play_boom(self):
        self.boom.stop()
        self.boom.play()
