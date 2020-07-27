# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_Dialog(object):
    def setupUi(self, Dialog, index, BGMs):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1117, 759)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 130, 660, 499))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(790, 120, 291, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(800, 580, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(960, 580, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(270, 60, 241, 31))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog, index, BGMs)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog, index, BGMs):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        png = QPixmap("./output_data/fig" + str(index) + ".png")
        BGM_result_text = BGMs[0] + ' , ' + BGMs[1] + ' , ' + BGMs[2]

        self.label.setPixmap(png)
        self.label_2.setText(_translate("Dialog", "最热门BGM前三类"))
        self.label_3.setText(_translate("Dialog", BGM_result_text))
        self.label_4.setText(_translate("Dialog", "推荐音乐示例"))
        self.label_5.setText(_translate("Dialog", "Result2"))
        self.pushButton.setText(_translate("Dialog", "播放"))
        self.pushButton_2.setText(_translate("Dialog", "停止"))
        self.label_6.setText(_translate("Dialog", "热门带货视频音频聚类图"))
