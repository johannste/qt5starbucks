from PyQt5 import QtCore, QtWidgets


class UiFood:
    def __init__(self, Form):
        Form.setObjectName("Form")
        Form.resize(728, 393)

        self.lImage_1 = QtWidgets.QLabel(Form)
        self.lImage_1.setGeometry(QtCore.QRect(60, 20, 161, 171))
        self.lImage_1.setObjectName("lImage_1")
        self.lName_1 = QtWidgets.QLabel(Form)
        self.lName_1.setGeometry(QtCore.QRect(105, 220, 131, 21))
        self.lName_1.setObjectName("lName_1")
        self.lPrice_1 = QtWidgets.QLabel(Form)
        self.lPrice_1.setGeometry(QtCore.QRect(102, 250, 72, 15))
        self.lPrice_1.setObjectName("lPrice_1")
        self.pbOrder_1 = QtWidgets.QPushButton(Form)
        self.pbOrder_1.setGeometry(QtCore.QRect(90, 280, 91, 31))
        self.pbOrder_1.setObjectName("pbOrder_1")

        self.lImage_2 = QtWidgets.QLabel(Form)
        self.lImage_2.setGeometry(QtCore.QRect(300, 20, 171, 171))
        self.lImage_2.setObjectName("lImage_2")
        self.lName_2 = QtWidgets.QLabel(Form)
        self.lName_2.setGeometry(QtCore.QRect(345, 220, 111, 21))
        self.lName_2.setObjectName("lName_2")
        self.lPrice_2 = QtWidgets.QLabel(Form)
        self.lPrice_2.setGeometry(QtCore.QRect(352, 250, 72, 15))
        self.lPrice_2.setObjectName("lPrice_2")
        self.pbOrder_2 = QtWidgets.QPushButton(Form)
        self.pbOrder_2.setGeometry(QtCore.QRect(340, 280, 93, 31))
        self.pbOrder_2.setObjectName("pbOrder_2")

        self.pbOrder_3 = QtWidgets.QPushButton(Form)
        self.pbOrder_3.setGeometry(QtCore.QRect(560, 280, 101, 41))
        self.pbOrder_3.setObjectName("pbOrder_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        self.lImage_1.setText(_translate("Form", "TextLabel"))
        self.lName_1.setText(_translate("Form", "美式松饼"))
        self.lPrice_1.setText(_translate("Form", "钱1"))
        self.pbOrder_1.setText(_translate("Form", "加入订单"))

        self.lImage_2.setText(_translate("Form", "TextLabel"))
        self.lName_2.setText(_translate("Form", "蜂蜜提子司康"))
        self.lPrice_2.setText(_translate("Form", "钱2"))
        self.pbOrder_2.setText(_translate("Form", "加入订单"))

        self.pbOrder_3.setText(_translate("Form", "返回"))
