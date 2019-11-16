import sys, sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.btn_open.clicked.connect(self.open)

        self.con_all_sorts = sqlite3.connect('coffee.sqlite.db')

    def open(self):
        cur = self.con_all_sorts.cursor()
        number_of_sorts = len(list(cur.execute('select * from sorts')))
        self.table_coffee.setRowCount(number_of_sorts)
        sorts = list(cur.execute('select * from sorts'))
        if sorts:
            for i in range(number_of_sorts):
                self.table_coffee.setItem(i, 0, QTableWidgetItem(str(sorts[i][0])))
                self.table_coffee.setItem(i, 1, QTableWidgetItem(str(sorts[i][1])))
                self.table_coffee.setItem(i, 2, QTableWidgetItem(str(sorts[i][2])))
                self.table_coffee.setItem(i, 3, QTableWidgetItem(str(sorts[i][3])))
                self.table_coffee.setItem(i, 4, QTableWidgetItem(str(sorts[i][4])))
                self.table_coffee.setItem(i, 5, QTableWidgetItem(str(sorts[i][5])))
                self.table_coffee.setItem(i, 6, QTableWidgetItem(str(sorts[i][6])))


app = QApplication(sys.argv)
ex = Coffee()
ex.show()
sys.exit(app.exec_())