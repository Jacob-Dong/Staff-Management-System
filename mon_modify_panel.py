# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.mon_modify_ui import mon_modify_ui
from link_to_database import LinkMysql


class mon_modify_panel(QWidget, mon_modify_ui):
    def __init__(self,user_id):
        super(mon_modify_panel,self).__init__()
        self.setupUi(self)
        self.user_id=user_id
        sql='select * from monthrecord where staId=%s'
        self.data=LinkMysql().select_sql(sql,user_id)

        self.mon_id.setText(str(self.data[0][0]))
        self.mon_name.setText(self.data[0][1])
        self.mon_date.setText(str(self.data[0][2]))
        self.mon_awa.setText(str(self.data[0][3]))
        self.mon_re.setText(self.data[0][4])
        

    def save_to_database(self):
        self.value=[]
        self.value.append(self.mon_id.text())
        self.value.append(self.mon_name.text())
        self.value.append(self.mon_date.text())
        self.value.append(self.mon_awa.text())
        self.value.append(self.mon_re.toPlainText())

        print(self.value)
        sql0="delete from monthrecord where staId=%s"
        LinkMysql().commit_sql(sql0,self.user_id)
        sql = "INSERT INTO monthrecord values (%s,%s,%s,%s,%s)"
        if LinkMysql().commit_sql(sql,self.value):
           QMessageBox.information(self,"温馨提示", "修改成功",QMessageBox.Ok)
           print('You succeed')
        else:
           QMessageBox.warning(self, '温馨提示','有错误发生,请重试',QMessageBox.Retry)
           print('Something wrong')
        self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    user_id=1
    win = mon_modify_panel(user_id)
    win.show()
    sys.exit(app.exec_())
