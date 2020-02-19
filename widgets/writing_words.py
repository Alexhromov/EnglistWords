"""Info here"""

import random
import sys

from PyQt5 import QtWidgets

import Config
import UI.text2 as text2


class Main(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.base = Config.base
        self.wordcount = Config.wordcount

        self.window2 = QtWidgets.QWidget()
        self.ui2 = text2.Ui_Form()
        self.ui2.setupUi(self.window2)
        self.window2.setWindowTitle("Text test")

        key = random.choice(list(self.base.keys()))
        self.key = key

        self.ui2.label.setText(str(self.wordcount))
        self.ui2.lineEdit.setText(self.base[key])

        self.ui2.pushButton.setShortcut("Return")
        self.ui2.pushButton_1.setShortcut("Return")
        self.ui2.pushButton_1.setEnabled(False)
        self.ui2.pushButton_1.close()
        self.ui2.pushButton.clicked.connect(lambda: self.b2checkWord())
        self.ui2.pushButton_1.clicked.connect(lambda: self.b2nextCard())

        self.window2.show()

    def b2nextCard(self):
        self.ui2.lineEdit_2.clear()
        self.ui2.lineEdit_2.setStyleSheet("color: black")

        self.ui2.pushButton.setEnabled(True)
        self.ui2.pushButton.show()
        self.ui2.pushButton_1.setEnabled(False)
        self.ui2.pushButton_1.close()

        if self.wordcount == 0:
            self.ui2.lineEdit.setText("All words are complete")
            self.ui2.pushButton.setText("OK")
            # self.window2.close()
            self.ui2.pushButton.clicked.connect(lambda: self.window2.close())
            self.ui2.label.setText(str(self.wordcount))

        else:
            key = random.choice(list(self.base.keys()))
            self.key = key
            self.ui2.lineEdit.setText(self.base[key])

    def b2checkWord(self):
        answer = self.ui2.lineEdit_2.text()
        answer.lower()
        flag = True
        newstr = ""
        for i in range(len(self.key) - abs(len(self.key) - len(answer))):

            if self.key.lower()[i] != answer.lower()[i]:
                flag = False
            newstr += answer[i]

        self.ui2.lineEdit_2.setText(self.key + " -> " + newstr)

        if flag and answer != '':
            self.ui2.lineEdit_2.setStyleSheet("color: rgb(1, 255, 1)")
            self.base.pop(self.key)
            self.wordcount -= 1
            self.ui2.label.setText(str(self.wordcount))
        else:
            self.ui2.lineEdit_2.setStyleSheet("color: rgb(255, 1, 1)")

        self.ui2.pushButton_1.setEnabled(True)
        self.ui2.pushButton_1.show()
        self.ui2.pushButton.setEnabled(False)
        self.ui2.pushButton.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Main()
    application.show()

    sys.exit(app.exec())
