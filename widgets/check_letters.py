import random
import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets

import Config
import UI.text3 as text3


class Main(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.setMinimumSize(535, 465)

        self.base = Config.base
        self.wordcount = Config.wordcount

        self.window3 = QtWidgets.QMainWindow()
        self.ui3 = text3.Ui_Form()
        self.ui3.setupUi(self.window3)
        self.window3.setWindowTitle("Letter check")

        self.key = random.choice(list(self.base.keys()))
        word = self.key.lower().split()
        self.values = [[i for i in word[j]] for j in range(len(word))]
        self.ui3.lcdNumber.display(self.wordcount)
        self.ui3.pushButton.setShortcut("Return")
        self.ui3.lineEdit.setText(self.base[self.key])

        self.ui3.pushButton.flag = True
        self.ui3.pushButton.clicked.connect(lambda: self.b3button())

        self.window3.show()

    def b3button(self):

        def clear_layout(layout):
            if layout is not None:
                while layout.count():
                    child = layout.takeAt(0)
                    if child.widget() is not None:
                        child.widget().deleteLater()
                    elif child.layout() is not None:
                        clear_layout(child.layout())

        if self.ui3.pushButton.flag:
            self.check_word()
        else:
            self.ui3.lineEdit_2.clear()
            clear_layout(self.ui3.gridLayout)
            self.ui3.pushButton.flag = True

            if self.wordcount == 0:
                self.ui3.lineEdit.setText("All words are complete")

                self.ui3.pushButton.setText("OK")
                self.ui3.pushButton.clicked.connect(self.window3.close)
                self.ui3.pushButton.setShortcut("Return")
                self.ui3.lcdNumber.display(self.wordcount)

            else:

                key = random.choice(list(self.base.keys()))
                self.key = key
                word = self.key.lower().split()
                self.values = [[i for i in word[j]] for j in range(len(word))]

                self.ui3.lineEdit.setText(self.base[key])

    def check_word(self):
        answer = self.ui3.lineEdit_2.text()
        answer = answer.lower().strip().split()
        flag = True
        counter = 0
        w_length = 0
        self.ui3.label.setText("0")
        if len(answer) != len(self.values):
            flag = False

        for i in range(len(self.values)):
            w_length += len(self.values[i])

            try:

                if len(answer[i]) != len(self.values[i]):
                    flag = False
            except IndexError:
                flag = False

            for j in range(len(self.values[i])):
                while True:
                    try:

                        button = QtWidgets.QLabel(self.values[i][j])
                        button.setMaximumSize(50, 50)
                        button.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                        if answer[i][j] == self.values[i][j]:
                            counter += 1
                            button.setStyleSheet("background-color: rgb(2, 255, 2);")

                        else:
                            flag = False
                            button.setStyleSheet("background-color: rgb(230, 2, 2);")

                        self.ui3.gridLayout.addWidget(button, *(i, j))

                        break
                    except IndexError:
                        flag = False
                        for k in range(j, len(self.values[i])):
                            button = QtWidgets.QLabel(self.values[i][k])
                            button.setStyleSheet("background-color: rgb(230, 2, 2);")
                            button.setMaximumSize(50, 50)
                            button.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                            self.ui3.gridLayout.addWidget(button, *(i, k))
                        break

        self.ui3.label.setText(str(round(counter / w_length, 2)))

        if flag and answer != '':
            self.base.pop(self.key)
            self.wordcount -= 1
            self.ui3.lcdNumber.display(self.wordcount)

        self.ui3.pushButton.flag = False


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Main()

    sys.exit(app.exec())
