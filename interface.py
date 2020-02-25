import random
import sys

from PyQt5 import QtGui
from PyQt5 import QtWidgets

import Config
import UI.AnkiSetup as AnkiS
import UI.menuV2 as Menu
from widgets import Anki, writing_words, check_letters


# Todo: After widgets close renew counter at main window
# Todo: Setup check if program can't read so many word (error or max of exist words)
# Todo: Auto window size


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.base = Config.base
        self.wordcount = Config.wordcount
        self.write_to_base("English Dota 2")

        self.ui = Menu.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textEdit.setReadOnly(True)
        self.ui.pushButton_3.setText("Letter check")
        self.ui.textEdit.setText("English Dota 2")
        self.ui.textEdit.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))
        self.ui.label_3.setText(str(self.wordcount))

        # подключение кнопок
        self.ui.pushButton_6.clicked.connect(lambda: self.setup())
        self.ui.pushButton_2.clicked.connect(Anki.RepeatWords)
        self.ui.pushButton_4.clicked.connect(writing_words.Main)
        self.ui.pushButton_3.clicked.connect(check_letters.Main)

    def setup(self):

        self.windowsetup = QtWidgets.QMainWindow()
        self.uisetup = AnkiS.Ui_Form()
        self.uisetup.setupUi(self.windowsetup)
        self.windowsetup.setWindowTitle("Setup")
        self.windowsetup.setMinimumSize(400, 400)
        self.uisetup.pushButton.clicked.connect(self.getinfoas)
        self.uisetup.pushButton.setShortcut("Return")
        self.windowsetup.show()

    def getinfoas(self):
        self.wordcount = int(self.uisetup.lineEdit.text())
        self.write_to_base("English Dota 2")
        self.ui.label_3.setText(str(self.wordcount))
        Config.wordcount = self.wordcount
        self.windowsetup.close()

    def write_to_base(self, name):
        def fill_base():
            self.base.clear()
            with open("Words\\" + name + ".txt", encoding="utf-8") as w:
                f = w.readlines()
                if len(f) < self.wordcount:
                    self.wordcount = len(f)

                while len(self.base) < self.wordcount:
                    text = random.choice(f)
                    text = text.rstrip("\n").rstrip().split("\t")
                    self.base[text[0]] = text[1]

        fill_base()

        self.wordcount = len(self.base)


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())