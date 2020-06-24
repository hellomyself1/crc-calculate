# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, QTimer
from crc_windows import Ui_crcform
import treewidget

class Pyqt5Crc(QtWidgets.QMainWindow, Ui_crcform):

    signal_txt = pyqtSignal(str)

    def __init__(self):
        super(Pyqt5Crc, self).__init__()
        self.setupUi(self)
        self.tw = None
        self.init()

    def init(self):
        self.signal_txt.connect(self.txt_data_display)
        self.tw = treewidget.TreeWidgetClass(self.tw_crc_contents, self.signal_txt_emit)

    def signal_txt_emit(self, str):
        self.signal_txt.emit(str)

    def txt_data_display(self, str_info):
        self.textBrowsercrc.setText("")
        self.textBrowsercrc.insertPlainText(str_info)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = Pyqt5Crc()
    myshow.show()
    sys.exit(app.exec_())
