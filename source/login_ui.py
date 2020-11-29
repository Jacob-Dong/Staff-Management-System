# -*- coding: utf-8 -*-



import sys
import qdarkstyle
from PyQt5.QtGui import QIcon


from PyQt5 import QtCore, QtGui, QtWidgets


class login_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(587, 219)
        self.login = QtWidgets.QPushButton(Form)
        self.login.setGeometry(QtCore.QRect(460, 170, 112, 34))
        self.login.setEnabled(False)
        self.login.setObjectName("login")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 17, 261, 31))
        self.label.setObjectName("label")
        self.name_la = QtWidgets.QLabel(Form)
        self.name_la.setGeometry(QtCore.QRect(10, 77, 81, 31))
        self.name_la.setObjectName("name_la")
        self.password_la = QtWidgets.QLabel(Form)
        self.password_la.setGeometry(QtCore.QRect(10, 130, 81, 31))
        self.password_la.setObjectName("password_la")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(90, 130, 131, 31))
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.account = QtWidgets.QLineEdit(Form)
        self.account.setGeometry(QtCore.QRect(90, 80, 131, 31))
        self.account.setObjectName("account")
        self.adminButton = QtWidgets.QRadioButton(Form)
        self.adminButton.setGeometry(QtCore.QRect(10, 180, 132, 22))
        self.adminButton.setObjectName("adminButton")
        self.staffButton = QtWidgets.QRadioButton(Form)
        self.staffButton.setGeometry(QtCore.QRect(170, 180, 132, 22))
        self.staffButton.setObjectName("staffButton")

        self.retranslateUi(Form)

        self.account.textChanged['QString'].connect(Form.btn_sate_le)
        self.password.textChanged['QString'].connect(Form.btn_sate_le)
        self.adminButton.toggled.connect(Form.btn_sate_le)
        self.staffButton.toggled.connect(Form.btn_sate_le)
        self.login.clicked.connect(Form.land_btn)
        Form.setTabOrder(self.account, self.password)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录"))
        self.login.setText(_translate("Form", "登录"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;font-weight:600;\">欢迎使用人事管理系统</span></p></body></html>"))
        self.name_la.setText(_translate("Form", "用户账户"))
        self.password_la.setText(_translate("Form", "<html><head/><body><p>密码</p></body></html>"))
        self.adminButton.setText(_translate("Form", "管理者"))
        self.staffButton.setText(_translate("Form", "职工"))


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("./source/staff.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    Form = QtWidgets.QWidget()
    ui = login_ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
