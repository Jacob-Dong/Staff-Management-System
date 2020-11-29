# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


from source.main_window_ui import Ui_MainWindow

from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import qdarkstyle

from staff_console import staff_console
from staff_add_panel import staff_add_panel
from source.staff_add_ui import staff_add_ui
from login_panel import login_panel
from link_to_database import LinkMysql
from change_secret_panel import change_secret_panel
from sys_admin_console import sys_admin_console
from dep_console import dep_console
from act_console import act_console
from mon_console import mon_console
from check_console import check_console
from salary_console import salary_console
from staff_bad_console import staff_bad_console
from staff_good_console import staff_good_console
from sys_secret_console import sys_secret_console

from act_staff_console import act_staff_console
from mon_staff_console import mon_staff_console
from check_staff_console import check_staff_console
from dep_staff_console import dep_staff_console
from salary_staff_console import salary_staff_console
from staff_go_console import staff_go_console
from staff_b_console import staff_b_console
from staff_sta_console import staff_sta_console







class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.sta_secret.triggered.connect(self.staff_secret)
        self.sys.triggered.connect(self.sys_admin)

       #部门管理
        self.de_query.triggered.connect(self.dep_con)
        self.de_add.triggered.connect(self.dep_con)
        self.de_up.triggered.connect(self.dep_con)
        self.de_de.triggered.connect(self.dep_con)

        #活动管理
        self.ac_query.triggered.connect(self.act_con)
        self.ac_de.triggered.connect(self.act_con)
        self.ac_add.triggered.connect(self.act_con)
        self.ac_up.triggered.connect(self.act_con)

        #月度优秀员工管理
        self.mon_query.triggered.connect(self.mon_con)
        self.mon_add.triggered.connect(self.mon_con)
        self.mon_up.triggered.connect(self.mon_con)
        self.mon_de.triggered.connect(self.mon_con)

        #缺勤管理
        self.che_query.triggered.connect(self.check_con)
        self.che_add.triggered.connect(self.check_con)
        self.che_up.triggered.connect(self.check_con)
        self.che_de.triggered.connect(self.check_con)

        #工资管理
        self.sa_query.triggered.connect(self.salary_con)
        self.sa_up.triggered.connect(self.salary_con)

        #优秀员工
        self.sta_good.triggered.connect(self.staff_good_con)
        #不佳员工
        self.sta_bad.triggered.connect(self.staff_bad_con)
        #员工上方板块
        self.sta_query.triggered.connect(self.staff_query)
        self.sta_de.triggered.connect(self.staff_query)
        self.sta_up.triggered.connect(self.staff_query)
        self.staff_add.triggered.connect(self.staff_query)

         #员工中间板块
        self.sta_t_query.clicked.connect(self.staff_query)
        self.sta_t_add.clicked.connect(self.staff_query)
        self.sta_t_up.clicked.connect(self.staff_query)
        self.sta_t_delete.clicked.connect(self.staff_query)

           #部门
        self.de_t_add.clicked.connect(self.dep_con)
        self.de_t_up.clicked.connect(self.dep_con)
        self.de_t_de.clicked.connect(self.dep_con)
        self.de_t_query.clicked.connect(self.dep_con)

           #活动
        self.ac_t_add.clicked.connect(self.act_con)
        self.ac_t_de.clicked.connect(self.act_con)
        self.ac_t_query.clicked.connect(self.act_con)


           #缺勤
        self.che_t_add.clicked.connect(self.check_con)
        self.che_t_de.clicked.connect(self.check_con)
        self.che_t_up.clicked.connect(self.check_con)
        self.check_t_query.clicked.connect(self.check_con)

           #工资
        self.sa_t_up.clicked.connect(self.salary_con)
        self.sa_t_auery.clicked.connect(self.salary_con)

           #月度成就
        self.mon_t_add.clicked.connect(self.mon_con)
        self.mon_t_up.clicked.connect(self.mon_con)
        self.mon_t_de.clicked.connect(self.mon_con)
        self.mon_t_query.clicked.connect(self.mon_con)
        
       
    #获得用户id
    def get_user(self,user_id):
        self.user_id=int(user_id)
    def sys_admin(self):
        if self.user_id<1000:
            QMessageBox.warning(self, '温馨提示','对不起,您无权使用',QMessageBox.Ok)
        else:
            self.sys_a = sys_admin_console()
            self.sys_a.show()
            self.sys_a.exec_()
            print('You succeed')
    #用户改变密码
    def staff_secret(self):
        if self.user_id>=1000:
            self.sys_s = sys_secret_console()
            self.sys_s.show()
            self.sys_s.exec_()
            print('You succeed')
            
        else:
            self.ch= change_secret_panel(self.user_id)
            self.ch.show() 

    #部门控制板
    def dep_con(self):
       if self.user_id<1000:
         self.dep = dep_staff_console()
         self.dep.show()
         self.dep.exec_()
         print('You succeed')
       else:
         self.dep = dep_console()
         self.dep.show()
         self.dep.exec_()
         print('You succeed')
    #活动管理
    def act_con(self):
        if self.user_id<1000:
            self.ac=act_staff_console()
            self.ac.show()
            self.ac.exec_()
            print('You succeed')
        else:
          self.ac = act_console()
          self.ac.show()
          self.ac.exec_()
          print('You succeed')

    #月度优秀员工管理
    def  mon_con(self):
        if self.user_id<1000:
            self.mo = mon_staff_console()
            self.mo.show()
            self.mo.exec_()
            print('You succeed')
        else:
            self.mo = mon_console()
            self.mo.show()
            self.mo.exec_()
            print('You succeed')

    #缺勤管理
    def  check_con(self):
        if self.user_id<1000:
            self.ch = check_staff_console()
            self.ch.show()
            self.ch.exec_()
            print('You succeed')

        else:
            self.ch = check_console()
            self.ch.show()
            self.ch.exec_()
            print('You succeed')

    #工资控制板
    def salary_con(self):
       if self.user_id<1000:
          self.sa =salary_staff_console()
          self.sa.show()
          self.sa.exec_()
          print('You succeed')
       else:
          self.sa = salary_console()
          self.sa.show()
          self.sa.exec_()
          print('You succeed') 

    #优秀员工
    #staff_good_con
    def staff_good_con(self):
        if self.user_id<1000:
           self.sgood = staff_go_console()
           self.sgood.show()
           self.sgood.exec_()
           print('You succeed')
        else:
           self.sgood = staff_good_console()
           self.sgood.show()
           self.sgood.exec_()
           print('You succeed')
    #不佳员工
    def staff_bad_con(self):
        if self.user_id<1000:
           self.sbad = staff_b_console()
           self.sbad.show()
           self.sbad.exec_()
           print('You succeed')
        else:
           self.sbad = staff_bad_console()
           self.sbad.show()
           self.sbad.exec_()
           print('You succeed')
    

    def staff_query(self):
        if self.user_id<1000:
           self.st_q = staff_sta_console()
           self.st_q.show()
           self.st_q.exec_()
           print('You succeed')
        else:
           self.st_q = staff_console()
           self.st_q.show()
           self.st_q.exec_()
           print('You succeed')

    
    
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./source/staff.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    landing=login_panel()
    myWin = MyMainWindow()
    # 将窗口控件显示在屏幕上
    
    def show_joblog(ls):
    
        print(ls)
        #管理员登录
        if ls[2]:
            p=LinkMysql().select_admin(ls[0])
            pwd=(" ".join('%s' %id for id in p))
            print(pwd)
            if ls[1]==pwd:
                landing.hide()
                myWin.get_user(ls[0])
                myWin.show()
            else:    
                landing.show_error()

        #员工登录
        if ls[3]:
            p1=LinkMysql().select_staff(ls[0])
            pwd1=(" ".join('%s' %id for id in p1))
            print(pwd1)
            if ls[1]==pwd1:
                landing.hide()
                myWin.get_user(ls[0])
                myWin.show()
            else:    
                landing.show_error()


    landing.landing_sig.connect(show_joblog)  # 登陆按钮信号

    landing.show()
    sys.exit(app.exec_())


