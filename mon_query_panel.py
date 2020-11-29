# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.mon_query_ui import mon_query_ui
from link_to_database import LinkMysql


class mon_query_panel(QWidget, mon_query_ui):
    def __init__(self,user_id):
        super(mon_query_panel,self).__init__()
        self.setupUi(self)
        
        sql='select * from monthrecord where staId=%s'
        self.data=LinkMysql().select_sql(sql,user_id)

        

        self.mon_id.setText(str(self.data[0][0]))
        self.mon_name.setText(self.data[0][1])
        self.mon_date.setText(str(self.data[0][2]))
        self.mon_awa.setText(str(self.data[0][3]))
        self.mon_re.setText(self.data[0][4])
       
        
        self.mon_id.setReadOnly(True)
        self.mon_name.setReadOnly(True)
        self.mon_date.setReadOnly(True)
        self.mon_awa.setReadOnly(True)
        self.mon_re.setReadOnly(True)
        
       
    def fade(self):
        self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    user_id=1
    win = mon_query_panel(user_id)
    win.show()
    sys.exit(app.exec_())
