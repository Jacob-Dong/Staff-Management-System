# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.dep_query_ui import dep_query_ui
from link_to_database import LinkMysql


class dep_query_panel(QWidget, dep_query_ui):
    def __init__(self,user_id):
        super(dep_query_panel,self).__init__()
        self.setupUi(self)
        
        sql='select * from department where dId=%s'
        self.data=LinkMysql().select_sql(sql,user_id)

        

        self.did_ln.setText(str(self.data[0][0]))
        self.ddirname_ln.setText(self.data[0][1])
        self.ddir_ln.setText(self.data[0][2])
        self.ddir_tel.setText(self.data[0][3])
        self.ddir_mail.setText(self.data[0][4])
        self.dintr_ln.setText(self.data[0][5])
       
        
        self.did_ln.setReadOnly(True)
        self.ddirname_ln.setReadOnly(True)
        self.ddir_ln.setReadOnly(True)
        self.ddir_tel.setReadOnly(True)
        self.ddir_mail.setReadOnly(True)
        self.dintr_ln.setReadOnly(True)
        
       
    def fade(self):
        self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    user_id=1
    win = dep_query_panel(user_id)
    win.show()
    sys.exit(app.exec_())
