# -*- coding: utf-8 -*-

import sys
import os
# build and portable
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from macro_const import DictCommandInfo, DictCommandInfoMacro


class TreeWidgetClass:
    def __init__(self, treewidget, display):
        super(TreeWidgetClass, self).__init__()
        self.treeWidget = None
        self.show = display
        self.scan_flag = 0
        self.intiui(treewidget)

    def intiui(self, treewidget):
        self.treeWidget = treewidget

        self.treeWidget = treewidget
        # 设置列数
        self.treeWidget.setColumnCount(1)
        # 设置树形控件头部的标题
        self.treeWidget.setHeaderLabels(['选择 CRC 项'])
        self.treeWidget.setColumnWidth(0, 120)
        # 设置节点
        for value in DictCommandInfo.keys():
            item_protocon = QTreeWidgetItem(self.treeWidget)
            item_protocon.setText(0, value)
            item_protocon.setCheckState(0, Qt.Unchecked)
        # 节点全部展开
        self.treeWidget.expandAll()
        self.treeWidget.itemClicked.connect(self.handlechanged)
        # 设置初始crc选项
        item = QtWidgets.QTreeWidgetItemIterator(self.treeWidget)
        self.handlechanged(item.value(), 0)

    def treescan(self, value):
        print("value:%s" % value)
        # set unchecked
        item = QtWidgets.QTreeWidgetItemIterator(self.treeWidget)
        # 该类的value() 即为QTreeWidgetItem
        while item.value():
            print("1 %s " % item.value().text(0))
            if item.value().text(0) != value:
                print("1 change:%s" % item.value().text(0))
                item.value().setCheckState(0, Qt.Unchecked)
            else :
                item.value().setCheckState(0, Qt.Checked)
            # 到下一个节点
            item = item.__iadd__(1)

    def Tree_Clicked(self, iteme, column):
        print("ssdafasfasf")
        # item = self.treeWidget.currentItem()
        # print("key=%s " % item.text(0))

    def handlechanged(self, iteme, column):
        print("x %s " % iteme.text(0))
        # set unchecked
        item = QtWidgets.QTreeWidgetItemIterator(self.treeWidget)
        # 该类的value() 即为QTreeWidgetItem
        while item.value():
            print("x %s " % item.value().text(0))
            if item.value().text(0) != iteme.text(0):
                print("1 change:%s" % item.value().text(0))
                item.value().setCheckState(0, Qt.Unchecked)
            else:
                print("2 change:%s" % item.value().text(0))
                item.value().setCheckState(0, Qt.Checked)
                self.show(DictCommandInfo[item.value().text(0)])
            # 到下一个节点
            item = item.__iadd__(1)

    def treegetchecked(self):
        # set unchecked
        item = QtWidgets.QTreeWidgetItemIterator(self.treeWidget)
        # 该类的value() 即为QTreeWidgetItem
        while item.value():
            if item.value().checkState(0) == Qt.Checked:
                print(item.value().text(0))
                return DictCommandInfoMacro[item.value().text(0)]
            # 到下一个节点
            item = item.__iadd__(1)
