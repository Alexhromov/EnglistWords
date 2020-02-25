"""Widget for learning foreign word, simply Anki
"""
import random
import sys

from PyQt5 import QtGui
from PyQt5 import QtWidgets

import Config
import UI.Anki as Anki


class RepeatWords(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.setMinimumSize(500, 400)

        self.base = Config.base
        self.wordcount = Config.wordcount

        self.window = QtWidgets.QWidget()
        self.uia = Anki.Ui_Form()
        self.uia.setupUi(self.window)
        self.window.setWindowTitle("Anki")

        self.uia.pushButton.setShortcut("Enter")
        self.uia.pushButton_2.setShortcut("1")
        self.uia.pushButton_3.setShortcut("2")

        key = random.choice(list(self.base.keys()))
        self.key = key

        self.uia.pushButton_2.hide()
        self.uia.pushButton_3.hide()
        self.uia.textBrowser.hide()

        self.uia.label.setText(str(self.wordcount))
        self.uia.textEdit.setText(key)
        self.uia.textEdit.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))

        self.uia.textBrowser.setText(self.base[key])
        self.uia.textBrowser.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))
        self.uia.pushButton.clicked.connect(self.showall)
        self.uia.pushButton_2.clicked.connect(lambda: self.popAnkiCard())
        self.uia.pushButton_2.clicked.connect(lambda: self.nextcard())
        self.uia.pushButton_3.clicked.connect(lambda: self.nextcard())

        self.window.show()

    def popAnkiCard(self):
        if len(self.base) == 0:
            pass
        else:
            self.base.pop(self.key)
            self.wordcount -= 1
            self.uia.label.setText(str(self.wordcount))

    def nextcard(self):
        if self.wordcount == 0:
            self.uia.pushButton_2.setEnabled(False)
            self.uia.textBrowser.setStyleSheet("background-color: rgb(20, 160, 0)")
            self.uia.textBrowser.setText("All words are complete")
            self.uia.pushButton.setText("OK")
            self.uia.pushButton.setShortcut("Enter")
            self.uia.pushButton.clicked.connect(lambda: self.window.close())
            self.uia.textEdit.hide()
            self.uia.pushButton_2.hide()
            self.uia.pushButton_3.hide()

        else:

            key = random.choice(list(self.base.keys()))
            self.key = key
            self.uia.pushButton_2.hide()
            self.uia.pushButton_3.hide()
            self.uia.textBrowser.hide()

            self.uia.textEdit.setText(key)
            self.uia.textEdit.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))
            self.uia.textBrowser.setText(self.base[key])
            self.uia.textBrowser.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))

    def showall(self):

        self.uia.pushButton_2.show()
        self.uia.pushButton_3.show()
        self.uia.textBrowser.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = RepeatWords()

    application.show()

    sys.exit(app.exec())
