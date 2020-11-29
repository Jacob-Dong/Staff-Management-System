

import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.mon_add_ui import mon_add_ui
from link_to_database import LinkMysql

class mon_add_panel(QWidget, mon_add_ui):
    def __init__(self):
        super(mon_add_panel,self).__init__()
        self.setupUi(self)
    def add_to_database(self):
        self.value=[]
        self.value.append(self.mon_id.text())
        self.value.append(self.mon_name.text())
        self.value.append(self.mon_date.text())
        self.value.append(self.mon_awa.text())
        self.value.append(self.mon_re.toPlainText())
       
        
        print(self.value)
        sql = "INSERT INTO monthrecord values (%s,%s,%s,%s,%s)"
        
        if LinkMysql().commit_sql(sql,self.value):
                  QMessageBox.information(self,"温馨提示", "添加成功",QMessageBox.Ok)
                  print('You succeed')
        else:
                 QMessageBox.warning(self, '温馨提示','有错误发生',QMessageBox.Retry)
                 print('Something wrong')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    win =mon_add_panel()
    win.show()
    sys.exit(app.exec_())
