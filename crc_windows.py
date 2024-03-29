# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crc_windows.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_crcform(object):
    def setupUi(self, crcform):
        crcform.setObjectName("crcform")
        crcform.resize(710, 553)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        crcform.setFont(font)
        crcform.setStyleSheet("")
        crcform.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(crcform)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(260, 50, 421, 251))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.textEdit_putin = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_putin.setGeometry(QtCore.QRect(18, 40, 391, 171))
        self.textEdit_putin.setObjectName("textEdit_putin")
        self.radioButton_hex = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_hex.setGeometry(QtCore.QRect(290, 20, 89, 16))
        self.radioButton_hex.setObjectName("radioButton_hex")
        self.radioButton_ascii = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_ascii.setGeometry(QtCore.QRect(210, 20, 89, 16))
        self.radioButton_ascii.setObjectName("radioButton_ascii")
        self.label_show = QtWidgets.QLabel(self.groupBox)
        self.label_show.setGeometry(QtCore.QRect(20, 220, 381, 21))
        self.label_show.setObjectName("label_show")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(260, 310, 421, 71))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser_result = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_result.setGeometry(QtCore.QRect(18, 20, 391, 31))
        self.textBrowser_result.setObjectName("textBrowser_result")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 10, 190, 31))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 390, 651, 111))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.textBrowser_crc = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_crc.setGeometry(QtCore.QRect(10, 20, 621, 81))
        self.textBrowser_crc.setStyleSheet("")
        self.textBrowser_crc.setObjectName("textBrowser_crc")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 50, 211, 331))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.tw_crc_contents = QtWidgets.QTreeWidget(self.groupBox_4)
        self.tw_crc_contents.setGeometry(QtCore.QRect(10, 20, 190, 301))
        self.tw_crc_contents.setObjectName("tw_crc_contents")
        self.tw_crc_contents.headerItem().setText(0, "1")
        crcform.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(crcform)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 710, 23))
        self.menubar.setObjectName("menubar")
        crcform.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(crcform)
        self.statusbar.setObjectName("statusbar")
        crcform.setStatusBar(self.statusbar)

        self.retranslateUi(crcform)
        QtCore.QMetaObject.connectSlotsByName(crcform)

    def retranslateUi(self, crcform):
        _translate = QtCore.QCoreApplication.translate
        crcform.setWindowTitle(_translate("crcform", "MainWindow"))
        self.groupBox.setTitle(_translate("crcform", "输入框"))
        self.radioButton_hex.setText(_translate("crcform", "十六进制"))
        self.radioButton_ascii.setText(_translate("crcform", "ASCII"))
        self.label_show.setText(_translate("crcform", "TextLabel"))
        self.groupBox_2.setTitle(_translate("crcform", "计算结果"))
        self.pushButton.setText(_translate("crcform", "开始计算"))
        self.groupBox_3.setTitle(_translate("crcform", "描述"))
        self.groupBox_4.setTitle(_translate("crcform", "CRC 项"))
