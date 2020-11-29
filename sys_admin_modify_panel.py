# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.sys_admin_modify_ui import sys_admin_modify_ui
from link_to_database import LinkMysql


class sys_admin_modify_panel(QWidget, sys_admin_modify_ui):
    def __init__(self,user_id):
        super(sys_admin_modify_panel,self).__init__()
        self.setupUi(self)
        self.user_id=user_id
        sql='select * from sys_admin where aId=%s'
        self.data=LinkMysql().select_sql(sql,user_id)

        self.id_ln.setText(str(self.data[0][0]))
        self.name_ln.setText(self.data[0][1])
        self.pw_ln.setText(self.data[0][2])
        self.tel_ln.setText(self.data[0][3])
        self.mail_ln.setText(str(self.data[0][4]))
        self.dep_ln.setText(self.data[0][5])
        self.work_ln.setText(self.data[0][6])
        

    def save_to_database(self):
        self.value=[]
        self.value.append(self.id_ln.text())
        self.value.append(self.name_ln.text())
        self.value.append(self.pw_ln.text())
        self.value.append(self.tel_ln.text())
        self.value.append(self.mail_ln.text())
        self.value.append(self.dep_ln.text())
        self.value.append(self.work_ln.text())
        print(self.value)
        sql0="delete from sys_admin where aId=%s"
        LinkMysql().commit_sql(sql0,self.user_id)
        sql = "INSERT INTO sys_admin values (%s,%s,%s,%s,%s,%s,%s)"
        if LinkMysql().commit_sql(sql,self.value):
           QMessageBox.information(self,"温馨提示", "修改成功",QMessageBox.Ok)
           print('You succeed')
        else:
           QMessageBox.warning(self, '温馨提示','有错误发生,请重试',QMessageBox.Retry)
           print('Something wrong')
        self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    user_id=1000
    win = sys_admin_modify_panel(user_id)
    win.show()
    sys.exit(app.exec_())
