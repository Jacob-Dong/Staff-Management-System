# -*- coding: utf-8 -*-

import sys
import qdarkstyle
from PyQt5.QtGui import QIcon

from PyQt5 import QtCore, QtGui, QtWidgets


class sys_admin_query_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(476, 406)
        self.id = QtWidgets.QLabel(Form)
        self.id.setGeometry(QtCore.QRect(30, 100, 41, 31))
        self.id.setObjectName("id")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 51, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 220, 61, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 280, 51, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(270, 160, 51, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(270, 100, 61, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(270, 220, 51, 31))
        self.label_7.setObjectName("label_7")
        self.id_ln = QtWidgets.QLineEdit(Form)
        self.id_ln.setGeometry(QtCore.QRect(80, 100, 113, 31))
        self.id_ln.setObjectName("id_ln")
        self.pw_ln = QtWidgets.QLineEdit(Form)
        self.pw_ln.setGeometry(QtCore.QRect(80, 160, 113, 31))
        self.pw_ln.setObjectName("pw_ln")
        self.work_ln = QtWidgets.QLineEdit(Form)
        self.work_ln.setGeometry(QtCore.QRect(80, 220, 113, 31))
        self.work_ln.setObjectName("work_ln")
        self.tel_ln = QtWidgets.QLineEdit(Form)
        self.tel_ln.setGeometry(QtCore.QRect(80, 280, 125, 31))
        self.tel_ln.setObjectName("tel_ln")
        self.dep_ln = QtWidgets.QLineEdit(Form)
        self.dep_ln.setGeometry(QtCore.QRect(320, 160, 113, 31))
        self.dep_ln.setObjectName("dep_ln")
        self.mail_ln = QtWidgets.QLineEdit(Form)
        self.mail_ln.setGeometry(QtCore.QRect(320, 220, 125, 31))
        self.mail_ln.setObjectName("mail_ln")
        self.name_ln = QtWidgets.QLineEdit(Form)
        self.name_ln.setGeometry(QtCore.QRect(320, 100, 113, 31))
        self.name_ln.setObjectName("name_ln")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(150, 30, 161, 41))
        self.label_8.setObjectName("label_8")
        self.query = QtWidgets.QPushButton(Form)
        self.query.setGeometry(QtCore.QRect(330, 330, 112, 41))
        self.query.setObjectName("query")

        self.retranslateUi(Form)
        self.query.clicked.connect(Form.fade)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理员详细信息"))
        self.id.setText(_translate("Form", "ID"))
        self.label_2.setText(_translate("Form", "密码"))
        self.label_3.setText(_translate("Form", "职务"))
        self.label_4.setText(_translate("Form", "电话"))
        self.label_5.setText(_translate("Form", "部门"))
        self.label_6.setText(_translate("Form", "名字"))
        self.label_7.setText(_translate("Form", "邮箱"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">管理员信息</span></p></body></html>"))
        self.query.setText(_translate("Form", "OK"))


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("./source/staff.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    Form = QtWidgets.QWidget()
    ui = sys_admin_query_ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
