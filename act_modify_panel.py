# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.Qt import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.act_modify_ui import act_modify_ui
from link_to_database import LinkMysql


class act_modify_panel(QWidget, act_modify_ui):
    def __init__(self,user_id):
        super(act_modify_panel,self).__init__()
        self.setupUi(self)
        self.user_id=user_id
        sql='select * from activity where acId=%s'
        self.data=LinkMysql().select_sql(sql,user_id)
        print(self.data)
    
        self.time.setDate(QDate(self.data[0][2]))
        self.title_ln.setText(self.data[0][1])
        self.con_ln.setText(self.data[0][3])

    def save_to_database(self):
        dateTime= self.time.date().toString('yyyy-MM-dd')
        print(dateTime)

        self.value=[]
        self.value.append(self.title_ln.text())
        self.value.append(dateTime)
        self.value.append(self.con_ln.toPlainText())
        self.value.append(1)
       
        print(self.value)
        sql0="delete from activity where acId=%s"
        LinkMysql().commit_sql(sql0,self.user_id)
        sql = "INSERT INTO activity(acTitle,acTime,acContent,acbuilder) values (%s,%s,%s,%s)"
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
    win = act_modify_panel(user_id)
    win.show()
    sys.exit(app.exec_())
