import random
import sys

from PyQt5 import QtWidgets

import Config
import UI.text3 as text3


class Main(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.base = Config.base
        self.wordcount = Config.wordcount

        self.window3 = QtWidgets.QMainWindow()
        self.ui3 = text3.Ui_Form()
        self.ui3.setupUi(self.window3)
        self.window3.setWindowTitle("Letter check")

        self.key = random.choice(list(self.base.keys()))
        word = self.key.lower().split()
        self.ui3.values = [[i for i in word[j]] for j in range(len(word))]
        self.ui3.lcdNumber.display(self.wordcount)
        self.ui3.pushButton.setShortcut("Return")
        self.ui3.lineEdit.setText(self.base[self.key])

        self.ui3.pushButton.flag = True
        self.ui3.pushButton.clicked.connect(lambda: self.b3button())

        self.window3.show()

    def b3button(self):

        if self.ui3.pushButton.flag:
            self.b3checkWord()
        else:
            self.ui3.pushButton.flag = True
            if self.wordcount == 0:
                self.ui3.lineEdit.setText("All words are complete")
                self.ui3.pushButton.setText("OK")
                self.window3.close()
                self.ui3.lcdNumber.display(self.wordcount)

            else:
                def clearLayout(layout):
                    if layout != None:
                        while layout.count():
                            child = layout.takeAt(0)
                            if child.widget() is not None:
                                child.widget().deleteLater()
                            elif child.layout() is not None:
                                clearLayout(child.layout())

                self.ui3.lineEdit_2.clear()
                clearLayout(self.ui3.gridLayout)
                key = random.choice(list(self.base.keys()))
                self.key = key
                word = self.key.lower().split()
                self.ui3.values = [[i for i in word[j]] for j in range(len(word))]

                self.ui3.lineEdit.setText(self.base[key])

    def b3checkWord(self):
        answer = self.ui3.lineEdit_2.text()
        answer = answer.lower().split()
        flag = True
        for i in range(len(self.ui3.values)):
            for j in range(len(self.ui3.values[i])):
                while True:
                    try:

                        if answer[i][j] == self.ui3.values[i][j]:
                            button = QtWidgets.QPushButton(self.ui3.values[i][j])
                            button.setStyleSheet("background-color: rgb(2, 255, 2);")
                            self.ui3.gridLayout.addWidget(button, *(i, j))
                        else:
                            flag = False
                            button = QtWidgets.QPushButton(self.ui3.values[i][j])
                            button.setStyleSheet("background-color: rgb(230, 2, 2);")
                            self.ui3.gridLayout.addWidget(button, *(i, j))
                        break
                    except IndexError:
                        flag = False
                        for k in range(j, len(self.ui3.values[i])):
                            button = QtWidgets.QPushButton(self.ui3.values[i][k])
                            button.setStyleSheet("background-color: rgb(230, 2, 2);")
                            self.ui3.gridLayout.addWidget(button, *(i, k))
                        break

        if flag and answer != '':
            self.base.pop(self.key)
            self.wordcount -= 1
            self.ui3.lcdNumber.display(self.wordcount)

        self.ui3.pushButton.flag = False


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Main()
    application.show()

    sys.exit(app.exec())
