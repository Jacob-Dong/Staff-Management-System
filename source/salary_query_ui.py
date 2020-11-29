# -*- coding: utf-8 -*-


import sys
import qdarkstyle
from PyQt5.QtGui import QIcon

from PyQt5 import QtCore, QtGui, QtWidgets


class salary_query_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 504)
        self.sa_name = QtWidgets.QLineEdit(Form)
        self.sa_name.setGeometry(QtCore.QRect(70, 110, 113, 31))
        self.sa_name.setObjectName("sa_name")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 51, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 260, 51, 31))
        self.label_5.setObjectName("label_5")
        self.sa_or = QtWidgets.QLineEdit(Form)
        self.sa_or.setGeometry(QtCore.QRect(70, 210, 113, 31))
        self.sa_or.setObjectName("sa_or")
        self.OK = QtWidgets.QPushButton(Form)
        self.OK.setGeometry(QtCore.QRect(270, 440, 112, 34))
        self.OK.setObjectName("OK")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 151, 41))
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 110, 51, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 51, 31))
        self.label_2.setObjectName("label_2")
        self.lt = QtWidgets.QLabel(Form)
        self.lt.setGeometry(QtCore.QRect(20, 310, 81, 31))
        self.lt.setObjectName("lt")
        self.sa_id = QtWidgets.QLineEdit(Form)
        self.sa_id.setGeometry(QtCore.QRect(70, 160, 113, 31))
        self.sa_id.setObjectName("sa_id")
        self.sa_aw = QtWidgets.QLineEdit(Form)
        self.sa_aw.setGeometry(QtCore.QRect(70, 260, 113, 31))
        self.sa_aw.setObjectName("sa_aw")
        self.sa_times = QtWidgets.QLineEdit(Form)
        self.sa_times.setGeometry(QtCore.QRect(100, 310, 113, 31))
        self.sa_times.setObjectName("sa_times")
        self.real_sa = QtWidgets.QLineEdit(Form)
        self.real_sa.setGeometry(QtCore.QRect(100, 360, 113, 31))
        self.real_sa.setObjectName("real_sa")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 360, 81, 31))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        self.OK.clicked.connect(Form.fade)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "工资查看"))
        self.label_4.setText(_translate("Form", "底薪"))
        self.label_5.setText(_translate("Form", "奖金"))
        self.OK.setText(_translate("Form", "OK"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">员工工资</span></p></body></html>"))
        self.label.setText(_translate("Form", "姓名"))
        self.label_2.setText(_translate("Form", "工号"))
        self.lt.setText(_translate("Form", "缺勤次数"))
        self.label_7.setText(_translate("Form", "实得工资"))

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("./source/staff.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    Form = QtWidgets.QWidget()
    ui = salary_query_ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())