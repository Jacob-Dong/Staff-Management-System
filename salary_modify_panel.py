# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.salary_modify_ui import salary_modify_ui
from link_to_database import LinkMysql


class salary_modify_panel(QWidget, salary_modify_ui):
    def __init__(self,user_id):
        super(salary_modify_panel,self).__init__()
        self.setupUi(self)
        self.user_id=user_id
        sql='select * from salary where staId=%s'
        self.data=LinkMysql().select_sql(sql,user_id)
        print(self.data)

        times=self.data[0][4]
        origin=self.data[0][2]
        award=self.data[0][3]
        realSalary=origin+award-(times*100)
        self.sa_id.setText(str(self.data[0][0]))
        self.sa_name.setText(self.data[0][1])
        self.sa_or.setText(str(self.data[0][2]))
        self.sa_aw.setText(str(self.data[0][3]))
        self.sa_times.setText(str(self.data[0][4]))
        self.real_sa.setText(str(realSalary))

        self.real_sa.setReadOnly(True)
        

    def save_to_database(self):
        self.value=[]
        self.value.append(self.sa_id.text())
        self.value.append(self.sa_name.text())
        self.value.append(self.sa_or.text())
        self.value.append(self.sa_aw.text())
        self.value.append(self.sa_times.text())
       
        print(self.value)
        sql0="delete from salary where staId=%s"
        LinkMysql().commit_sql(sql0,self.user_id)
        sql = "INSERT INTO salary values (%s,%s,%s,%s,%s)"
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
    win = salary_modify_panel(user_id)
    win.show()
    sys.exit(app.exec_())
