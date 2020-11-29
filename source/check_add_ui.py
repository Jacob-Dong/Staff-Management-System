# -*- coding: utf-8 -*-



import sys
import qdarkstyle
from PyQt5.QtGui import QIcon

from PyQt5 import QtCore, QtGui, QtWidgets


class check_add_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(377, 438)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 110, 51, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 51, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 310, 81, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 210, 51, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 260, 51, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(90, 30, 171, 41))
        self.label_6.setObjectName("label_6")
        self.ch_name = QtWidgets.QLineEdit(Form)
        self.ch_name.setGeometry(QtCore.QRect(80, 110, 113, 31))
        self.ch_name.setObjectName("ch_name")
        self.ch_id = QtWidgets.QLineEdit(Form)
        self.ch_id.setGeometry(QtCore.QRect(80, 160, 113, 31))
        self.ch_id.setObjectName("ch_id")
        self.ch_dep = QtWidgets.QLineEdit(Form)
        self.ch_dep.setGeometry(QtCore.QRect(80, 210, 113, 31))
        self.ch_dep.setObjectName("ch_dep")
        self.ch_work = QtWidgets.QLineEdit(Form)
        self.ch_work.setGeometry(QtCore.QRect(80, 260, 113, 31))
        self.ch_work.setObjectName("ch_work")
        self.ch_date = QtWidgets.QDateEdit(Form)
        self.ch_date.setGeometry(QtCore.QRect(120, 310, 141, 31))
        self.ch_date.setObjectName("ch_date")
        self.add = QtWidgets.QPushButton(Form)
        self.add.setGeometry(QtCore.QRect(250, 380, 112, 34))
        self.add.setObjectName("add")
        self.add.clicked.connect(Form.add_to_database)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "添加缺勤记录"))
        self.label.setText(_translate("Form", "姓名"))
        self.label_2.setText(_translate("Form", "工号"))
        self.label_3.setText(_translate("Form", "缺勤日期"))
        self.label_4.setText(_translate("Form", "部门"))
        self.label_5.setText(_translate("Form", "职务"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">添加缺勤记录</span></p></body></html>"))
        self.add.setText(_translate("Form", "添加"))


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("./source/staff.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    Form = QtWidgets.QWidget()
    ui = check_add_ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())