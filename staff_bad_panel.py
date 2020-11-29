# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.staff_good_ui import staff_good_ui
from link_to_database import LinkMysql


class staff_bad_panel(QWidget, staff_good_ui):
    def __init__(self,user_id):
        super(staff_bad_panel,self).__init__()
        self.setupUi(self)
        
        sql='select * from staff_bad where staId=%s'
        self.data=LinkMysql().select_sql(sql,user_id)
        print(self.data)

       
        self.id.setText(str(self.data[0][0]))
        self.name.setText(self.data[0][1])
        self.dep.setText(self.data[0][2])
        self.work.setText(self.data[0][3])
        self.remark.setText(self.data[0][4])
       
        
        self.id.setReadOnly(True)
        self.name.setReadOnly(True)
        self.dep.setReadOnly(True)
        self.work.setReadOnly(True)
        self.remark.setReadOnly(True)
        
       
    def fade(self):
        self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    user_id=1
    win = staff_bad_panel(user_id)
    win.show()
    sys.exit(app.exec_())
