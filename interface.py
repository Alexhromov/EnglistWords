import random
import sys

from PyQt5 import QtGui
from PyQt5 import QtWidgets

import UI.Anki as Anki
import UI.AnkiSetup as AnkiS
import UI.menuV2 as menu  # импорт нашего сгенерированного файла
import UI.text2 as text2
import UI.text3 as text3


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.base = {}
        self.wordcount = 10
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
        self.ui.pushButton_2.clicked.connect(lambda: self.ankiInterfase())
        self.ui.pushButton_4.clicked.connect(lambda: self.writeWords())
        self.ui.pushButton_3.clicked.connect(lambda: self.b3main())

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
        self.write_to_base("English Dota 2", self.wordcount)
        self.ui.label_3.setText(str(self.wordcount))
        self.windowsetup.close()

    def ankiInterfase(self):

        self.window = QtWidgets.QMainWindow()
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
            self.ui.label_3.setText(str(self.wordcount))
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
            self.window2.close()
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

    def b3main(self):
        self.window3 = QtWidgets.QMainWindow()
        self.ui3 = text3.Ui_Form()
        self.ui3.setupUi(self.window3)
        self.window3.setWindowTitle("Letter check")

        key = random.choice(list(self.base.keys()))
        self.key = key
        word = self.key.lower().split()
        self.ui3.values = [[i for i in word[j]] for j in range(len(word))]
        self.ui3.lcdNumber.display(self.wordcount)
        self.ui3.pushButton.setShortcut("Return")
        self.ui3.lineEdit.setText(self.base[key])

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
                self.window2.close()
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






app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())