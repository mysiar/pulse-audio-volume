# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/UIMainWindowForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(503, 89)
        MainWindow.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sinks = QtWidgets.QComboBox(self.centralwidget)
        self.sinks.setGeometry(QtCore.QRect(20, 20, 461, 25))
        self.sinks.setObjectName("sinks")
        self.volumenStepLabel = QtWidgets.QLabel(self.centralwidget)
        self.volumenStepLabel.setGeometry(QtCore.QRect(23, 55, 91, 17))
        self.volumenStepLabel.setObjectName("volumenStepLabel")
        self.volumeStep = QtWidgets.QComboBox(self.centralwidget)
        self.volumeStep.setGeometry(QtCore.QRect(110, 51, 60, 25))
        self.volumeStep.setObjectName("volumeStep")
        self.volumeUp = QtWidgets.QPushButton(self.centralwidget)
        self.volumeUp.setGeometry(QtCore.QRect(177, 51, 51, 25))
        self.volumeUp.setObjectName("volumeUp")
        self.volumeDown = QtWidgets.QPushButton(self.centralwidget)
        self.volumeDown.setGeometry(QtCore.QRect(238, 51, 51, 25))
        self.volumeDown.setObjectName("volumeDown")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.volumenStepLabel.setText(_translate("MainWindow", "Volume step"))
        self.volumeUp.setText(_translate("MainWindow", "Up"))
        self.volumeDown.setText(_translate("MainWindow", "Down"))
