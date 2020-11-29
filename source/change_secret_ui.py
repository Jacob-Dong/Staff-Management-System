# -*- coding: utf-8 -*-


import sys
import qdarkstyle
from PyQt5.QtGui import QIcon

from PyQt5 import QtCore, QtGui, QtWidgets


class change_secret_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 307)
        self.name = QtWidgets.QLabel(Form)
        self.name.setGeometry(QtCore.QRect(20, 87, 61, 31))
        self.name.setObjectName("name")
        self.nsec = QtWidgets.QLabel(Form)
        self.nsec.setGeometry(QtCore.QRect(20, 200, 81, 31))
        self.nsec.setObjectName("nsec")
        self.osec = QtWidgets.QLabel(Form)
        self.osec.setGeometry(QtCore.QRect(20, 147, 71, 31))
        self.osec.setObjectName("osec")
        self.id = QtWidgets.QLabel(Form)
        self.id.setGeometry(QtCore.QRect(220, 87, 61, 31))
        self.id.setObjectName("id")
        self.name_ln = QtWidgets.QLineEdit(Form)
        self.name_ln.setGeometry(QtCore.QRect(80, 90, 113, 25))
        self.name_ln.setObjectName("name_ln")
        self.osec_ln = QtWidgets.QLineEdit(Form)
        self.osec_ln.setGeometry(QtCore.QRect(80, 150, 113, 25))
        self.osec_ln.setObjectName("osec_ln")
        self.nsec_ln = QtWidgets.QLineEdit(Form)
        self.nsec_ln.setGeometry(QtCore.QRect(80, 200, 113, 25))
        self.nsec_ln.setObjectName("nsec_ln")
        self.id_ln = QtWidgets.QLineEdit(Form)
        self.id_ln.setGeometry(QtCore.QRect(260, 90, 113, 25))
        self.id_ln.setObjectName("id_ln")
        self.admit = QtWidgets.QPushButton(Form)
        self.admit.setGeometry(QtCore.QRect(280, 260, 112, 34))
        self.admit.setObjectName("admit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "员工修改密码"))
        self.name.setText(_translate("Form", "姓名"))
        self.nsec.setText(_translate("Form", "新密码"))
        self.osec.setText(_translate("Form", "原密码"))
        self.id.setText(_translate("Form", "工号"))
        self.admit.setText(_translate("Form", "确认修改"))


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("./source/staff.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    Form = QtWidgets.QWidget()
    ui = change_secret_ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
