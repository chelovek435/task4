from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt6 import uic
import sys
import sqlite3 as sl


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.db_name = 'coffee.sqlite'
        uic.loadUi("main.ui", self)
        self.upd_btn.clicked.connect(self.upd_table)

    def upd_table(self):
        rows, headers = self.get_data()

        self.table.clear()

        if not rows or not headers:
            return

        # задаем параметры для таблицы
        self.table.setRowCount(len(rows))
        self.table.setColumnCount(len(rows[0]))

        # устанавливаем заголовки
        self.table.setHorizontalHeaderLabels(headers)

        # записываем значения в каждую ячейку
        for r, row in enumerate(rows):
            for c, val in enumerate(row):
                display_val = "" if val is None else str(val)
                self.table.setItem(r, c, QTableWidgetItem(display_val))

    def get_data(self):
        with sl.connect(self.db_name) as con:
            cur = con.cursor()
            cur.execute('SELECT * FROM coffee')
            headers = [h[0] for h in cur.description]
            rows = cur.fetchall()
            return rows, headers


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
