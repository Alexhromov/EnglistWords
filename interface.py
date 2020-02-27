import random
import sys

from PyQt5 import QtGui
from PyQt5 import QtWidgets

import Config
import Exploper
import UI.AnkiSetup as AnkiS
import UI.menuV2 as Menu
from widgets import Anki, writing_words, check_letters


# Todo: After widgets close renew counter at main window
# Todo: Auto window size
# Todo: Open file: do flag check file; do function for download into base
# Todo: Base for save words


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.base = Config.base
        self.wordcount = Config.wordcount

        self.ui = Menu.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textEdit.setReadOnly(True)
        self.ui.pushButton_3.setText("Letter check")
        self.ui.textEdit.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))
        self.ui.label_3.setText(str(self.wordcount))
        self.ui.checkbox.setChecked(True)

        # подключение кнопок
        self.ui.pushButton_6.clicked.connect(self.setup)
        self.ui.pushButton_2.clicked.connect(Anki.RepeatWords)
        self.ui.pushButton_4.clicked.connect(writing_words.Main)
        self.ui.pushButton_3.clicked.connect(check_letters.Main)
        self.ui.pushButton_5.clicked.connect(Exploper.App)
        self.ui.pushButton_5.clicked.connect(self.show_words)
        self.ui.pushButton_clear.clicked.connect(self.clearText)

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

        def check_text():

            try:
                wordcount = int(self.uisetup.lineEdit.text())
                if not wordcount:
                    raise ValueError

            except ValueError:
                return 1

            return wordcount

        self.wordcount = check_text()

        self.write_to_base()
        self.ui.label_3.setText(str(self.wordcount))
        Config.wordcount = self.wordcount
        self.windowsetup.close()

    def clearText(self):
        self.ui.textEdit.clear()
        Config.words.clear()

    def show_words(self):

        if self.ui.checkbox.isChecked():
            for file in Config.words:
                with open(file, encoding="utf-8") as w:
                    f = w.readlines()
                    try:

                        for line in f:
                            text = line.rstrip("\n").rstrip().split("\t")
                            text = text[0] + text[1]
                    except IndexError:
                        Config.words.clear()
                        break

        if Config.words:
            self.ui.textEdit.setText(", ".join([str(elem[elem.rfind("/") + 1:]) for elem in Config.words]))
        else:
            self.ui.textEdit.setText("None file")

    def write_to_base(self):

        def fill_base():
            self.base.clear()
            for file in Config.words:
                with open(file, encoding="utf-8") as w:
                    f = w.readlines()
                    count = self.wordcount
                    if len(f) + len(self.base) < count:
                        count = len(f) + len(self.base)

                    while len(self.base) < count:
                        text = random.choice(f)
                        text = text.rstrip("\n").rstrip().split("\t")
                        self.base[text[0]] = text[1]

        fill_base()
        self.wordcount = len(self.base)


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())