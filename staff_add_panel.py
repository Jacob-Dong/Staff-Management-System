import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.staff_add_ui import staff_add_ui
from link_to_database import LinkMysql


class staff_add_panel(QWidget, staff_add_ui):
    def __init__(self):
        super(staff_add_panel,self).__init__()
        self.setupUi(self)
    def add_to_database(self):
        self.value=[]
        self.value.append(self.t_id.toPlainText())
        self.value.append(self.t_rank.toPlainText())
        self.value.append(self.t_name.toPlainText())
        self.value.append(self.t_sex.toPlainText())
        self.value.append(self.t_marriage.toPlainText())
        self.value.append(self.t_bir.toPlainText())
        self.value.append(self.t_nation.toPlainText())
        self.value.append(self.t_tel.toPlainText())
        self.value.append(self.t_mail.toPlainText())
        self.value.append(self.t_edu.toPlainText())
        self.value.append(self.t_salary.toPlainText())
        self.value.append(self.t_entry.toPlainText())
        self.value.append(self.t_depid.toPlainText())
        self.value.append(self.t_duty.toPlainText())
        self.value.append(self.t_politics.toPlainText())
        self.value.append(self.t_skills.toPlainText())
        self.value.append(self.t_dep.toPlainText())
        print(self.value)
        sql = "INSERT INTO staff values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        if LinkMysql().commit_sql1(sql,self.value):
           QMessageBox.information(self,"温馨提示", "添加成功",QMessageBox.Ok)
           print('You succeed')
        else:
           QMessageBox.warning(self, '温馨提示','有错误发生,请重试',QMessageBox.Retry)
           print('Something wrong')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = staff_add_panel()
    win.show()
    sys.exit(app.exec_())
