# -*- coding: utf-8 -*-

import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.act_add_ui import act_add_ui
from link_to_database import LinkMysql

class act_add_panel(QWidget, act_add_ui):
    def __init__(self):
        super(act_add_panel,self).__init__()
        self.setupUi(self)
    def add_to_database(self):
        dateTime= self.time.date().toString('yyyy-MM-dd')
        print(dateTime)

        self.value=[]
        self.value.append(self.title_ln.text())
        self.value.append(dateTime)
        self.value.append(self.con_ln.toPlainText())
        self.value.append(1)
        
        
        
        print(self.value)
        sql = "INSERT INTO activity(acTitle,acTime,acContent,acbuilder) values (%s,%s,%s,%s)"
        
        if LinkMysql().commit_sql(sql,self.value):
                  QMessageBox.information(self,"温馨提示", "添加成功",QMessageBox.Ok)
                  print('You succeed')
        else:
                 QMessageBox.warning(self, '温馨提示','有错误发生',QMessageBox.Retry)
                 print('Something wrong')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    win =act_add_panel()
    win.show()
    sys.exit(app.exec_())
