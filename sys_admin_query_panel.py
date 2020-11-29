# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.sys_admin_query_ui import sys_admin_query_ui
from link_to_database import LinkMysql


class sys_admin_query_panel(QWidget, sys_admin_query_ui):
    def __init__(self,user_id):
        super(sys_admin_query_panel,self).__init__()
        self.setupUi(self)
        
        sql='select * from sys_admin where aId=%s'
        self.data=LinkMysql().select_sql(sql,user_id)

        self.id_ln.setText(str(self.data[0][0]))
        self.name_ln.setText(self.data[0][1])
        self.pw_ln.setText(self.data[0][2])
        self.tel_ln.setText(self.data[0][3])
        self.mail_ln.setText(str(self.data[0][4]))
        self.dep_ln.setText(self.data[0][5])
        self.work_ln.setText(self.data[0][6])
        
        self.id_ln.setReadOnly(True)
        self.name_ln.setReadOnly(True)
        self.pw_ln.setReadOnly(True)
        self.tel_ln.setReadOnly(True)
        self.mail_ln.setReadOnly(True)
        self.dep_ln.setReadOnly(True)
        self.work_ln.setReadOnly(True)
        
       
    def fade(self):
        self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    user_id=1005
    win = sys_admin_query_panel(user_id)
    win.show()
    sys.exit(app.exec_())
