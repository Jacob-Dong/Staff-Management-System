# -*- coding: utf-8 -*-


import sys
import qdarkstyle
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets


class staff_query_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(728, 649)
        self.mail = QtWidgets.QLabel(Form)
        self.mail.setGeometry(QtCore.QRect(510, 313, 61, 31))
        self.mail.setObjectName("mail")
        self.t_dep = QtWidgets.QTextEdit(Form)
        self.t_dep.setGeometry(QtCore.QRect(590, 193, 107, 31))
        self.t_dep.setObjectName("t_dep")

        self.t_tel = QtWidgets.QTextEdit(Form)
        self.t_tel.setGeometry(QtCore.QRect(590, 253, 135,31))
        self.t_tel.setObjectName("t_tel")

        self.dep = QtWidgets.QLabel(Form)
        self.dep.setGeometry(QtCore.QRect(510, 193, 51, 31))
        self.dep.setObjectName("dep")

        self.t_skills = QtWidgets.QTextEdit(Form)
        self.t_skills.setGeometry(QtCore.QRect(30, 463, 421, 171))
        self.t_skills.setObjectName("t_skills")

        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(230, 20, 281, 31))
        self.title.setObjectName("title")

        self.salary = QtWidgets.QLabel(Form)
        self.salary.setGeometry(QtCore.QRect(270, 313, 51, 31))
        self.salary.setObjectName("salary")

        self.t_duty = QtWidgets.QTextEdit(Form)
        self.t_duty.setGeometry(QtCore.QRect(350, 253, 107, 31))
        self.t_duty.setObjectName("t_duty")

        self.t_nation = QtWidgets.QTextEdit(Form)
        self.t_nation.setGeometry(QtCore.QRect(350, 133, 107, 31))
        self.t_nation.setObjectName("t_nation")

        self.query = QtWidgets.QPushButton(Form)
        self.query.setGeometry(QtCore.QRect(540, 583, 171, 41))
        self.query.setObjectName("query")
        
        

        self.bir = QtWidgets.QLabel(Form)
        self.bir.setGeometry(QtCore.QRect(30, 133, 81, 31))
        self.bir.setObjectName("bir")

        self.entry = QtWidgets.QLabel(Form)
        self.entry.setGeometry(QtCore.QRect(30, 373, 81, 31))
        self.entry.setObjectName("entry")

        self.rank = QtWidgets.QLabel(Form)
        self.rank.setGeometry(QtCore.QRect(30, 313, 51, 31))
        self.rank.setObjectName("rank")

        self.t_entry = QtWidgets.QTextEdit(Form)
        self.t_entry.setGeometry(QtCore.QRect(110, 373, 121, 31))
        self.t_entry.setObjectName("t_entry")

        self.t_sex = QtWidgets.QTextEdit(Form)
        self.t_sex.setGeometry(QtCore.QRect(590, 73, 107, 31))
        self.t_sex.setObjectName("t_sex")

        self.t_bir = QtWidgets.QTextEdit(Form)
        self.t_bir.setGeometry(QtCore.QRect(110, 133, 121, 31))
        self.t_bir.setObjectName("t_bir")

        self.skills = QtWidgets.QLabel(Form)
        self.skills.setGeometry(QtCore.QRect(30, 423, 141, 31))
        self.skills.setObjectName("skills")

        self.nation = QtWidgets.QLabel(Form)
        self.nation.setGeometry(QtCore.QRect(270, 133, 51, 31))
        self.nation.setObjectName("nation")

        self.t_marriage = QtWidgets.QTextEdit(Form)
        self.t_marriage.setGeometry(QtCore.QRect(350, 193, 107, 31))
        self.t_marriage.setObjectName("t_marriage")

        self.marriage = QtWidgets.QLabel(Form)
        self.marriage.setGeometry(QtCore.QRect(270, 193, 81, 31))
        self.marriage.setObjectName("marriage")

        self.depid = QtWidgets.QLabel(Form)
        self.depid.setGeometry(QtCore.QRect(30, 253, 71, 31))
        self.depid.setObjectName("depid")

        self.id = QtWidgets.QLabel(Form)
        self.id.setGeometry(QtCore.QRect(30, 73, 71, 31))
        self.id.setObjectName("id")

        self.t_name = QtWidgets.QTextEdit(Form)
        self.t_name.setGeometry(QtCore.QRect(350, 73, 107, 31))
        self.t_name.setObjectName("t_name")

        self.edu = QtWidgets.QLabel(Form)
        self.edu.setGeometry(QtCore.QRect(30, 193, 61, 31))
        self.edu.setObjectName("edu")

        self.t_depid = QtWidgets.QTextEdit(Form)
        self.t_depid.setGeometry(QtCore.QRect(110, 253, 121, 31))
        self.t_depid.setObjectName("t_depid")

        self.t_salary = QtWidgets.QTextEdit(Form)
        self.t_salary.setGeometry(QtCore.QRect(350, 313, 107, 31))
        self.t_salary.setObjectName("t_salary")

        self.politics = QtWidgets.QLabel(Form)
        self.politics.setGeometry(QtCore.QRect(510, 133, 81, 31))
        self.politics.setObjectName("politics")

        self.tel = QtWidgets.QLabel(Form)
        self.tel.setGeometry(QtCore.QRect(510, 253, 61, 31))
        self.tel.setObjectName("tel")

        self.name = QtWidgets.QLabel(Form)
        self.name.setGeometry(QtCore.QRect(270, 73, 61, 31))
        self.name.setObjectName("name")

        self.duty = QtWidgets.QLabel(Form)
        self.duty.setGeometry(QtCore.QRect(270, 253, 61, 31))
        self.duty.setObjectName("duty")

        self.t_id = QtWidgets.QTextEdit(Form)
        self.t_id.setGeometry(QtCore.QRect(110, 73, 121, 31))
        self.t_id.setObjectName("t_id")

        self.sex = QtWidgets.QLabel(Form)
        self.sex.setGeometry(QtCore.QRect(510, 73, 51, 31))
        self.sex.setObjectName("sex")

        self.t_edu = QtWidgets.QTextEdit(Form)
        self.t_edu.setGeometry(QtCore.QRect(110, 193, 121, 31))
        self.t_edu.setObjectName("t_edu")

        self.t_mail = QtWidgets.QTextEdit(Form)
        self.t_mail.setGeometry(QtCore.QRect(590, 313, 135, 31))
        self.t_mail.setObjectName("t_mail")

        self.t_politics = QtWidgets.QTextEdit(Form)
        self.t_politics.setGeometry(QtCore.QRect(590, 133, 107, 31))
        self.t_politics.setObjectName("t_politics")

        self.t_rank = QtWidgets.QTextEdit(Form)
        self.t_rank.setGeometry(QtCore.QRect(110, 313, 121, 31))
        self.t_rank.setObjectName("t_rank")

        self.retranslateUi(Form)
        self.query.clicked.connect(Form.fade)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "查看员工信息"))
        self.mail.setText(_translate("Form", "邮箱"))
        self.dep.setText(_translate("Form", "部门"))
        self.title.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">查看员工信息</span></p></body></html>"))
        self.salary.setText(_translate("Form", "工资"))
        self.query.setText(_translate("Form", "OK"))
        self.bir.setText(_translate("Form", "出生日期"))
        self.entry.setText(_translate("Form", "入职日期"))
        self.rank.setText(_translate("Form", "级别"))
        self.skills.setText(_translate("Form", "工作经验及技能"))
        self.nation.setText(_translate("Form", "民族"))
        self.marriage.setText(_translate("Form", "婚姻状况"))
        self.depid.setText(_translate("Form", "部门ID"))
        self.id.setText(_translate("Form", "员工Id"))
        self.edu.setText(_translate("Form", "学历"))
        self.politics.setText(_translate("Form", "政治面貌"))
        self.tel.setText(_translate("Form", "手机"))
        self.name.setText(_translate("Form", "姓名"))
        self.duty.setText(_translate("Form", "职务"))
        self.sex.setText(_translate("Form", "性别"))



if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("./source/staff.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    Form = QtWidgets.QWidget()
    ui = staff_query_ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
