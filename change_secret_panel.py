# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.change_secret_ui import change_secret_ui
from link_to_database import LinkMysql


class change_secret_panel(QWidget,change_secret_ui):
    def __init__(self,user_id):
        super(change_secret_panel,self).__init__()
        self.setupUi(self)
        self.user_id=user_id
        self.admit.clicked.connect(self.change)

        sql='select * from staff where stId=%s'
        sql1='select staPwd from sys_staff where staId=%s'
        self.data=LinkMysql().select_sql(sql,user_id)
        self.data1=LinkMysql().select_sql(sql1,user_id)
        self.pwd=(" ".join('%s' %id for id in self.data1))

        self.id_ln.setText(str(user_id))
        self.name_ln.setText(self.data[0][2])
        self.osec_ln.setText(self.pwd)

        self.id_ln.setReadOnly(True)
        self.name_ln.setReadOnly(True)
        self.osec_ln.setReadOnly(True)

    def change(self):
        new_sec=self.nsec_ln.text()
        sql='update sys_staff set staPwd=%s where staId=%s'
        ls=[]
        ls.append(new_sec)
        ls.append(self.user_id)
        if LinkMysql().commit_sql(sql,ls):
            QMessageBox.information(self,"温馨提示", "修改成功",QMessageBox.Ok)
            print('You succeed')
        else:
            QMessageBox.warning(self, '温馨提示','修改失败',QMessageBox.Retry)
            print('Something wrong')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    user_id=5
    win = change_secret_panel(user_id)
    win.show()
    sys.exit(app.exec_())
