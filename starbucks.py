from order import UiOrder
from drink import UiDrink
from food import UiFood
from seckill import UiSecKill
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class STARBUCKS(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui_order = UiOrder(self)

        pb_del = self.ui_order.pb_del
        pb_del.clicked.connect(self.order_del)
        pb_num = self.ui_order.pb_num
        pb_num.clicked.connect(self.order_num)
        self.pb_tip = self.ui_order.pb_tip
        self.pb_tip.clicked.connect(self.order_tip)

        self.pb_tip.setEnabled(False)

        self.num = []
        self.new_num = []

    def person(self):
        self.ui_order.logo.setPixmap(QPixmap('images/th.jpg'))
        # self.ui_order.lName_3.setScaledContents(True)
        self.balance = 200
        self.coupons = 1
        self.count = 0
        self.ui_order.l_balance_2.setText(str(self.balance))
        self.ui_order.lName_2.setText(str(self.coupons))
        starbucks.show()

    def order_del(self):
        drink.bt1 = 0
        drink.bt2 = 0
        drink.bt3 = 0
        drink.bt4 = 0
        drink.bt5 = 0
        drink.bt6 = 0
        food.bt1 = 0
        food.bt2 = 0
        food.bt3 = 0
        seckill.bt1 = 0
        seckill.bt2 = 0
        seckill.bt3 = 0
        for i in range(starbucks.ui_order.tableWidget.rowCount()):
            starbucks.ui_order.tableWidget.removeRow(0)
        self.ui_order.l_balance_2.setText(str(self.balance))

    def order_num(self):
        self.pb_tip.setEnabled(True)
        for row_index in range(starbucks.ui_order.tableWidget.rowCount()):
            self.num.append(starbucks.ui_order.tableWidget.item(row_index, 2).text())

        self.new_num = eval('[' + (','.join(self.num)) + ']')
        self.money = sum(self.new_num)

        if self.money > 0:
            if self.coupons >= 1 and QMessageBox.information(self, "温馨提示", "是否使用优惠券",
                                                             QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                self.coupons -= 1
                self.count = 20
                self.ui_order.lName_2.setText(str(self.coupons))
            else:
                self.count = 0

            if self.balance >= (self.money - self.count):
                QMessageBox.information(self, "恭喜您", "付款成功！", QMessageBox.Yes)
                if self.count != 0:
                    self.balance += self.count - self.money
                else:
                    self.balance -= self.money
                self.num = []
                self.new_num = []
                self.order_del()
            else:
                QMessageBox.information(self, "交易失败！", QMessageBox.Yes)

    def order_tip(self):
        with open("tip.log", "a+", encoding='utf-8') as f:
            for row_index in range(starbucks.ui_order.tableWidget.rowCount()):
                for column_index in range(starbucks.ui_order.tableWidget.columnCount()):
                    f.write(starbucks.ui_order.tableWidget.item(row_index, column_index).text() + "\n")
            f.write("合计：" + str(self.money) + "元")
        f.close()


class Drink(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.UiDrink = UiDrink(self)

        self.bt1 = 0
        self.bt2 = 0
        self.bt3 = 0
        self.bt4 = 0
        self.bt5 = 0
        self.bt6 = 0

        pb_affogato = self.UiDrink.pbOrder_1
        pb_affogato.clicked.connect(self.order_affogato)
        btn_cold_brew_malt = self.UiDrink.pbOrder_2
        btn_cold_brew_malt.clicked.connect(self.order_cold_brew_malt)
        btn_cold_brew_float = self.UiDrink.pbOrder_3
        btn_cold_brew_float.clicked.connect(self.order_cold_brew_float)
        btn_instore_nitro_cold_brew_float = self.UiDrink.pbOrder_4
        btn_instore_nitro_cold_brew_float.clicked.connect(self.order_instore_nitro_cold_brew_float)
        btn_vanilla_flavor_sweet_cream_cold_brew = self.UiDrink.pbOrder_5
        btn_vanilla_flavor_sweet_cream_cold_brew.clicked.connect(self.order_vanilla_flavor_sweet_cream_cold_brew)
        btn_return = self.UiDrink.pbOrder_back
        btn_return.clicked.connect(self.drink_show)

    def drink_order(self):
        self.UiDrink.lImage_1.setPixmap(QPixmap('images/drink/affogato.jpg'))
        self.UiDrink.lImage_1.setScaledContents(True)
        self.UiDrink.lImage_2.setPixmap(QPixmap('images/drink/cold-brew-malt.jpg'))
        self.UiDrink.lImage_2.setScaledContents(True)
        self.UiDrink.lImage_3.setPixmap(QPixmap('images/drink/cold-brew-float.jpg'))
        self.UiDrink.lImage_3.setScaledContents(True)
        self.UiDrink.lImage_4.setPixmap(QPixmap('images/drink/instore-nitro-cold-brew-float.jpg'))
        self.UiDrink.lImage_4.setScaledContents(True)
        self.UiDrink.lImage_5.setPixmap(QPixmap('images/drink/vanilla-flavor-sweet-cream-cold-brew.jpg'))
        self.UiDrink.lImage_5.setScaledContents(True)

        self.affogato = 42.5
        self.cold_brew_malt = 41.0
        self.cold_brew_float = 43.0
        self.instore_nitro_cold_brew_float = 43.5
        self.vanilla_flavor_sweet_cream_cold_brew = 40.0

        self.UiDrink.lPrice_1.setText(str(self.affogato) + "元/份")
        self.UiDrink.lPrice_2.setText(str(self.cold_brew_malt) + "元/份")
        self.UiDrink.lPrice_3.setText(str(self.cold_brew_float) + "元/份")
        self.UiDrink.lPrice_4.setText(str(self.instore_nitro_cold_brew_float) + "元/份")
        self.UiDrink.lPrice_5.setText(str(self.vanilla_flavor_sweet_cream_cold_brew) + "元/份")
        drink.show()

    def order_affogato(self):
        self.bt1 += 1

    def order_cold_brew_malt(self):
        self.bt2 += 1

    def order_cold_brew_float(self):
        self.bt3 += 1

    def order_instore_nitro_cold_brew_float(self):
        self.bt4 += 1

    def order_vanilla_flavor_sweet_cream_cold_brew(self):
        self.bt5 += 1

    def drink_show(self):
        self.bt6 += 1

        drink.hide()

        self.num_affogato = self.affogato * self.bt1
        self.num_cold_brew_malt = self.cold_brew_malt * self.bt2
        self.num_cold_brew_float = self.cold_brew_float * self.bt3
        self.num_instore_nitro_cold_brew_float = self.instore_nitro_cold_brew_float * self.bt4
        self.num_vanilla_flavor_sweet_cream_cold_brew = self.vanilla_flavor_sweet_cream_cold_brew * self.bt5

        if self.bt6 > 1:
            for row_index in range(starbucks.ui_order.tableWidget.rowCount()):
                name.append(starbucks.ui_order.tableWidget.item(row_index, 0).text())
            if '阿馥奇朵™' in name:
                starbucks.ui_order.tableWidget.setItem(name.index('阿馥奇朵™'), 1, QTableWidgetItem("×" + str(self.bt1)))
                starbucks.ui_order.tableWidget.setItem(name.index('阿馥奇朵™'), 2, QTableWidgetItem(str(self.num_affogato)))
            if '阿馥奇朵™' not in name:
                if self.bt1 != 0:
                    row_count = starbucks.ui_order.tableWidget.rowCount()
                    starbucks.ui_order.tableWidget.insertRow(row_count)
                    starbucks.ui_order.tableWidget.setItem(row_count, 0, QTableWidgetItem(drink.UiDrink.lName_1.text()))
                    starbucks.ui_order.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                    starbucks.ui_order.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_affogato)))
            if '麦芽雪冷萃™' in name:
                starbucks.ui_order.tableWidget.setItem(name.index('麦芽雪冷萃™'), 1, QTableWidgetItem("×" + str(self.bt2)))
                starbucks.ui_order.tableWidget.setItem(name.index('麦芽雪冷萃™'), 2,
                                                       QTableWidgetItem(str(self.num_cold_brew_malt)))
            if '麦芽雪冷萃™' not in name:
                if self.bt2 != 0:
                    row_count = starbucks.ui_order.tableWidget.rowCount()
                    starbucks.ui_order.tableWidget.insertRow(row_count)
                    starbucks.ui_order.tableWidget.setItem(row_count, 0, QTableWidgetItem(drink.UiDrink.lName_2.text()))
                    starbucks.ui_order.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                    starbucks.ui_order.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_cold_brew_malt)))
            if '冷萃浮乐朵™' in name:
                starbucks.ui_order.tableWidget.setItem(name.index('冷萃浮乐朵™'), 1, QTableWidgetItem("×" + str(self.bt3)))
                starbucks.ui_order.tableWidget.setItem(name.index('冷萃浮乐朵™'), 2,
                                                       QTableWidgetItem(str(self.num_cold_brew_float)))
            if '冷萃浮乐朵™' not in name:
                if self.bt3 != 0:
                    row_count = starbucks.ui_order.tableWidget.rowCount()
                    starbucks.ui_order.tableWidget.insertRow(row_count)
                    starbucks.ui_order.tableWidget.setItem(row_count, 0, QTableWidgetItem(drink.UiDrink.lName_3.text()))
                    starbucks.ui_order.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt3)))
                    starbucks.ui_order.tableWidget.setItem(row_count, 2,
                                                           QTableWidgetItem(str(self.num_cold_brew_float)))
            if '气致™冷萃浮乐朵™' in name:
                starbucks.ui_order.tableWidget.setItem(name.index('气致™冷萃浮乐朵™'), 1,
                                                       QTableWidgetItem("×" + str(self.bt4)))
                starbucks.ui_order.tableWidget.setItem(name.index('气致™冷萃浮乐朵™'), 2,
                                                       QTableWidgetItem(str(self.instore_nitro_cold_brew_float)))
            if '气致™冷萃浮乐朵™' not in name:
                if self.bt4 != 0:
                    row_count = starbucks.ui_order.tableWidget.rowCount()
                    starbucks.ui_order.tableWidget.insertRow(row_count)
                    starbucks.ui_order.tableWidget.setItem(row_count, 0,
                                                           QTableWidgetItem(drink.UiDrink.lName_4.text()))
                    starbucks.ui_order.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt4)))
                    starbucks.ui_order.tableWidget.setItem(row_count, 2,
                                                           QTableWidgetItem(str(self.instore_nitro_cold_brew_float)))
            if '轻甜奶油冷萃' in name:
                starbucks.ui_order.tableWidget.setItem(name.index('轻甜奶油冷萃'), 1, QTableWidgetItem("×" + str(self.bt5)))
                starbucks.ui_order.tableWidget.setItem(name.index('轻甜奶油冷萃'), 2, QTableWidgetItem(
                    str(self.num_vanilla_flavor_sweet_cream_cold_brew)))
            if '轻甜奶油冷萃' not in name:
                if self.bt5 != 0:
                    row_count = starbucks.ui_order.tableWidget.rowCount()
                    starbucks.ui_order.tableWidget.insertRow(row_count)
                    starbucks.ui_order.tableWidget.setItem(row_count, 0,
                                                           QTableWidgetItem(drink.UiDrink.lName_5.text()))
                    starbucks.ui_order.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt5)))
                    starbucks.ui_order.tableWidget.setItem(row_count, 2, QTableWidgetItem(
                        str(self.num_vanilla_flavor_sweet_cream_cold_brew)))
        else:
            if self.bt1 != 0:
                row_count = starbucks.ui_order.tableWidget.rowCount()
                starbucks.ui_order.tableWidget.insertRow(row_count)
                starbucks.ui_order.tableWidget.setItem(row_count, 0, QTableWidgetItem(drink.UiDrink.lName_1.text()))
                starbucks.ui_order.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                starbucks.ui_order.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_affogato)))
            if self.bt2 != 0:
                row_count = starbucks.ui_order.tableWidget.rowCount()
                starbucks.ui_order.tableWidget.insertRow(row_count)
                starbucks.ui_order.tableWidget.setItem(row_count, 0, QTableWidgetItem(drink.UiDrink.lName_2.text()))
                starbucks.ui_order.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                starbucks.ui_order.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_cold_brew_malt)))
            if self.bt3 != 0:
                row_count = starbucks.ui_order.tableWidget.rowCount()
                starbucks.ui_order.tableWidget.insertRow(row_count)
                starbucks.ui_order.tableWidget.setItem(row_count, 0, QTableWidgetItem(drink.UiDrink.lName_3.text()))
                starbucks.ui_order.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt3)))
                starbucks.ui_order.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_cold_brew_float)))
            if self.bt4 != 0:
                row_count = starbucks.ui_order.tableWidget.rowCount()
                starbucks.ui_order.tableWidget.insertRow(row_count)
                starbucks.ui_order.tableWidget.setItem(row_count, 0, QTableWidgetItem(drink.UiDrink.lName_4.text()))
                starbucks.ui_order.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt4)))
                starbucks.ui_order.tableWidget.setItem(row_count, 2,
                                                       QTableWidgetItem(str(self.instore_nitro_cold_brew_float)))
            if self.bt5 != 0:
                row_count = starbucks.ui_order.tableWidget.rowCount()
                starbucks.ui_order.tableWidget.insertRow(row_count)
                starbucks.ui_order.tableWidget.setItem(row_count, 0, QTableWidgetItem(drink.UiDrink.lName_5.text()))
                starbucks.ui_order.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt5)))
                starbucks.ui_order.tableWidget.setItem(row_count, 2, QTableWidgetItem(
                    str(self.num_vanilla_flavor_sweet_cream_cold_brew)))


