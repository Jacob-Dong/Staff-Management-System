# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.staff_query_ui import staff_query_ui
from link_to_database import LinkMysql


class staff_query_panel(QWidget, staff_query_ui):
    def __init__(self,user_id):
        super(staff_query_panel,self).__init__()
        self.setupUi(self)
        
        sql='select * from staff where stId=%s'
        self.data=LinkMysql().select_sql(sql,user_id)

        self.t_id.setText(str(self.data[0][0]))
        self.t_rank.setText(str(self.data[0][1]))
        self.t_name.setText(self.data[0][2])
        self.t_sex.setText(self.data[0][3])
        self.t_marriage.setText(self.data[0][4])
        self.t_bir.setText(str(self.data[0][5]))
        self.t_nation.setText(self.data[0][6])
        self.t_tel.setText(self.data[0][7])
        self.t_mail.setText(self.data[0][8])
        self.t_edu.setText(self.data[0][9])
        self.t_salary.setText(str(self.data[0][10]))
        self.t_entry.setText(str(self.data[0][11]))
        self.t_depid.setText(str(self.data[0][12]))
        self.t_duty.setText(self.data[0][13])
        self.t_politics.setText(self.data[0][14])
        self.t_skills.setText(self.data[0][15])
        self.t_dep.setText(self.data[0][16])
       
    def fade(self):
        self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    user_id=5
    win = staff_query_panel(user_id)
    win.show()
    sys.exit(app.exec_())
