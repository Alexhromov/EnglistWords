# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Text test")
        Form.resize(500, 400)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 30, 291, 101))
        self.lineEdit.setFrame(False)
        self.lineEdit.setCursorPosition(7)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 180, 291, 121))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(370, 340, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(370, 340, 93, 28))
        self.pushButton_1.setObjectName("pushButton_1")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 340, 55, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Text test", "Form"))
        self.lineEdit.setText(_translate("Form", "UA Text"))
        self.pushButton.setText(_translate("Form", "Enter"))
        self.label.setText(_translate("Form", "num"))
        self.pushButton_1.setText(_translate("Form", "Enter"))
