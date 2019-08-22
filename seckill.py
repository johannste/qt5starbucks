from PyQt5 import QtCore, QtWidgets


class UiSecKill:
    def __init__(self, Form):
        Form.setObjectName("Form")
        Form.resize(639, 335)

        self.lImage_1 = QtWidgets.QLabel(Form)
        self.lImage_1.setGeometry(QtCore.QRect(30, 30, 141, 141))
        self.lImage_1.setObjectName("lImage_1")
        self.lName_1 = QtWidgets.QLabel(Form)
        self.lName_1.setGeometry(QtCore.QRect(50, 180, 91, 16))
        self.lName_1.setObjectName("lName_1")
        self.lPrice_1 = QtWidgets.QLabel(Form)
        self.lPrice_1.setGeometry(QtCore.QRect(11, 220, 201, 20))
        self.lPrice_1.setObjectName("lPrice_1")
        self.lTime_1 = QtWidgets.QLabel(Form)
        self.lTime_1.setGeometry(QtCore.QRect(20, 200, 161, 16))
        self.lTime_1.setObjectName("lTime_1")
        self.pbOrder_1 = QtWidgets.QPushButton(Form)
        self.pbOrder_1.setGeometry(QtCore.QRect(50, 240, 93, 31))
        self.pbOrder_1.setObjectName("pbOrder_1")

        self.lImage_2 = QtWidgets.QLabel(Form)
        self.lImage_2.setGeometry(QtCore.QRect(280, 30, 151, 141))
        self.lImage_2.setObjectName("lImage_2")
        self.lName_2 = QtWidgets.QLabel(Form)
        self.lName_2.setGeometry(QtCore.QRect(310, 180, 61, 16))
        self.lName_2.setObjectName("lName_2")
        self.lPrice_2 = QtWidgets.QLabel(Form)
        self.lPrice_2.setGeometry(QtCore.QRect(261, 220, 201, 20))
        self.lPrice_2.setObjectName("lPrice_2")
        self.lTime_2 = QtWidgets.QLabel(Form)
        self.lTime_2.setGeometry(QtCore.QRect(270, 200, 161, 16))
        self.lTime_2.setObjectName("lTime_2")
        self.pbOrder_2 = QtWidgets.QPushButton(Form)
        self.pbOrder_2.setGeometry(QtCore.QRect(300, 240, 93, 31))
        self.pbOrder_2.setObjectName("pbOrder_2")

        self.pbOrder_3 = QtWidgets.QPushButton(Form)
        self.pbOrder_3.setGeometry(QtCore.QRect(490, 250, 101, 31))
        self.pbOrder_3.setObjectName("pbOrder_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        self.lImage_1.setText(_translate("Form", "TextLabel"))
        self.lName_1.setText(_translate("Form", "9oz 臻选玻璃杯"))
        self.lPrice_1.setText(_translate("Form", "钱1"))
        self.lTime_1.setText(_translate("Form", "2019.08.1-2018.08.31"))
        self.pbOrder_1.setText(_translate("Form", "加入订单"))

        self.lImage_2.setText(_translate("Form", "TextLabel"))
        self.lName_2.setText(_translate("Form", "12oz 纯黑/古铜亮面品牌桌面杯"))
        self.lPrice_2.setText(_translate("Form", "钱2"))
        self.lTime_2.setText(_translate("Form", "2019.11.1-2018.11.11"))
        self.pbOrder_2.setText(_translate("Form", "加入订单"))

        self.pbOrder_3.setText(_translate("Form", "返回"))
