

import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.check_add_ui import check_add_ui
from link_to_database import LinkMysql

class check_add_panel(QWidget, check_add_ui):
    def __init__(self):
        super(check_add_panel,self).__init__()
        self.setupUi(self)
    def add_to_database(self):
        da=self.ch_date.date().toString('yyyy-MM-dd')
        self.value=[]
        self.value.append(self.ch_id.text())
        self.value.append(self.ch_name.text())
        self.value.append(self.ch_dep.text())
        self.value.append(self.ch_work.text())
        self.value.append(da)
        
        
        
        print(self.value)
        sql = "INSERT INTO checking_in values (%s,%s,%s,%s,%s)"
        
        if LinkMysql().commit_sql(sql,self.value):
                  QMessageBox.information(self,"温馨提示", "添加成功",QMessageBox.Ok)
                  print('You succeed')
        else:
                 QMessageBox.warning(self, '温馨提示','有错误发生',QMessageBox.Retry)
                 print('Something wrong')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    win =check_add_panel()
    win.show()
    sys.exit(app.exec_())
