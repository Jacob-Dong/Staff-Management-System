# -*- coding: utf-8 -*-


import sys
import qdarkstyle
from PyQt5.QtGui import QIcon

from PyQt5 import QtCore, QtGui, QtWidgets


class mon_add_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(531, 514)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 110, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(310, 110, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 91, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(310, 180, 91, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 101, 31))
        self.label_5.setObjectName("label_5")
        self.mon_name = QtWidgets.QLineEdit(Form)
        self.mon_name.setGeometry(QtCore.QRect(100, 110, 113, 31))
        self.mon_name.setObjectName("mon_name")
        self.mon_date = QtWidgets.QLineEdit(Form)
        self.mon_date.setGeometry(QtCore.QRect(100, 180, 113, 31))
        self.mon_date.setObjectName("mon_date")
        self.mon_re = QtWidgets.QTextEdit(Form)
        self.mon_re.setGeometry(QtCore.QRect(16, 286, 281, 221))
        self.mon_re.setObjectName("mon_re")
        self.mon_id = QtWidgets.QLineEdit(Form)
        self.mon_id.setGeometry(QtCore.QRect(390, 110, 113, 31))
        self.mon_id.setObjectName("mon_id")
        self.mon_awa = QtWidgets.QLineEdit(Form)
        self.mon_awa.setGeometry(QtCore.QRect(390, 180, 113, 31))
        self.mon_awa.setObjectName("mon_awa")
        self.save = QtWidgets.QPushButton(Form)
        self.save.setGeometry(QtCore.QRect(390, 450, 112, 34))
        self.save.setObjectName("save")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(190, 30, 171, 41))
        self.label_6.setObjectName("label_6")
       
        self.retranslateUi(Form)
        self.save.clicked.connect(Form.add_to_database)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "添加优秀员工"))
        self.label.setText(_translate("Form", "员工姓名"))
        self.label_2.setText(_translate("Form", "员工工号"))
        self.label_3.setText(_translate("Form", "成就日期"))
        self.label_4.setText(_translate("Form", "奖励金额"))
        self.label_5.setText(_translate("Form", "奖励备注"))
        self.save.setText(_translate("Form", "保存"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">添加优秀员工</span></p></body></html>"))


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("./source/staff.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    Form = QtWidgets.QWidget()
    ui = mon_add_ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
