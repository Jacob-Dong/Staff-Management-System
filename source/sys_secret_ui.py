# -*- coding: utf-8 -*-


import sys
import qdarkstyle
from PyQt5.QtGui import QIcon

from PyQt5 import QtCore, QtGui, QtWidgets


class sys_secret_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(314, 300)
        self.osec_ln = QtWidgets.QLineEdit(Form)
        self.osec_ln.setGeometry(QtCore.QRect(120, 103, 113, 25))
        self.osec_ln.setObjectName("osec_ln")
        self.id_ln = QtWidgets.QLineEdit(Form)
        self.id_ln.setGeometry(QtCore.QRect(120, 43, 113, 25))
        self.id_ln.setObjectName("id_ln")
        self.nsec_ln = QtWidgets.QLineEdit(Form)
        self.nsec_ln.setGeometry(QtCore.QRect(120, 153, 113, 25))
        self.nsec_ln.setObjectName("nsec_ln")
        self.nsec = QtWidgets.QLabel(Form)
        self.nsec.setGeometry(QtCore.QRect(20, 153, 81, 31))
        self.nsec.setObjectName("nsec")
        self.name = QtWidgets.QLabel(Form)
        self.name.setGeometry(QtCore.QRect(30, 40, 61, 31))
        self.name.setObjectName("name")
        self.admit = QtWidgets.QPushButton(Form)
        self.admit.setGeometry(QtCore.QRect(190, 240, 112, 34))
        self.admit.setObjectName("admit")
        self.osec = QtWidgets.QLabel(Form)
        self.osec.setGeometry(QtCore.QRect(20, 100, 71, 31))
        self.osec.setObjectName("osec")

        self.admit.clicked.connect(Form.save_to_database)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "更改员工密码"))
        self.nsec.setText(_translate("Form", "新密码"))
        self.name.setText(_translate("Form", "工号"))
        self.admit.setText(_translate("Form", "确认修改"))
        self.osec.setText(_translate("Form", "原密码"))

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("./source/staff.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    Form = QtWidgets.QWidget()
    ui = sys_secret_ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
