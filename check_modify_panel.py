# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.Qt import QDate

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.check_modify_ui import check_modify_ui
from link_to_database import LinkMysql


class check_modify_panel(QWidget, check_modify_ui):
    def __init__(self,user_id):
        super(check_modify_panel,self).__init__()
        self.setupUi(self)
        self.user_id=user_id
        sql='select * from checking_in where staId=%s'
        self.data=LinkMysql().select_sql(sql,user_id)

        

        self.ch_id.setText(str(self.data[0][0]))
        self.ch_name.setText(self.data[0][1])
        self.ch_dep.setText(self.data[0][2])
        self.ch_work.setText(self.data[0][3])
        self.ch_date.setDate(QDate(self.data[0][4]))
        

    def save_to_database(self):
        da=self.ch_date.date().toString('yyyy-MM-dd')
        self.value=[]
        self.value.append(self.ch_id.text())
        self.value.append(self.ch_name.text())
        self.value.append(self.ch_dep.text())
        self.value.append(self.ch_work.text())
        self.value.append(da)

        print(self.value)
        sql0="delete from checking_in where staId=%s"
        LinkMysql().commit_sql(sql0,self.user_id)
        sql = "INSERT INTO checking_in values (%s,%s,%s,%s,%s)"
        if LinkMysql().commit_sql(sql,self.value):
           QMessageBox.information(self,"温馨提示", "修改成功",QMessageBox.Ok)
           print('You succeed')
        else:
           QMessageBox.warning(self, '温馨提示','有错误发生,请重试',QMessageBox.Retry)
           print('Something wrong')
        self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    user_id=2
    win = check_modify_panel(user_id)
    win.show()
    sys.exit(app.exec_())
