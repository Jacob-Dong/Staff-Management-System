# -*- coding: utf-8 -*-


import sys
import qdarkstyle
from PyQt5.QtGui import QIcon

from PyQt5 import QtCore, QtGui, QtWidgets


class dep_modify_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(574, 494)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 100, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(300, 100, 91, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 81, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(300, 160, 101, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 101, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 91, 31))
        self.label_6.setObjectName("label_6")
        self.did_ln = QtWidgets.QLineEdit(Form)
        self.did_ln.setGeometry(QtCore.QRect(90, 100, 113, 31))
        self.did_ln.setObjectName("did_ln")
        self.ddir_ln = QtWidgets.QLineEdit(Form)
        self.ddir_ln.setGeometry(QtCore.QRect(90, 160, 113, 31))
        self.ddir_ln.setObjectName("ddir_ln")
        self.ddir_mail = QtWidgets.QLineEdit(Form)
        self.ddir_mail.setGeometry(QtCore.QRect(120, 220, 141, 31))
        self.ddir_mail.setObjectName("ddir_mail")
        self.ddirname_ln = QtWidgets.QLineEdit(Form)
        self.ddirname_ln.setGeometry(QtCore.QRect(410, 100, 113, 31))
        self.ddirname_ln.setObjectName("ddirname_ln")
        self.ddir_tel = QtWidgets.QLineEdit(Form)
        self.ddir_tel.setGeometry(QtCore.QRect(410, 160, 141, 31))
        self.ddir_tel.setObjectName("ddir_tel")
        self.dintr_ln = QtWidgets.QTextEdit(Form)
        self.dintr_ln.setGeometry(QtCore.QRect(20, 300, 341, 181))
        self.dintr_ln.setObjectName("dintr_ln")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(220, 17, 151, 41))
        self.label_7.setObjectName("label_7")
        self.modify = QtWidgets.QPushButton(Form)
        self.modify.setGeometry(QtCore.QRect(430, 410, 121, 41))
        self.modify.setObjectName("modify")

        self.retranslateUi(Form)
        self.modify.clicked.connect(Form.save_to_database)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "修改部门信息"))
        self.label.setText(_translate("Form", "部门id"))
        self.label_2.setText(_translate("Form", "部门名字"))
        self.label_3.setText(_translate("Form", "负责人"))
        self.label_4.setText(_translate("Form", "负责人电话"))
        self.label_5.setText(_translate("Form", "负责人邮箱"))
        self.label_6.setText(_translate("Form", "部门简介"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">修改部门信息</span></p></body></html>"))
        self.modify.setText(_translate("Form", "保存更改"))

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("./source/staff.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    Form = QtWidgets.QWidget()
    ui = dep_modify_ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
