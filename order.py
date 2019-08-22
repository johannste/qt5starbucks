from PyQt5 import QtCore, QtWidgets


class UiOrder:
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(893, 489)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pbDrink = QtWidgets.QPushButton(self.centralwidget)
        self.pbDrink.setGeometry(QtCore.QRect(510, 20, 101, 41))
        self.pbDrink.setObjectName("pbDrink")

        self.pbFood = QtWidgets.QPushButton(self.centralwidget)
        self.pbFood.setGeometry(QtCore.QRect(510, 80, 101, 41))
        self.pbFood.setObjectName("pbFood")

        self.pbSeckill = QtWidgets.QPushButton(self.centralwidget)
        self.pbSeckill.setGeometry(QtCore.QRect(510, 140, 101, 41))
        self.pbSeckill.setObjectName("pbSeckill")
        
        self.l_balance_0 = QtWidgets.QLabel(self.centralwidget)
        self.l_balance_0.setGeometry(QtCore.QRect(510, 200, 111, 21))
        self.l_balance_0.setObjectName("l_balance_0")
        self.l_balance_1 = QtWidgets.QLabel(self.centralwidget)
        self.l_balance_1.setGeometry(QtCore.QRect(510, 230, 72, 15))
        self.l_balance_1.setObjectName("l_balance_1")
        self.l_balance_2 = QtWidgets.QLabel(self.centralwidget)
        self.l_balance_2.setGeometry(QtCore.QRect(580, 230, 61, 16))
        self.l_balance_2.setObjectName("l_balance_2")

        self.lImage_2 = QtWidgets.QLabel(self.centralwidget)
        self.lImage_2.setGeometry(QtCore.QRect(590, 290, 21, 16))
        self.lImage_2.setObjectName("lImage_2")
        self.lName_2 = QtWidgets.QLabel(self.centralwidget)
        self.lName_2.setGeometry(QtCore.QRect(510, 290, 72, 15))
        self.lName_2.setObjectName("lName_2")
        self.l_coupon = QtWidgets.QLabel(self.centralwidget)
        self.l_coupon.setGeometry(QtCore.QRect(510, 260, 81, 21))
        self.l_coupon.setObjectName("l_coupon")
        self.lPrice_3 = QtWidgets.QLabel(self.centralwidget)
        self.lPrice_3.setGeometry(QtCore.QRect(640, 20, 61, 21))
        self.lPrice_3.setObjectName("lPrice_3")

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 10, 480, 480))
        self.logo.setObjectName("logo")


        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(640, 40, 241, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(70)
        self.pb_del = QtWidgets.QPushButton(self.centralwidget)
        self.pb_del.setGeometry(QtCore.QRect(640, 290, 71, 31))
        self.pb_del.setObjectName("pbOrder_del")
        self.pb_num = QtWidgets.QPushButton(self.centralwidget)
        self.pb_num.setGeometry(QtCore.QRect(640, 350, 91, 31))
        self.pb_num.setObjectName("pbOrder_5")
        self.pb_tip = QtWidgets.QPushButton(self.centralwidget)
        self.pb_tip.setGeometry(QtCore.QRect(750, 350, 91, 31))
        self.pb_tip.setObjectName("pb_tip")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 893, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "星巴克"))
        self.logo.setText(_translate("MainWindow", "logo"))

        self.pbDrink.setText(_translate("MainWindow", "饮料"))
        self.pbFood.setText(_translate("MainWindow", "美食"))
        self.pbSeckill.setText(_translate("MainWindow", "秒杀"))

        self.l_balance_0.setText(_translate("MainWindow", "会员储值卡余额"))
        self.l_balance_1.setText(_translate("MainWindow", "钱"))
        self.l_balance_2.setText(_translate("MainWindow", "元"))

        self.l_coupon.setText(_translate("MainWindow", "您的优惠券"))
        self.lName_2.setText(_translate("MainWindow", "券"))
        self.lImage_2.setText(_translate("MainWindow", "张"))

        self.lPrice_3.setText(_translate("MainWindow", "您的订单"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "数量"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "价格/元"))

        self.pb_del.setText(_translate("MainWindow", "清空"))
        self.pb_num.setText(_translate("MainWindow", "结算"))
        self.pb_tip.setText(_translate("MainWindow", "打印小票"))
