

import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.sys_admin_add_ui import sys_admin_add_ui
from link_to_database import LinkMysql

class sys_admin_add_panel(QWidget, sys_admin_add_ui):
    def __init__(self):
        super(sys_admin_add_panel,self).__init__()
        self.setupUi(self)
    def add_to_database(self):
        self.value=[]
        self.value.append(self.id_ln.text())
        self.value.append(self.name_ln.text())
        self.value.append(self.pw_ln.text())
        self.value.append(self.tel_ln.text())
        self.value.append(self.mail_ln.text())
        self.value.append(self.dep_ln.text())
        self.value.append(self.work_ln.text())
        if not self.id_ln.text():
            QMessageBox.warning(self, '温馨提示','请输入管理员id',QMessageBox.Retry)
            print('Something wrong')
        else:
            id=int(self.id_ln.text())
            print(self.value)
            sql = "INSERT INTO sys_admin values (%s,%s,%s,%s,%s,%s,%s)"
            if  id<1000:
                  QMessageBox.warning(self, '温馨提示','管理员id要大于1000',QMessageBox.Retry)
                  print('Something wrong')
            elif LinkMysql().commit_sql(sql,self.value):
                  QMessageBox.information(self,"温馨提示", "添加成功",QMessageBox.Ok)
                  print('You succeed')
            else:
                 QMessageBox.warning(self, '温馨提示','有错误发生,请重试',QMessageBox.Retry)
                 print('Something wrong')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = sys_admin_add_panel()
    win.show()
    sys.exit(app.exec_())
