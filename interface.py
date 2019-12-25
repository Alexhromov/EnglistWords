from PyQt5 import QtWidgets
from PyQt5 import QtGui
import time
import UI.menu as menu  # импорт нашего сгенерированного файла
import UI.Anki as Anki
import UI.AnkiSetup as AnkiS
import sys, random


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = menu.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.textEdit.setReadOnly(True)

        self.ui.textEdit.setText("English Dota 2")
        self.ui.textEdit.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))
        self.base = {}
        self.wordcount = 10
        # подключение клик-сигнал к слоту btnClick, ankiInterfase финкция яка буде виконуватися при нажатиї
        self.ui.pushButton_2.clicked.connect(self.setupAnki)

    def setupAnki(self):

        self.windowas = QtWidgets.QMainWindow()
        self.uias = AnkiS.Ui_Form()
        self.uias.setupUi(self.windowas)

        self.uias.pushButton.clicked.connect(lambda: self.getinfoas())
        self.uias.pushButton.setShortcut("Ctrl+Return")
        self.windowas.show()

    def getinfoas(self):
        self.wordcount = int(self.uias.textEdit.toPlainText())
        self.ankiInterfase()
        self.windowas.close()

    def ankiInterfase(self):
        self.write_to_base("English Dota 2", self.wordcount)
        self.window = QtWidgets.QMainWindow()
        self.uia = Anki.Ui_Form()
        self.uia.setupUi(self.window)

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

        if len(self.base) == 0:
            self.uia.pushButton_2.setEnabled(False)
            self.uia.textBrowser.setStyleSheet("background-color: rgb(20, 160, 0)")
            self.uia.textBrowser.setText("All words are complete")
            self.uia.pushButton.setText("OK")
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


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())