import random
import sys

from PyQt5 import QtGui
from PyQt5 import QtWidgets

import Config
import UI.AnkiSetup as AnkiS
import UI.menuV2 as menu  # импорт нашего сгенерированного файла
from widgets import Anki, writing_words, check_letters


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.base = Config.base
        self.wordcount = Config.wordcount
        self.write_to_base("English Dota 2", self.wordcount)

        self.ui = menu.Ui_MainWindow()
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
        self.uisetup.pushButton.clicked.connect(lambda: self.getinfoas())
        self.uisetup.pushButton.setShortcut("Ctrl+Return")
        self.windowsetup.show()

    def getinfoas(self):
        self.wordcount = int(self.uisetup.textEdit.toPlainText())
        Config.wordcount = self.wordcount
        self.write_to_base("English Dota 2", self.wordcount)
        self.ui.label_3.setText(str(self.wordcount))
        self.windowsetup.close()

    def write_to_base(self, name, numb=3):

        self.base.clear()

        def random_line(afile):
            line = ""
            for num, aline in enumerate(afile, 2):
                if random.randrange(num):
                    continue
                line = aline
            return line

        for i in range(numb):  # Можливо не потрібна кількість елементів, тобто елементи повторюються
            with open("Words\\" + name + ".txt", encoding="utf-8") as w:
                line = random_line(w)
                text = line.rstrip("\n").rstrip().split("\t")
                self.base[text[0]] = text[1]

        self.wordcount = len(self.base)




app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())