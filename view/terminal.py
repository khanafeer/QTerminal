# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/terminal.ui'
#
# Created: Sun Nov  4 02:15:14 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1163, 68)
        Form.setStyleSheet(".QWidget{\n"
"background:#2F4858;}\n"
"")
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtGui.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtGui.QGridLayout(self.widget_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_5 = QtGui.QWidget(self.widget_3)
        self.widget_5.setStyleSheet("background:#CC3333;\n"
"color:#fff;")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtGui.QLabel(self.widget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(220, 0))
        font = QtGui.QFont()
        font.setFamily("Alarabiya Font")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.current_lbl = QtGui.QLabel(self.widget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_lbl.sizePolicy().hasHeightForWidth())
        self.current_lbl.setSizePolicy(sizePolicy)
        self.current_lbl.setMinimumSize(QtCore.QSize(220, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.current_lbl.setFont(font)
        self.current_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.current_lbl.setObjectName("current_lbl")
        self.verticalLayout_4.addWidget(self.current_lbl)
        self.gridLayout.addWidget(self.widget_5, 0, 1, 1, 1)
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setStyleSheet("background:#FFAA32;\n"
"color:#fff;")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtGui.QLabel(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(220, 0))
        font = QtGui.QFont()
        font.setFamily("Alarabiya Font")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.waiting_lbl = QtGui.QLabel(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.waiting_lbl.sizePolicy().hasHeightForWidth())
        self.waiting_lbl.setSizePolicy(sizePolicy)
        self.waiting_lbl.setMinimumSize(QtCore.QSize(220, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.waiting_lbl.setFont(font)
        self.waiting_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.waiting_lbl.setObjectName("waiting_lbl")
        self.verticalLayout_3.addWidget(self.waiting_lbl)
        self.gridLayout.addWidget(self.widget_4, 0, 0, 1, 1)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ext_btn = QtGui.QPushButton(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ext_btn.sizePolicy().hasHeightForWidth())
        self.ext_btn.setSizePolicy(sizePolicy)
        self.ext_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/n/imgs/Cancel-500.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ext_btn.setIcon(icon)
        self.ext_btn.setIconSize(QtCore.QSize(20, 20))
        self.ext_btn.setObjectName("ext_btn")
        self.gridLayout_2.addWidget(self.ext_btn, 0, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 3, 1, 1)
        self.log_out = QtGui.QPushButton(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_out.sizePolicy().hasHeightForWidth())
        self.log_out.setSizePolicy(sizePolicy)
        self.log_out.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/n/imgs/Reply All Arrow Filled-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.log_out.setIcon(icon1)
        self.log_out.setIconSize(QtCore.QSize(20, 20))
        self.log_out.setObjectName("log_out")
        self.gridLayout_2.addWidget(self.log_out, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 0, 8, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        self.status_btn = QtGui.QPushButton(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_btn.sizePolicy().hasHeightForWidth())
        self.status_btn.setSizePolicy(sizePolicy)
        self.status_btn.setStyleSheet("")
        self.status_btn.setText("")
        self.status_btn.setObjectName("status_btn")
        self.gridLayout.addWidget(self.status_btn, 0, 3, 1, 1)
        self.next_btn = QtGui.QPushButton(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_btn.sizePolicy().hasHeightForWidth())
        self.next_btn.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/n/imgs/Fast Forward-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_btn.setIcon(icon2)
        self.next_btn.setIconSize(QtCore.QSize(25, 25))
        self.next_btn.setObjectName("next_btn")
        self.gridLayout.addWidget(self.next_btn, 0, 6, 1, 1)
        self.call_btn = QtGui.QPushButton(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.call_btn.sizePolicy().hasHeightForWidth())
        self.call_btn.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/n/imgs/Recycling-104.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.call_btn.setIcon(icon3)
        self.call_btn.setIconSize(QtCore.QSize(25, 25))
        self.call_btn.setObjectName("call_btn")
        self.gridLayout.addWidget(self.call_btn, 0, 5, 1, 1)
        self.widget_6 = QtGui.QWidget(self.widget_3)
        self.widget_6.setStyleSheet("background:#757780;\n"
"color:#fff;")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtGui.QLabel(self.widget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(220, 0))
        font = QtGui.QFont()
        font.setFamily("Alarabiya Font")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.terminal_lbl = QtGui.QLabel(self.widget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.terminal_lbl.sizePolicy().hasHeightForWidth())
        self.terminal_lbl.setSizePolicy(sizePolicy)
        self.terminal_lbl.setMinimumSize(QtCore.QSize(220, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.terminal_lbl.setFont(font)
        self.terminal_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.terminal_lbl.setObjectName("terminal_lbl")
        self.verticalLayout_5.addWidget(self.terminal_lbl)
        self.gridLayout.addWidget(self.widget_6, 0, 2, 1, 1)
        self.horizontalLayout.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "العميل الحالى", None, QtGui.QApplication.UnicodeUTF8))
        self.current_lbl.setText(QtGui.QApplication.translate("Form", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "عدد المنتظرين", None, QtGui.QApplication.UnicodeUTF8))
        self.waiting_lbl.setText(QtGui.QApplication.translate("Form", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.ext_btn.setToolTip(QtGui.QApplication.translate("Form", "اغلاق البرنامج", None, QtGui.QApplication.UnicodeUTF8))
        self.log_out.setToolTip(QtGui.QApplication.translate("Form", "تسجيل الخروج", None, QtGui.QApplication.UnicodeUTF8))
        self.next_btn.setText(QtGui.QApplication.translate("Form", "التالى", None, QtGui.QApplication.UnicodeUTF8))
        self.call_btn.setText(QtGui.QApplication.translate("Form", "نداء", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "رقم الشباك", None, QtGui.QApplication.UnicodeUTF8))
        self.terminal_lbl.setText(QtGui.QApplication.translate("Form", "0", None, QtGui.QApplication.UnicodeUTF8))

import source_rc
