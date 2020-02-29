# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Anki.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#


from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Anki")

        self.vertical = QtWidgets.QVBoxLayout()
        self.vertical.setSpacing(10)
        self.textBrowser = QtWidgets.QTextBrowser()
        self.label = QtWidgets.QLabel()
        self.textBrowser_2 = QtWidgets.QTextBrowser()
        self.pushButton = QtWidgets.QPushButton()
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.pushButton_2 = QtWidgets.QPushButton()
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoRepeat(False)
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_2.setStyleSheet("background-color: rgb(0, 255, 0)")
        self.pushButton_3 = QtWidgets.QPushButton()
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0)")

        self.vertical.addWidget(self.textBrowser)
        self.vertical.addWidget(self.textBrowser_2)
        self.vertical.addWidget(self.pushButton)
        self.vertical.addLayout(self.horizontalLayout)
        self.vertical.addWidget(self.label)

        Form.setLayout(self.vertical)
        self.pushButton.raise_()
        self.textBrowser.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Anki", "Form"))

        self.pushButton.setText(_translate("Form", "Get Answer"))
        self.pushButton_2.setText(_translate("Form", "1"))
        self.pushButton_3.setText(_translate("Form", "2"))
