

import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.dep_add_ui import dep_add_ui
from link_to_database import LinkMysql

class dep_add_panel(QWidget, dep_add_ui):
    def __init__(self):
        super(dep_add_panel,self).__init__()
        self.setupUi(self)
    def add_to_database(self):
        self.value=[]
        self.value.append(self.did_ln.text())
        self.value.append(self.ddirname_ln.text())
        self.value.append(self.ddir_ln.text())
        self.value.append(self.ddir_tel.text())
        self.value.append(self.ddir_mail.text())
        self.value.append(self.dintr_ln.toPlainText())
        
        
        print(self.value)
        sql = "INSERT INTO department values (%s,%s,%s,%s,%s,%s)"
        
        if LinkMysql().commit_sql(sql,self.value):
                  QMessageBox.information(self,"温馨提示", "添加成功",QMessageBox.Ok)
                  print('You succeed')
        else:
                 QMessageBox.warning(self, '温馨提示','请检查部门id是否重复',QMessageBox.Retry)
                 print('Something wrong')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    win =dep_add_panel()
    win.show()
    sys.exit(app.exec_())
