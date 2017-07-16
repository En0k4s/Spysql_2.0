# -*- coding: utf-8 -*-

__author__ = 'Enokas Sakone'
try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    from PyQt4 import QtCore, QtGui
except:
    print "Need to install PyQt4\npip install PyQt4 or apt-get install python-qt4"
import sys
from threading import *
try:
    import requests
except:
    print "Need to install requests\npip install requests"
from random import *
try:
    from bs4 import BeautifulSoup as sp
except:
    print "Need to install bs4\npip install bs4"
import re
import json
import random
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(437, 300)
        Dialog.setStyleSheet(_fromUtf8("QWidget{\n"
"    background:rgba(0, 0, 0, 84);\n"
"}\n"
"QFrame{\n"
"    background:rgb(23, 23, 23);\n"
"}\n"
"QComboBox{\n"
"    background:rgb(86, 86, 86);\n"
"color:white;\n"
"border:1px solid white;\n"
"}\n"
"QPushButton{\n"
"    background:rgb(86, 86, 86);\n"
"color:white;\n"
"border:1px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"    background:none;\n"
"color:white;\n"
"border:1px solid white;\n"
"}"))
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.d2 = QtGui.QComboBox(self.frame)
        self.d2.setMinimumSize(QtCore.QSize(0, 40))
        self.d2.setObjectName(_fromUtf8("d2"))
        self.d2.addItem(_fromUtf8(""))
        self.d2.addItem(_fromUtf8(""))
        self.d2.addItem(_fromUtf8(""))
        self.d2.addItem(_fromUtf8(""))
        self.d2.addItem(_fromUtf8(""))
        self.d2.addItem(_fromUtf8(""))
        self.d2.addItem(_fromUtf8(""))
        self.d2.addItem(_fromUtf8(""))
        self.d2.addItem(_fromUtf8(""))
        self.d2.addItem(_fromUtf8(""))
        self.d2.addItem(_fromUtf8(""))
        self.d2.addItem(_fromUtf8(""))
        self.d2.addItem(_fromUtf8(""))
        self.d2.addItem(_fromUtf8(""))
        self.d2.addItem(_fromUtf8(""))
        self.d2.addItem(_fromUtf8(""))
        self.d2.addItem(_fromUtf8(""))
        self.d2.addItem(_fromUtf8(""))
        self.d2.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.d2, 5, 7, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 3, 6, 1, 1)
        self.use = QtGui.QPushButton(self.frame)
        self.use.setMinimumSize(QtCore.QSize(0, 40))
        self.use.setObjectName(_fromUtf8("use"))
        self.gridLayout.addWidget(self.use, 6, 5, 1, 3)
        self.d1 = QtGui.QComboBox(self.frame)
        self.d1.setMinimumSize(QtCore.QSize(0, 40))
        self.d1.setObjectName(_fromUtf8("d1"))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.d1.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.d1, 5, 6, 1, 1)
        self.domaine = QtGui.QComboBox(self.frame)
        self.domaine.setMinimumSize(QtCore.QSize(0, 40))
        self.domaine.setObjectName(_fromUtf8("domaine"))
        self.domaine.addItem(_fromUtf8(""))
        self.domaine.addItem(_fromUtf8(""))
        self.domaine.addItem(_fromUtf8(""))
        self.domaine.addItem(_fromUtf8(""))
        self.domaine.addItem(_fromUtf8(""))
        self.domaine.addItem(_fromUtf8(""))
        self.domaine.addItem(_fromUtf8(""))
        self.domaine.addItem(_fromUtf8(""))
        self.domaine.addItem(_fromUtf8(""))
        self.domaine.addItem(_fromUtf8(""))
        self.domaine.addItem(_fromUtf8(""))
        self.domaine.addItem(_fromUtf8(""))
        self.domaine.addItem(_fromUtf8(""))
        self.domaine.addItem(_fromUtf8(""))
        self.domaine.addItem(_fromUtf8(""))
        self.domaine.addItem(_fromUtf8(""))
        self.domaine.addItem(_fromUtf8(""))
        self.domaine.addItem(_fromUtf8(""))
        self.domaine.setItemText(17, _fromUtf8(""))
        self.gridLayout.addWidget(self.domaine, 5, 5, 1, 1)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.d2.setItemText(0, _translate("Dialog", "?id=", None))
        self.d2.setItemText(1, _translate("Dialog", "?i=", None))
        self.d2.setItemText(2, _translate("Dialog", "?p=", None))
        self.d2.setItemText(3, _translate("Dialog", "?c=", None))
        self.d2.setItemText(4, _translate("Dialog", "?page=", None))
        self.d2.setItemText(5, _translate("Dialog", "?user=", None))
        self.d2.setItemText(6, _translate("Dialog", "?ud=", None))
        self.d2.setItemText(7, _translate("Dialog", "?pid=", None))
        self.d2.setItemText(8, _translate("Dialog", "?cardId=", None))
        self.d2.setItemText(9, _translate("Dialog", "?catid=", None))
        self.d2.setItemText(10, _translate("Dialog", "?storeID=", None))
        self.d2.setItemText(11, _translate("Dialog", "?card=", None))
        self.d2.setItemText(12, _translate("Dialog", "?bookid=", None))
        self.d2.setItemText(13, _translate("Dialog", "?action=", None))
        self.d2.setItemText(14, _translate("Dialog", "?url=", None))
        self.d2.setItemText(15, _translate("Dialog", "?UserID=", None))
        self.d2.setItemText(16, _translate("Dialog", "?order=", None))
        self.d2.setItemText(17, _translate("Dialog", "?orderID=", None))
        self.d2.setItemText(18, _translate("Dialog", "?category=", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; color:#7d0029;\">Dork</span><span style=\" font-size:24pt; color:#ecffe5;\">Generator 1.1</span></p></body></html>", None))
        self.use.setText(_translate("Dialog", "use", None))
        self.d1.setItemText(0, _translate("Dialog", "/index.php", None))
        self.d1.setItemText(1, _translate("Dialog", "/search.php", None))
        self.d1.setItemText(2, _translate("Dialog", "/post.php", None))
        self.d1.setItemText(3, _translate("Dialog", "/home.php", None))
        self.d1.setItemText(4, _translate("Dialog", "/achat.php", None))
        self.d1.setItemText(5, _translate("Dialog", "/shop.php", None))
        self.d1.setItemText(6, _translate("Dialog", "/card.php", None))
        self.d1.setItemText(7, _translate("Dialog", "/product.php", None))
        self.d1.setItemText(8, _translate("Dialog", "/article.php", None))
        self.d1.setItemText(9, _translate("Dialog", "/page.php", None))
        self.d1.setItemText(10, _translate("Dialog", "/user.php", None))
        self.d1.setItemText(11, _translate("Dialog", "/admin.php", None))
        self.d1.setItemText(12, _translate("Dialog", "/content.php", None))
        self.d1.setItemText(13, _translate("Dialog", "/account.php", None))
        self.d1.setItemText(14, _translate("Dialog", "/store.php", None))
        self.d1.setItemText(15, _translate("Dialog", "/view.php", None))
        self.d1.setItemText(16, _translate("Dialog", "/event.php", None))
        self.d1.setItemText(17, _translate("Dialog", "/news.php", None))
        self.d1.setItemText(18, _translate("Dialog", "/book.php", None))
        self.d1.setItemText(19, _translate("Dialog", "/detail.php", None))
        self.d1.setItemText(20, _translate("Dialog", "/main.php", None))
        self.d1.setItemText(21, _translate("Dialog", "/list.php", None))
        self.domaine.setItemText(0, _translate("Dialog", ".com", None))
        self.domaine.setItemText(1, _translate("Dialog", ".net", None))
        self.domaine.setItemText(2, _translate("Dialog", ".fr", None))
        self.domaine.setItemText(3, _translate("Dialog", ".gov", None))
        self.domaine.setItemText(4, _translate("Dialog", ".nl", None))
        self.domaine.setItemText(5, _translate("Dialog", ".ml", None))
        self.domaine.setItemText(6, _translate("Dialog", ".edu", None))
        self.domaine.setItemText(7, _translate("Dialog", ".tk", None))
        self.domaine.setItemText(8, _translate("Dialog", ".cf", None))
        self.domaine.setItemText(9, _translate("Dialog", ".ru", None))
        self.domaine.setItemText(10, _translate("Dialog", ".gouv", None))
        self.domaine.setItemText(11, _translate("Dialog", ".biz", None))
        self.domaine.setItemText(12, _translate("Dialog", ".org", None))
        self.domaine.setItemText(13, _translate("Dialog", ".gq", None))
        self.domaine.setItemText(14, _translate("Dialog", ".ci", None))
        self.domaine.setItemText(15, _translate("Dialog", ".es", None))
        self.domaine.setItemText(16, _translate("Dialog", ".info", None))

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(734, 612)
        MainWindow.setStyleSheet(_fromUtf8("QWidget{\n"
"    background:rgba(0, 0, 0, 84);\n"
"}\n"
"QFrame{\n"
"    background:rgb(23, 23, 23);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background:rgb(86, 86, 86);\n"
"color:white;\n"
"border:1px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"    background:none;\n"
"color:white;\n"
"border:1px solid white;\n"
"}\n"
"QMenu{\n"
"color:white;\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.stackedWidget = QtGui.QStackedWidget(self.frame_2)
        self.stackedWidget.setStyleSheet(_fromUtf8("\n"
"QWidget{\n"
"    background:rgb(23, 23, 23);\n"
"border:1px solid rgb(192, 192, 192);\n"
"}\n"
"QPushButton{\n"
"    background:rgb(86, 86, 86);\n"
"color:white;\n"
"border:1px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"    background:none;\n"
"color:white;\n"
"border:1px solid white;\n"
"}\n"
"QFrame{\n"
"border:none;\n"
"}"))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.gridLayout_4 = QtGui.QGridLayout(self.page)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        spacerItem = QtGui.QSpacerItem(20, 58, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(229, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.page)
        self.label.setMaximumSize(QtCore.QSize(200, 200))
        self.label.setStyleSheet(_fromUtf8("border:none;"))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/Demon.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 1, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(229, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setStyleSheet(_fromUtf8("color:white;\n"
"border:none;\n"
"font: 75 36pt \"Noteworthy\";"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 2, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 57, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 3, 1, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.scanner = QtGui.QWidget()
        self.scanner.setObjectName(_fromUtf8("scanner"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scanner)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame_3 = QtGui.QFrame(self.scanner)
        self.frame_3.setMinimumSize(QtCore.QSize(100, 40))
        self.frame_3.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.frame_3.setStyleSheet(_fromUtf8("QPushButton{\n"
"    background:rgb(86, 86, 86);\n"
"color:white;\n"
"border:1px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"    background:none;\n"
"color:white;\n"
"border:1px solid white;\n"
"}\n"
"QFrame{\n"
"border:none;\n"
"}"))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(4, 4, 12, 4)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.url = QtGui.QLineEdit(self.frame_3)
        self.url.setMinimumSize(QtCore.QSize(0, 30))
        self.url.setStyleSheet(_fromUtf8("color:white;"))
        self.url.setObjectName(_fromUtf8("url"))
        self.horizontalLayout.addWidget(self.url)
        self.pushButton = QtGui.QPushButton(self.frame_3)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.raise_()
        self.url.raise_()
        self.verticalLayout_2.addWidget(self.frame_3)
        self.ws = QtGui.QTreeWidget(self.scanner)
        self.ws.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.ws.setIconSize(QtCore.QSize(30, 30))
        self.ws.setObjectName(_fromUtf8("ws"))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.ws.headerItem().setFont(0, font)
        self.verticalLayout_2.addWidget(self.ws)
        self.bt2 = QtGui.QFrame(self.scanner)
        self.bt2.setMinimumSize(QtCore.QSize(0, 40))
        self.bt2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bt2.setFrameShadow(QtGui.QFrame.Raised)
        self.bt2.setObjectName(_fromUtf8("bt2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.bt2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem4 = QtGui.QSpacerItem(555, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.show_2 = QtGui.QPushButton(self.bt2)
        self.show_2.setMinimumSize(QtCore.QSize(100, 30))
        self.show_2.setObjectName(_fromUtf8("show_2"))
        self.horizontalLayout_2.addWidget(self.show_2)
        self.stop_2 = QtGui.QPushButton(self.bt2)
        self.stop_2.setMinimumSize(QtCore.QSize(100, 30))
        self.stop_2.setObjectName(_fromUtf8("stop_2"))
        self.horizontalLayout_2.addWidget(self.stop_2)
        self.save_2 = QtGui.QPushButton(self.bt2)
        self.save_2.setMinimumSize(QtCore.QSize(100, 30))
        self.save_2.setObjectName(_fromUtf8("save_2"))
        self.horizontalLayout_2.addWidget(self.save_2)
        self.clean2 = QtGui.QPushButton(self.bt2)
        self.clean2.setMinimumSize(QtCore.QSize(100, 30))
        self.clean2.setObjectName(_fromUtf8("clean2"))
        self.horizontalLayout_2.addWidget(self.clean2)
        self.verticalLayout_2.addWidget(self.bt2)
        self.stackedWidget.addWidget(self.scanner)
        self.dorker = QtGui.QWidget()
        self.dorker.setObjectName(_fromUtf8("dorker"))
        self.gridLayout_5 = QtGui.QGridLayout(self.dorker)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.url_2 = QtGui.QLineEdit(self.dorker)
        self.url_2.setMinimumSize(QtCore.QSize(0, 30))
        self.url_2.setStyleSheet(_fromUtf8("color:white;"))
        self.url_2.setObjectName(_fromUtf8("url_2"))
        self.gridLayout_5.addWidget(self.url_2, 0, 0, 1, 1)
        self.l2 = QtGui.QPushButton(self.dorker)
        self.l2.setMinimumSize(QtCore.QSize(100, 30))
        self.l2.setObjectName(_fromUtf8("l2"))
        self.gridLayout_5.addWidget(self.l2, 0, 1, 1, 1)
        self.dork_gen = QtGui.QPushButton(self.dorker)
        self.dork_gen.setMinimumSize(QtCore.QSize(100, 30))
        self.dork_gen.setObjectName(_fromUtf8("dork_gen"))
        self.gridLayout_5.addWidget(self.dork_gen, 0, 2, 1, 1)
        self.ws_2 = QtGui.QTreeWidget(self.dorker)
        self.ws_2.setStyleSheet(_fromUtf8("QTreeView{\n"
"color:white;\n"
"}"))
        self.ws_2.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.ws_2.setDefaultDropAction(QtCore.Qt.TargetMoveAction)
        self.ws_2.setAlternatingRowColors(False)
        self.ws_2.setIconSize(QtCore.QSize(30, 30))
        self.ws_2.setAnimated(True)
        self.ws_2.setObjectName(_fromUtf8("ws_2"))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.ws_2.headerItem().setFont(0, font)
        self.gridLayout_5.addWidget(self.ws_2, 1, 0, 1, 3)
        self.bt = QtGui.QFrame(self.dorker)
        self.bt.setMinimumSize(QtCore.QSize(0, 40))
        self.bt.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bt.setFrameShadow(QtGui.QFrame.Raised)
        self.bt.setObjectName(_fromUtf8("bt"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.bt)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem5 = QtGui.QSpacerItem(555, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.show = QtGui.QPushButton(self.bt)
        self.show.setMinimumSize(QtCore.QSize(100, 30))
        self.show.setObjectName(_fromUtf8("show"))
        self.horizontalLayout_3.addWidget(self.show)
        self.stop = QtGui.QPushButton(self.bt)
        self.stop.setMinimumSize(QtCore.QSize(100, 30))
        self.stop.setObjectName(_fromUtf8("stop"))
        self.horizontalLayout_3.addWidget(self.stop)
        self.save = QtGui.QPushButton(self.bt)
        self.save.setMinimumSize(QtCore.QSize(100, 30))
        self.save.setObjectName(_fromUtf8("save"))
        self.horizontalLayout_3.addWidget(self.save)
        self.clean = QtGui.QPushButton(self.bt)
        self.clean.setMinimumSize(QtCore.QSize(100, 30))
        self.clean.setObjectName(_fromUtf8("clean"))
        self.horizontalLayout_3.addWidget(self.clean)
        self.gridLayout_5.addWidget(self.bt, 2, 0, 1, 3)
        self.stackedWidget.addWidget(self.dorker)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 100))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.tabWidget.setStyleSheet(_fromUtf8(" QTabWidget::tab-bar{\n"
"    left:5px;\n"
"    border:1px solid rgb(192, 192, 192);\n"
"\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover{\n"
"    background:none;\n"
"color:rgb(192, 192, 192);\n"
"width:300px;\n"
"border:1px solid rgb(192, 192, 192);\n"
"border-bottom:none;\n"
"}\n"
"QTabBar::tab{\n"
"    width:100px;\n"
"\n"
"padding:5px;\n"
"    color:rgb(192, 192, 192);\n"
"\n"
"}\n"
" QTabWidget::pane{\n"
"    border:1px solid rgb(192, 192, 192);\n"
"\n"
"}\n"
""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabWidgetPage1 = QtGui.QWidget()
        self.tabWidgetPage1.setObjectName(_fromUtf8("tabWidgetPage1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tabWidgetPage1)
        self.gridLayout_3.setMargin(10)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.dscan = QtGui.QPushButton(self.tabWidgetPage1)
        self.dscan.setMinimumSize(QtCore.QSize(100, 25))
        self.dscan.setMaximumSize(QtCore.QSize(150, 16777215))
        self.dscan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dscan.setObjectName(_fromUtf8("dscan"))
        self.gridLayout_3.addWidget(self.dscan, 1, 0, 2, 1)
        self.frame = QtGui.QFrame(self.tabWidgetPage1)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.console = QtGui.QTextEdit(self.frame)
        self.console.setStyleSheet(_fromUtf8("color:rgb(149, 149, 149);"))
        self.console.setObjectName(_fromUtf8("console"))
        self.verticalLayout.addWidget(self.console)
        self.gridLayout_3.addWidget(self.frame, 0, 4, 3, 1)
        self.wscan = QtGui.QPushButton(self.tabWidgetPage1)
        self.wscan.setMinimumSize(QtCore.QSize(100, 25))
        self.wscan.setMaximumSize(QtCore.QSize(150, 16777215))
        self.wscan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.wscan.setObjectName(_fromUtf8("wscan"))
        self.gridLayout_3.addWidget(self.wscan, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage1, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_window = QtGui.QAction(MainWindow)
        self.actionNew_window.setObjectName(_fromUtf8("actionNew_window"))
        self.actionHome = QtGui.QAction(MainWindow)
        self.actionHome.setObjectName(_fromUtf8("actionHome"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionDork_extractor = QtGui.QAction(MainWindow)
        self.actionDork_extractor.setObjectName(_fromUtf8("actionDork_extractor"))
        self.actionWebsite_scan = QtGui.QAction(MainWindow)
        self.actionWebsite_scan.setObjectName(_fromUtf8("actionWebsite_scan"))
        self.actionDork_generator = QtGui.QAction(MainWindow)
        self.actionDork_generator.setObjectName(_fromUtf8("actionDork_generator"))
        self.actionMaximized = QtGui.QAction(MainWindow)
        self.actionMaximized.setObjectName(_fromUtf8("actionMaximized"))
        self.actionMinimized = QtGui.QAction(MainWindow)
        self.actionMinimized.setObjectName(_fromUtf8("actionMinimized"))
        self.actionFullscreen = QtGui.QAction(MainWindow)
        self.actionFullscreen.setObjectName(_fromUtf8("actionFullscreen"))
        self.actionReduice = QtGui.QAction(MainWindow)
        self.actionReduice.setObjectName(_fromUtf8("actionReduice"))
        self.actionDisable_console = QtGui.QAction(MainWindow)
        self.actionDisable_console.setObjectName(_fromUtf8("actionDisable_console"))
        self.actionDocumentation = QtGui.QAction(MainWindow)
        self.actionDocumentation.setObjectName(_fromUtf8("actionDocumentation"))
        self.actionApropos = QtGui.QAction(MainWindow)
        self.actionApropos.setObjectName(_fromUtf8("actionApropos"))
        self.actionNew_window_2 = QtGui.QAction(MainWindow)
        self.actionNew_window_2.setObjectName(_fromUtf8("actionNew_window_2"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.menuFichier.addAction(self.actionNew_window_2)
        self.menuFichier.addAction(self.actionHome)
        self.menuFichier.addAction(self.actionExit)
        self.menuTools.addAction(self.actionDork_extractor)
        self.menuTools.addAction(self.actionWebsite_scan)
        self.menuTools.addAction(self.actionDork_generator)
        self.menuView.addAction(self.actionMaximized)
        self.menuView.addAction(self.actionMinimized)
        self.menuView.addAction(self.actionFullscreen)
        self.menuHelp.addAction(self.actionApropos)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.clean2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ws.clear)
        QtCore.QObject.connect(self.clean, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ws_2.reset)
        QtCore.QObject.connect(self.clean2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ws.reset)
        QtCore.QObject.connect(self.clean, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ws_2.clear)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionMaximized, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.showMaximized)
        QtCore.QObject.connect(self.actionMinimized, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.showMinimized)
        QtCore.QObject.connect(self.actionFullscreen, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.showFullScreen)
        QtCore.QObject.connect(self.actionNew_window, QtCore.SIGNAL(_fromUtf8("triggered()")), self.centralwidget.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ultimate SQLI Tools | Spysql 2.0", None))
        self.label_2.setText(_translate("MainWindow", "Spyql 2.0", None))
        self.url.setPlaceholderText(_translate("MainWindow", "http://", None))
        self.pushButton.setText(_translate("MainWindow", "launch", None))
        self.ws.headerItem().setText(0, _translate("MainWindow", "id", None))
        self.ws.headerItem().setText(1, _translate("MainWindow", "url", None))
        self.ws.headerItem().setText(2, _translate("MainWindow", "result", None))
        self.show_2.setText(_translate("MainWindow", "show", None))
        self.stop_2.setText(_translate("MainWindow", "stop", None))
        self.save_2.setText(_translate("MainWindow", "save", None))
        self.clean2.setText(_translate("MainWindow", "clean", None))
        self.url_2.setPlaceholderText(_translate("MainWindow", "dork", None))
        self.l2.setText(_translate("MainWindow", "launch", None))
        self.dork_gen.setText(_translate("MainWindow", "dork", None))
        self.ws_2.headerItem().setText(0, _translate("MainWindow", "id", None))
        self.ws_2.headerItem().setText(1, _translate("MainWindow", "target", None))
        self.ws_2.headerItem().setText(2, _translate("MainWindow", "result", None))
        self.show.setText(_translate("MainWindow", "show", None))
        self.stop.setText(_translate("MainWindow", "stop", None))
        self.save.setText(_translate("MainWindow", "save", None))
        self.clean.setText(_translate("MainWindow", "clean", None))
        self.dscan.setText(_translate("MainWindow", "Dork Scan", None))
        self.console.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">started</p></body></html>", None))
        self.wscan.setText(_translate("MainWindow", "Website Scan", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("MainWindow", "Ultimate SQLI Tools | Spysql 2.0", None))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuHelp.setTitle(_translate("MainWindow", "help", None))
        self.actionNew_window.setText(_translate("MainWindow", "new window", None))
        self.actionHome.setText(_translate("MainWindow", "home", None))
        self.actionExit.setText(_translate("MainWindow", "exit", None))
        self.actionDork_extractor.setText(_translate("MainWindow", "dork scan", None))
        self.actionWebsite_scan.setText(_translate("MainWindow", "website scan", None))
        self.actionDork_generator.setText(_translate("MainWindow", "dork generator", None))
        self.actionMaximized.setText(_translate("MainWindow", "maximized", None))
        self.actionMinimized.setText(_translate("MainWindow", "minimized", None))
        self.actionFullscreen.setText(_translate("MainWindow", "fullscreen", None))
        self.actionReduice.setText(_translate("MainWindow", "reduice", None))
        self.actionDisable_console.setText(_translate("MainWindow", "disable console", None))
        self.actionDocumentation.setText(_translate("MainWindow", "documentation ", None))
        self.actionApropos.setText(_translate("MainWindow", "apropos", None))
        self.actionNew_window_2.setText(_translate("MainWindow", "New window", None))
        self.actionHelp.setText(_translate("MainWindow", "help", None))


from PyQt4 import QtCore, QtGui


def diff(first, second):
        second = set(second)
        return [item for item in first if item not in second]
def GetSource(link,method="GET",data="",type="1"):
    if method=="GET" and type=="1":
        if re.search("http://",link):
            pass
        elif re.search("https://",link):
            pass
        else:
            link = "http://"+link
        try:
            r = requests.get(link)
        except KeyboardInterrupt,e:
            return "Error occured "+e
        return r.content
def simpleCrawler(target,method=1):
    if method==1:
        s1 = GetSource(target)
        if s1=="Error occured":
      
            return("Network error")
        r = re.compile('href=".+"')
        stock =list()
        for link in r.findall(str(s1)):
            link = link.split("\"")
            for it in link:
                if re.search("http",it) or re.search("php",it) or re.search("html",it) :
                    it = it.replace(" ","")
                    """print("[*] ",(str(it[:60]))+"...")"""
                    stock.append(it)
        return stock
def webcrawler(link):
    lt = simpleCrawler(link)
    lit = []
    for it in lt:
        if "http" not in str(it):
            it = str(link)+it
        lit.append(it)
    return lit

class TreeIt(QTreeWidgetItem):
    def __init__(self):
        QTreeWidgetItem.__init__(self)
        self.setIcon(0,QIcon("images/demon.png"))
class TreeIt2(QTreeWidgetItem):
    def __init__(self):
        QTreeWidgetItem.__init__(self)
        self.setIcon(0,QIcon("images/im.ico"))
class Tr(Thread):
    def __init__(self, target, stype, parent):
        Thread.__init__(self)
        self.type = stype
        self.parent = parent
        self.target = target
        self.user_agent = [
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)',
            'Mozilla / 5.0 (Windows; U; Windows NT 5.1; de; rv: 1.9.2.3) Gecko / 20100401 Firefox / 3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) ',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; fr; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; fr; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3',
            'Mozilla/4.0 (compatible; MSIE 5.23; Mac_PowerPC)', 'GameSpyHTTP/1.0', '']

    def run(self):
        print "running"
        if self.type == "dork":
            self.s = requests.Session()
            x = 0
            limit = 2
            while x < limit:
                x += 1;
                self.bingget(self.target, x)
        elif self.type == "scanning":
            k = webcrawler(self.target)
            self.scanning(k)
    def scanning(self,target):
        self.parent.ui.bt2.setVisible(True)
        for iti in target:
            if re.search("",str(iti)) and "https://" not in str(iti):
                try:
                    try:
                        iti= iti.replace("%3f","?")
                        iti= iti.replace("%3d","=")
                        z = requests.get(str(iti)+str("'"))
                    except:pass
                    z = z.content
                except :
                    z = ""
                    self.parent.ui.console.append("<font color='red'>Network error </font>")

                m = iti
                if "You have" in z or "an error" in z or "mysql syntax" in  z or "Mysql syntax" in z or "mysql Syntax" in z:
                    it = TreeIt()
                    it.setText(0,"")
                    it.setText(1,str(m))
                    it.setText(1,str(m))
                    it.setText(2,"Vulnerable")
                    it.setForeground(2,QBrush(QColor("red")))
                    it.setForeground(1,QBrush(QColor("white")))
                    it.setIcon(0,QIcon("images/demon.png"))
                    self.parent.ui.console.append("[*] Scan <font color='green'>"+str(m)+"</font>")
                    self.parent.zscan.append(str(m)+"\tVulnerable")
                else:
                    it = TreeIt2()
                    it.setText(0,"")
                    it.setText(1,str(m))
                    it.setForeground(1,QBrush(QColor("white")))
                    it.setText(2,"not vulnerable")
                    it.setForeground(2,QBrush(QColor("green")))
                    it.setIcon(0,QIcon("images/im.ico"))
                    self.parent.zscan.append(str(m)+"\tnot vulnerable")
                    self.parent.ui.console.append("[*] Scan "+str(m))
                self.parent.ui.ws.addTopLevelItem(it)
                self.parent.ui.console.update()
    def bingget(self, name, start):
        debug = {'verbose': sys.stderr}
        self.choice = choice(self.user_agent)
        print(self.choice)
        self.parent.ui.console.append("[*] searching dork link...")
        agent = {'User-Agent': str(self.choice)}
        if start == 0:
            st = ""
        else :
            st = "first=" + str(start * 10)
        print start
        try:
            r = self.s.get("http://www.bing.com/search?q=" + str(name) + "&go=Valider&" + str(st), headers=agent)
            content = r.content
        except requests.ConnectionError,e:
            self.parent.ui.console.append("<font color='red'>"+str(e)+"</font>")
            pass

        soup = sp(content)
        self.parent.ui.bt.setVisible(True)
        for a in soup.find_all("a"):
            if re.search("ID=SERP", str(a)):
                name = (a.string)
                m = a['href']
                m = m.replace("http://www.microsofttranslator.com/bv.aspx?ref=SERP&br=ro&mkt=en-WW&dl=fr&lp=EN_FR&a=",
                              "")
                try:
                    if name == None:
                        pass


                    elif re.search("/search?", str(m)) or re.search("http://go.microsoft.com", str(m)) or re.search(
                            "# Votre avis", str(m)) or str(m) == None or str(m) == "None" or "http" not in str(m) or "=" not in str(m):
                        pass
                    else:
                        print (m, name)
                        if  "http://www.microsofttranslator.com" in str(m):
                            m = m.split("&a=")
                            m = m[1]

                        m = m.replace("%3a",":")
                        m = m.replace("%2f","/")
                        m= m.replace("%3f","?")
                        m= m.replace("%3d","=")
                        try:
                          po = requests.get(m+str("'"))
                          po = po.content
                        except requests.ConnectionError,e:
                            self.parent.ui.console.append("<font color='red'>"+str(e)+"</font>")
                            po = ""
                            pass
                        if "You have" in po or "an error" in po or "mysql syntax" in  po or "Mysql syntax" in po or "mysql Syntax" in po:
                            it = TreeIt()
                            it.setText(0,"")
                            it.setText(1,str(m))
                            it.setText(2,"Vulnerable")
                            it.setForeground(2,QBrush(QColor("red")))
                            it.setIcon(0,QIcon("images/demon.png"))
                            self.parent.zdork.append(str(m)+"\tVulnerable")
                            self.parent.ui.console.append("[*] Scan <font color='green'>"+str(m)+"</font>")
                        else:
                            it = TreeIt2()
                            it.setText(0,"")
                            it.setText(1,str(m))
                            it.setText(2,"not vulnerable")
                            it.setForeground(2,QBrush(QColor("green")))
                            it.setIcon(0,QIcon("images/im.ico"))
                            self.parent.zdork.append(str(m)+"\tnot ulnerable")
                            self.parent.ui.console.append("[*] Scan "+str(m)+"")

                        self.parent.ui.ws_2.addTopLevelItem(it)
                except:
                    pass
            elif re.search("/search?", str(m)):
                pass
            else:
                pass


class Content(QMainWindow):
    zdork = []
    zscan = []
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.console.toHtml()
        self.ui.console.setReadOnly(True)
        self.ui.dscan.clicked.connect(self.scan)
        self.ui.actionHome.triggered.connect(self.home)
        self.ui.wscan.clicked.connect(self.scan2)
        self.ui.l2.clicked.connect(self.dorking)
        self.ui.dork_gen.clicked.connect(self.generator)
        self.ui.pushButton.clicked.connect(self.scanning)
        self.ui.bt.setVisible(False)
        self.ui.bt2.setVisible(False)
        self.ui.actionDork_extractor.triggered.connect(self.scan)
        self.ui.actionWebsite_scan.triggered.connect(self.scan2)
        self.ui.actionDork_generator.triggered.connect(self.generator)
        self.ui.show.clicked.connect(self.show1)
        self.ui.show_2.clicked.connect(self.show2)
        self.ui.stop.clicked.connect(self.stop1)
        self.ui.save.clicked.connect(self.saving)
        self.ui.save_2.clicked.connect(self.saving2)
        self.ui.save.setText("show all")
        self.ui.save_2.setText("show all")
        self.setWindowIcon(QIcon("images/demon.png"))
    def saving(self):

        vi = QDialog()
        vi.resize(600,200)
        v = QTextEdit(vi)
        lay = QVBoxLayout()
        lay.addWidget(v)
        vi.setLayout(lay)
        v.resize(2000,2000)
        for it in self.zdork:
            v.append(it)
        vi.exec_()
    def saving2(self):

        vi = QDialog()

        vi.resize(600,200)
        v = QTextEdit(vi)
        lay = QVBoxLayout()
        lay.addWidget(v)
        vi.setLayout(lay)
        for it in self.zscan:
            v.append(it)
        vi.exec_()
    def stop1(self):
        self.tr.exit()
    def show1(self):
        i = self.ui.ws_2.currentItem()
        vi = QDialog()
        vi.resize(600,200)
        v = QTextEdit(vi)
        lay = QVBoxLayout()
        lay.addWidget(v)
        vi.setLayout(lay)
        v.append(str(i.text(1)))
        vi.exec_()
    def show2(self):
        i = self.ui.ws.currentItem()
        vi = QDialog()
        vi.resize(600,200)
        v = QTextEdit(vi)
        lay = QVBoxLayout()
        lay.addWidget(v)
        vi.setLayout(lay)
        v.append(str(i.text(1)))
        vi.exec_()
    def home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
    def scanning(self):
        self.target = self.ui.url.text()
        QApplication.processEvents()
        self.tr = Tr(self.target,"scanning",self)
        self.tr.start()
        self.ui.console.append("[*] Scan initiated...")
    def generator(self):
        self.gen = QDialog()
        self.gen.ui = Ui_Dialog()
        self.ui.console.append("[*] dork generator running...")
        self.gen.ui.setupUi(self.gen)
        self.gen.ui.use.clicked.connect(self.generation)
        self.gen.exec_()
    def generation(self):
        self.d1 = self.gen.ui.domaine.currentText()
        self.d2 = self.gen.ui.d1.currentText()
        self.d3 = self.gen.ui.d2.currentText()
        self.txt = str(self.d1)+str(self.d2)+str(self.d3)
        self.ui.url_2.setText(self.txt)
        self.gen.close()
        self.ui.console.append("[*] dork generated")
    def dorking(self):
        QApplication.processEvents()
        text = self.ui.url_2.text()
        self.tr2 = Tr(text, "dork", self)
        self.tr2.start()
    def scan(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.dorker)
    def scan2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.scanner)


Program = QApplication(sys.argv)
content = Content()
content.show()
Program.exec_()