class Food(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.UiFood = UiFood(self)

        self.bt1 = 0
        self.bt2 = 0
        self.bt3 = 0
        btn_pack1 = self.UiFood.pbOrder_1
        btn_pack1.clicked.connect(self.order_american_style_pancakes)
        btn_pack2 = self.UiFood.pbOrder_2
        btn_pack2.clicked.connect(self.order_honey_raisin_scone)
        btn_return = self.UiFood.pbOrder_3
        btn_return.clicked.connect(self.food_show)

    def food_order(self):
        self.UiFood.lImage_1.setPixmap(QPixmap('images/food/american-style-pancakes.jpg'))
        self.UiFood.lImage_1.setScaledContents(True)
        self.UiFood.lImage_2.setPixmap(QPixmap('images/food/honey-raisin-scone.jpg'))
        self.UiFood.lImage_2.setScaledContents(True)

        self.price_pack1 = 89.0
        self.price_pack2 = 67.0
        self.UiFood.lPrice_1.setText(str(self.price_pack1) + "元/份")
        self.UiFood.lPrice_2.setText(str(self.price_pack2) + "元/份")
        food.show()

    def order_american_style_pancakes(self):
        self.bt1 += 1

    def order_honey_raisin_scone(self):
        self.bt2 += 1

    def food_show(self):
        self.bt3 += 1

        food.hide()

        self.num_pack1 = self.price_pack1 * self.bt1
        self.num_pack2 = self.price_pack2 * self.bt2

        if self.bt3 > 1:
            for row_index in range(starbucks.ui_order.tableWidget.rowCount()):
                name.append(starbucks.ui_order.tableWidget.item(row_index, 0).text())
            if '美式松饼' in name:
                starbucks.ui_order.tableWidget.setItem(name.index('美式松饼'), 1, QTableWidgetItem("×" + str(self.bt1)))
                starbucks.ui_order.tableWidget.setItem(name.index('美式松饼'), 2, QTableWidgetItem(str(self.num_pack1)))
            if '美式松饼' not in name:
                if self.bt1 != 0:
                    row_count = starbucks.ui_order.tableWidget.rowCount()
                    starbucks.ui_order.tableWidget.insertRow(row_count)
                    starbucks.ui_order.tableWidget.setItem(row_count, 0,
                                                           QTableWidgetItem(food.UiFood.lName_1.text()))
                    starbucks.ui_order.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                    starbucks.ui_order.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_pack1)))
            if '蜂蜜提子司康' in name:
                starbucks.ui_order.tableWidget.setItem(name.index('蜂蜜提子司康'), 1, QTableWidgetItem("×" + str(self.bt2)))
                starbucks.ui_order.tableWidget.setItem(name.index('蜂蜜提子司康'), 2, QTableWidgetItem(str(self.num_pack2)))
            if '蜂蜜提子司康' not in name:
                if self.bt2 != 0:
                    row_count = starbucks.ui_order.tableWidget.rowCount()
                    starbucks.ui_order.tableWidget.insertRow(row_count)
                    starbucks.ui_order.tableWidget.setItem(row_count, 0,
                                                           QTableWidgetItem(food.UiFood.lName_2.text()))
                    starbucks.ui_order.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                    starbucks.ui_order.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_pack2)))
        else:
            if self.bt1 != 0:
                row_count = starbucks.ui_order.tableWidget.rowCount()
                starbucks.ui_order.tableWidget.insertRow(row_count)
                starbucks.ui_order.tableWidget.setItem(row_count, 0, QTableWidgetItem(food.UiFood.lName_1.text()))
                starbucks.ui_order.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                starbucks.ui_order.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_pack1)))
            if self.bt2 != 0:
                row_count = starbucks.ui_order.tableWidget.rowCount()
                starbucks.ui_order.tableWidget.insertRow(row_count)
                starbucks.ui_order.tableWidget.setItem(row_count, 0, QTableWidgetItem(food.UiFood.lName_2.text()))
                starbucks.ui_order.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                starbucks.ui_order.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_pack2)))


