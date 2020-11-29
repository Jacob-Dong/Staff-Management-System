# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.Qt import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.check_query_ui import check_query_ui
from link_to_database import LinkMysql


class check_query_panel(QWidget, check_query_ui):
    def __init__(self,user_id):
        super(check_query_panel,self).__init__()
        self.setupUi(self)
        
        sql='select * from checking_in where staId=%s'
        self.data=LinkMysql().select_sql(sql,user_id)

        

        self.ch_id.setText(str(self.data[0][0]))
        self.ch_name.setText(self.data[0][1])
        self.ch_dep.setText(self.data[0][2])
        self.ch_work.setText(self.data[0][3])
        self.ch_date.setDate(QDate(self.data[0][4]))
        
        self.ch_id.setReadOnly(True)
        self.ch_name.setReadOnly(True)
        self.ch_dep.setReadOnly(True)
        self.ch_work.setReadOnly(True)
        self.ch_date.setReadOnly(True)
        
       
    def fade(self):
        self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    user_id=2
    win = check_query_panel(user_id)
    win.show()
    sys.exit(app.exec_())
