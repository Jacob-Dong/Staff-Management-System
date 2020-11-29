# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.dep_modify_ui import dep_modify_ui
from link_to_database import LinkMysql


class dep_modify_panel(QWidget, dep_modify_ui):
    def __init__(self,user_id):
        super(dep_modify_panel,self).__init__()
        self.setupUi(self)
        self.user_id=user_id
        sql='select * from department where dId=%s'
        self.data=LinkMysql().select_sql(sql,user_id)

        

        self.did_ln.setText(str(self.data[0][0]))
        self.ddirname_ln.setText(self.data[0][1])
        self.ddir_ln.setText(self.data[0][2])
        self.ddir_tel.setText(self.data[0][3])
        self.ddir_mail.setText(self.data[0][4])
        self.dintr_ln.setText(self.data[0][5])
        

    def save_to_database(self):
        self.value=[]
        self.value.append(self.did_ln.text())
        self.value.append(self.ddirname_ln.text())
        self.value.append(self.ddir_ln.text())
        self.value.append(self.ddir_tel.text())
        self.value.append(self.ddir_mail.text())
        self.value.append(self.dintr_ln.toPlainText())
       
        print(self.value)
        sql0="delete from department where dId=%s"
        LinkMysql().commit_sql(sql0,self.user_id)
        sql = "INSERT INTO department values (%s,%s,%s,%s,%s,%s)"
        if LinkMysql().commit_sql(sql,self.value):
           QMessageBox.information(self,"温馨提示", "修改成功",QMessageBox.Ok)
           print('You succeed')
        else:
           QMessageBox.warning(self, '温馨提示','请检查该部门无员工后再进行更改',QMessageBox.Retry)
           print('Something wrong')
        self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    user_id=1
    win = dep_modify_panel(user_id)
    win.show()
    sys.exit(app.exec_())
