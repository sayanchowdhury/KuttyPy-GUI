# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dio_adcLog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(363, 300)
        font = QtGui.QFont()
        font.setPointSize(9)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/control/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(True)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(3, 3, 3, 0)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.switcher = QtWidgets.QPushButton(Dialog)
        self.switcher.setObjectName("switcher")
        self.gridLayout.addWidget(self.switcher, 0, 3, 1, 1)
        self.log = QtWidgets.QCheckBox(Dialog)
        self.log.setObjectName("log")
        self.gridLayout.addWidget(self.log, 1, 0, 1, 1)
        self.configLayout = QtWidgets.QHBoxLayout()
        self.configLayout.setObjectName("configLayout")
        self.gridLayout.addLayout(self.configLayout, 2, 0, 1, 3)
        self.monitors = QtWidgets.QStackedWidget(Dialog)
        self.monitors.setObjectName("monitors")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gaugeLayout = QtWidgets.QGridLayout()
        self.gaugeLayout.setSpacing(3)
        self.gaugeLayout.setObjectName("gaugeLayout")
        self.gauge = Gauge(self.page)
        self.gauge.setObjectName("gauge")
        self.gaugeLayout.addWidget(self.gauge, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gaugeLayout)
        self.monitors.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graph = PlotWidget(self.page_2)
        self.graph.setObjectName("graph")
        self.horizontalLayout_2.addWidget(self.graph)
        self.monitors.addWidget(self.page_2)
        self.gridLayout.addWidget(self.monitors, 3, 0, 1, 4)
        self.options = QtWidgets.QComboBox(Dialog)
        self.options.setObjectName("options")
        self.gridLayout.addWidget(self.options, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.log_2 = QtWidgets.QCheckBox(Dialog)
        self.log_2.setObjectName("log_2")
        self.gridLayout.addWidget(self.log_2, 1, 3, 1, 1)

        self.retranslateUi(Dialog)
        self.monitors.setCurrentIndex(0)
        self.switcher.clicked.connect(Dialog.next)
        self.log_2.toggled['bool'].connect(Dialog.changeRange)
        self.options.currentIndexChanged['QString'].connect(Dialog.config)
        self.log.toggled['bool'].connect(Dialog.config)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sensor Reading"))
        self.switcher.setText(_translate("Dialog", "Data Logger"))
        self.log.setText(_translate("Dialog", "Log Read/Write calls"))
        self.label.setText(_translate("Dialog", "ADMUX"))
        self.log_2.setText(_translate("Dialog", "0-5000mV Range"))

from .gauge import Gauge
from pyqtgraph import PlotWidget
from . import res_rc
