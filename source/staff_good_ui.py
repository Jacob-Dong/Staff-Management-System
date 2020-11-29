# -*- coding: utf-8 -*-


import sys
import qdarkstyle
from PyQt5.QtGui import QIcon

from PyQt5 import QtCore, QtGui, QtWidgets


class staff_good_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(533, 523)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(194, 20, 171, 41))
        self.label_6.setObjectName("label_6")
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setGeometry(QtCore.QRect(104, 100, 113, 31))
        self.name.setObjectName("name")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(24, 240, 101, 31))
        self.label_5.setObjectName("label_5")
        self.remark = QtWidgets.QTextEdit(Form)
        self.remark.setGeometry(QtCore.QRect(30, 280, 281, 221))
        self.remark.setObjectName("remark")
        self.OK = QtWidgets.QPushButton(Form)
        self.OK.setGeometry(QtCore.QRect(394, 440, 112, 34))
        self.OK.setObjectName("OK")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(24, 100, 81, 31))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(24, 170, 91, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(314, 170, 91, 31))
        self.label_4.setObjectName("label_4")
        self.id = QtWidgets.QLineEdit(Form)
        self.id.setGeometry(QtCore.QRect(394, 100, 113, 31))
        self.id.setObjectName("id")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(314, 100, 81, 31))
        self.label_2.setObjectName("label_2")
        self.work = QtWidgets.QLineEdit(Form)
        self.work.setGeometry(QtCore.QRect(394, 170, 113, 31))
        self.work.setObjectName("work")
        self.dep = QtWidgets.QLineEdit(Form)
        self.dep.setGeometry(QtCore.QRect(104, 170, 113, 31))
        self.dep.setObjectName("dep")

        self.retranslateUi(Form)
        self.OK.clicked.connect(Form.fade)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">详细信息</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "备注"))
        self.OK.setText(_translate("Form", "OK"))
        self.label.setText(_translate("Form", "员工姓名"))
        self.label_3.setText(_translate("Form", "员工部门"))
        self.label_4.setText(_translate("Form", "员工职务"))
        self.label_2.setText(_translate("Form", "员工工号"))

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("./source/staff.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    Form = QtWidgets.QWidget()
    ui = staff_good_ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
