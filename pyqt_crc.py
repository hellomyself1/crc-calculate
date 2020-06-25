# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, QTimer
from crc_windows import Ui_crcform
import treewidget
import crc_cal
from macro_const import AllCrcItems
import os_utils
import re


class Pyqt5Crc(QtWidgets.QMainWindow, Ui_crcform):

    signal_desc = pyqtSignal(str)
    signal_crc_result = pyqtSignal(str)

    def __init__(self):
        super(Pyqt5Crc, self).__init__()
        self.setupUi(self)
        self.tw = None
        self.crccal = None
        self.forminit()
        self.init()

    def init(self):
        self.signal_desc.connect(self.txt_desc_display)
        self.signal_crc_result.connect(self.txt_crc_result_display)
        self.tw = treewidget.TreeWidgetClass(self.tw_crc_contents, self.signal_desc_emit)
        self.pushButton.clicked.connect(self.start_cal)
        self.crccal = crc_cal.CrcCal()

    def forminit(self):
        self.textEdit_putin.setText("123456789")
        self.radioButton_ascii.setChecked(True)
        self.radioButton_hex.setChecked(False)

    def signal_desc_emit(self, str):
        self.signal_desc.emit(str)

    def txt_desc_display(self, str_info):
        self.textBrowser_crc.setText("")
        self.textBrowser_crc.insertPlainText(str_info)

    def signal_crc_result_emit(self, str):
        self.signal_crc_result.emit(str)

    def txt_crc_result_display(self, str_info):
        self.textBrowser_result.setText("")
        self.textBrowser_result.insertPlainText(str_info)


    def get_data_input(self):
        list = []
        rl_flag = True
        if self.radioButton_ascii.isChecked():
            # ascii
            inputstr = self.textEdit_putin.toPlainText()
            rl_flag = os_utils.isascii(inputstr)
            print(rl_flag)
            list = os_utils.ascii_to_intlist(inputstr)
        elif self.radioButton_hex.isChecked():
            # hex
            inputstr = self.textEdit_putin.toPlainText()
            s = len(inputstr)
            print(s)
            list = os_utils.hexstr_to_int_list(inputstr)
        else:
            assert 0, "error"
        print(list)
        return [rl_flag, list]

    def start_cal(self):
        list_input = self.get_data_input()
        rl_flag = list_input[0]
        if rl_flag is False:
            self.signal_crc_result_emit("请输入正确格式的ASCII码或者十六进制")
            return
        list = list_input[1]
        # get crc calculate project
        crcpro = self.tw.treegetchecked()
        print(crcpro)
        crcint = 0
        if crcpro == AllCrcItems.CRC_8:
            crcint = self.crccal.crc8(list)
        elif crcpro == AllCrcItems.CRC_16:
            crcint = self.crccal.crc16(list)
        elif crcpro == AllCrcItems.CRC_24:
            crcint = self.crccal.crc24(list)
        elif crcpro == AllCrcItems.CRC_32:
            crcint = self.crccal.crc32(list)
        else:
            print("not support")
        self.signal_crc_result_emit(hex(crcint))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = Pyqt5Crc()
    myshow.show()
    sys.exit(app.exec_())
