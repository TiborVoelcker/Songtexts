# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
import sys
from SpotifyHelper import SpotifyHelper
from Lyrics import Lyrics

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_GUI()
        self.sp = SpotifyHelper()
        self.l = Lyrics("******")
        self.current_title = ""

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(3000)

    def init_GUI(self):
        self.setWindowTitle = "Songtext"
        self.verticalLayout = QtWidgets.QVBoxLayout(self)

        self.chat = QtWidgets.QTextEdit(self)
        self.verticalLayout.addWidget(self.chat)
        self.chat.setReadOnly(True)

        self.show()

    def update(self):
        data, title, artist = self.sp.get_current_title()
        if data:
            if title != self.current_title:
                self.current_title = title
                lyrics = self.l.get_lyrics(artist, title)
                if lyrics:
                    self.chat.setPlainText(title+" - "+artist+":\n\n"+lyrics)
                else: self.chat.setPlainText(title+" - "+artist+":\n\nKeine Lyrics vorhanden.")
        else:
            self.chat.setPlainText("Spotify nicht offen oder es wird kein Song abgespielt.")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
