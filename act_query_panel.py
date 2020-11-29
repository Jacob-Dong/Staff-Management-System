# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.Qt import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.act_query_ui import act_query_ui
from link_to_database import LinkMysql


class act_query_panel(QWidget, act_query_ui):
    def __init__(self,user_id):
        super(act_query_panel,self).__init__()
        self.setupUi(self)
        
        sql='select * from activity where acId=%s'
        self.data=LinkMysql().select_sql(sql,user_id)
        print(self.data)
    
        self.time.setDate(QDate(self.data[0][2]))
        self.title_ln.setText(self.data[0][1])
        self.con_ln.setText(self.data[0][3])
       
        self.time.setReadOnly(True)
        self.title_ln.setReadOnly(True)
        self.con_ln.setReadOnly(True)
    
       
    def fade(self):
        self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    user_id=4
    win = act_query_panel(user_id)
    win.show()
    sys.exit(app.exec_())
