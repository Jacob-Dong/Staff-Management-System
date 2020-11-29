# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.sys_secret_ui import sys_secret_ui
from link_to_database import LinkMysql


class sys_secret_panel(QWidget, sys_secret_ui):
    def __init__(self,user_id):
        super(sys_secret_panel,self).__init__()
        self.setupUi(self)
        self.user_id=user_id
        sql='select * from sys_view where staId=%s'
        print(self.user_id)
        self.data=LinkMysql().select_sql(sql,user_id)
        print(self.data)
        self.id_ln.setText(str(self.data[0][0]))
        self.osec_ln.setText(self.data[0][1])
        

    def save_to_database(self):
        self.value=[]
        self.value.append(self.nsec_ln.text())
        self.value.append(self.user_id)
        
       
        print(self.value)
        
        sql = "call  pupdate(%s,%s)"
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
    win = sys_secret_panel(user_id)
    win.show()
    sys.exit(app.exec_())
