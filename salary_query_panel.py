# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.salary_query_ui import salary_query_ui
from link_to_database import LinkMysql


class salary_query_panel(QWidget, salary_query_ui):
    def __init__(self,user_id):
        super(salary_query_panel,self).__init__()
        self.setupUi(self)
        
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
       
        
        self.sa_id.setReadOnly(True)
        self.sa_name.setReadOnly(True)
        self.sa_or.setReadOnly(True)
        self.sa_aw.setReadOnly(True)
        self.sa_times.setReadOnly(True)
        self.real_sa.setReadOnly(True)
        
       
    def fade(self):
        self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    user_id=1
    win = salary_query_panel(user_id)
    win.show()
    sys.exit(app.exec_())
