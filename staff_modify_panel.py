# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import QApplication
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from source.staff_modify_ui import staff_modify_ui
from link_to_database import LinkMysql


class staff_modify_panel(QWidget, staff_modify_ui):
    def __init__(self,user_id):
        super(staff_modify_panel,self).__init__()
        self.setupUi(self)
        self.user_id=user_id
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
        

    def save_to_database(self):
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
        sql0="delete from staff where stId=%s"
        LinkMysql().commit_sql(sql0,self.user_id)
        sql = "INSERT INTO staff values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        if LinkMysql().commit_sql1(sql,self.value):
           QMessageBox.information(self,"温馨提示", "修改成功",QMessageBox.Ok)
           print('You succeed')
        else:
           QMessageBox.warning(self, '温馨提示','有错误发生,请重试',QMessageBox.Retry)
           print('Something wrong')
        self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    user_id=11
    win = staff_modify_panel(user_id)
    win.show()
    sys.exit(app.exec_())
