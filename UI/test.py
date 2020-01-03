# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 't.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(110, 90, 271, 161))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setHtml(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; color:#c5398d;\">Q</span><span style=\" font-size:26pt; color:#ffff00;\">uestion</span><span style=\" font-size:26pt;\"> </span><span style=\" font-size:26pt; color:#24dc21;\">w</span><span style=\" font-size:26pt; color:#dc28d9;\">ord</span></p></body></html>"))


        # self.ui2.lineEdit_2.setText('<span style=\" font-size:26pt; color:#c5398d;\">Q</span><span style=\" font-size:'
        '26pt; color:#ffff00;\">uestion</span><span style=\" font-size:26pt;\"> </span><span'
        ' style=\" font-size:26pt; color:#24dc21;\">w</span><span style=\" font-size:26pt; '
        'color:#dc28d9;\">ord</span></p></body></html>"')
