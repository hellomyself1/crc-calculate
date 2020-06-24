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
        crcform.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(crcform)
        self.centralwidget.setObjectName("centralwidget")
        self.tw_crc_contents = QtWidgets.QTreeWidget(self.centralwidget)
        self.tw_crc_contents.setGeometry(QtCore.QRect(20, 50, 231, 181))
        self.tw_crc_contents.setObjectName("tw_crc_contents")
        self.tw_crc_contents.headerItem().setText(0, "1")
        self.textBrowsercrc = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowsercrc.setGeometry(QtCore.QRect(20, 250, 751, 81))
        self.textBrowsercrc.setObjectName("textBrowsercrc")
        crcform.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(crcform)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
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
