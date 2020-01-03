import random
import sys

from PyQt5 import QtGui
from PyQt5 import QtWidgets

import UI.AnkiSetup as AnkiS
import UI.menuV2 as menu  # импорт нашего сгенерированного файла
import UI.text2 as text2


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.base = {}
        self.wordcount = 10
        self.write_to_base("English Dota 2", self.wordcount)

        self.ui = menu.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.textEdit.setReadOnly(True)

        self.ui.textEdit.setText("English Dota 2")
        self.ui.textEdit.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))
        self.ui.label_3.setText(str(self.wordcount))

        # подключение кнопок
        self.ui.pushButton_6.clicked.connect(lambda: self.setup())

        self.ui.pushButton_4.clicked.connect(lambda: self.writeWords())

    def setup(self):

        self.windowsetup = QtWidgets.QMainWindow()
        self.uisetup = AnkiS.Ui_Form()
        self.uisetup.setupUi(self.windowsetup)

        self.uisetup.pushButton.clicked.connect(lambda: self.getinfoas())
        self.uisetup.pushButton.setShortcut("Ctrl+Return")
        self.windowsetup.show()

    def getinfoas(self):
        self.wordcount = int(self.uisetup.textEdit.toPlainText())
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

    def writeWords(self):

        self.window2 = QtWidgets.QMainWindow()
        self.ui2 = text2.Ui_Form()
        self.ui2.setupUi(self.window2)

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
            self.ui2.pushButton.clicked.connect(lambda: self.window2.close())

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

            if self.key.lower()[i] != answer[i]:
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


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())
