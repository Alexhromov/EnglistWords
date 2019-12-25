from PyQt5 import QtWidgets
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
        self.base = {}
        self.write_to_base("English Dota 2")

        # подключение клик-сигнал к слоту btnClick, btn2Click финкция яка буде виконуватися при нажатиї
        self.ui.pushButton_2.clicked.connect(self.btn2Click)

    def btn2Click(self):

        self.window = QtWidgets.QMainWindow()
        self.uia = Anki.Ui_Form()
        self.uia.setupUi(self.window)


        key = random.choice(list(self.base.keys()))
        self.key = key
        self.uia.pushButton_2.hide()
        self.uia.pushButton_3.hide()
        self.uia.textBrowser.hide()

        self.uia.textEdit.setText(key)
        self.uia.textBrowser.setText(self.base[key])
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
            self.uia.textBrowser.setText(self.base[key])

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

        for i in range(numb):            #Можливо не потрібна кількість елементів, тобто елементи повторюються
            with open("Words\\" + name + ".txt", encoding="utf-8") as w:

                line = random_line(w)
                text = line.rstrip("\n").rstrip().split("\t")
                self.base[text[0]] = text[1]


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())