class Seckill(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.UiSecKill = UiSecKill(self)

        self.bt1 = 0
        self.bt3 = 0
        btn_act1 = self.UiSecKill.pbOrder_1
        btn_act1.clicked.connect(self.order_9oz_reserve_glass_cup)
        btn_act2 = self.UiSecKill.pbOrder_2
        btn_act2.clicked.connect(self.order_12oz_black_bronze_brand_handle_mug)
        btn_return = self.UiSecKill.pbOrder_3
        btn_return.clicked.connect(self.seckill_show)

    def seckill_order(self):
        self.UiSecKill.lImage_1.setPixmap(QPixmap('images/seckill/9oz-reserve-glass-cup.jpg'))
        self.UiSecKill.lImage_1.setScaledContents(True)
        self.UiSecKill.lImage_2.setPixmap(QPixmap('images/seckill/12oz-black-bronze-brand-handle-mug.jpg'))
        self.UiSecKill.lImage_2.setScaledContents(True)

        self.price_act1 = 29.0
        self.price_act2 = 69.0
        self.UiSecKill.lPrice_1.setText(str(self.price_act1) + "元/份  原价:" + str(self.price_act1 + 7) + "元/份")
        self.UiSecKill.lPrice_2.setText(str(self.price_act2) + "元/份  原价:" + str(self.price_act2 + 10) + "元/份")
        seckill.show()

    def order_9oz_reserve_glass_cup(self):
        self.bt1 += 1

    def order_12oz_black_bronze_brand_handle_mug(self):
        QMessageBox.information(self, "对不起", "活动还没有开始，敬请期待！", QMessageBox.Yes)

    def seckill_show(self):
        self.bt3 += 1

        seckill.hide()

        self.num_act1 = self.price_act1 * self.bt1

        if self.bt3 > 1:
            for row_index in range(starbucks.ui_order.tableWidget.rowCount()):
                name.append(starbucks.ui_order.tableWidget.item(row_index, 0).text())
            if '9oz 臻选玻璃杯' in name:
                starbucks.ui_order.tableWidget.setItem(name.index('9oz 臻选玻璃杯'), 1,
                                                       QTableWidgetItem("×" + str(self.bt1)))
                starbucks.ui_order.tableWidget.setItem(name.index('9oz 臻选玻璃杯'), 2, QTableWidgetItem(str(self.num_act1)))
            if '9oz 臻选玻璃杯' not in name:
                if self.bt1 != 0:
                    row_count = starbucks.ui_order.tableWidget.rowCount()
                    starbucks.ui_order.tableWidget.insertRow(row_count)
                    starbucks.ui_order.tableWidget.setItem(row_count, 0,
                                                           QTableWidgetItem(seckill.UiSecKill.lName_1.text()))
                    starbucks.ui_order.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                    starbucks.ui_order.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_act1)))
        else:
            if self.bt1 != 0:
                row_count = starbucks.ui_order.tableWidget.rowCount()
                starbucks.ui_order.tableWidget.insertRow(row_count)
                starbucks.ui_order.tableWidget.setItem(row_count, 0,
                                                       QTableWidgetItem(seckill.UiSecKill.lName_1.text()))
                starbucks.ui_order.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                starbucks.ui_order.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_act1)))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    starbucks = STARBUCKS()
    drink = Drink()
    food = Food()
    seckill = Seckill()

    starbucks.person()

    pb_drink = starbucks.ui_order.pbDrink
    pb_drink.clicked.connect(drink.drink_order)
    pb_food = starbucks.ui_order.pbFood
    pb_food.clicked.connect(food.food_order)
    pb_seckill = starbucks.ui_order.pbSeckill
    pb_seckill.clicked.connect(seckill.seckill_order)

    name = []

    sys.exit(app.exec_())
