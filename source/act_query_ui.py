# -*- coding: utf-8 -*-



import sys
import qdarkstyle
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets


class act_query_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(568, 621)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 70, 91, 31))
        self.label.setObjectName("label")
        self.title_ln = QtWidgets.QLineEdit(Form)
        self.title_ln.setGeometry(QtCore.QRect(110, 70, 131, 31))
        self.title_ln.setObjectName("title_ln")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 91, 31))
        self.label_2.setObjectName("label_2")
        self.time = QtWidgets.QDateEdit(Form)
        self.time.setGeometry(QtCore.QRect(110, 130, 131, 31))
        self.time.setObjectName("time")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 91, 31))
        self.label_3.setObjectName("label_3")
        self.con_ln = QtWidgets.QTextEdit(Form)
        self.con_ln.setGeometry(QtCore.QRect(20, 230, 531, 301))
        self.con_ln.setObjectName("con_ln")
        self.OK = QtWidgets.QPushButton(Form)
        self.OK.setGeometry(QtCore.QRect(430, 570, 112, 34))
        self.OK.setObjectName("OK")

        self.retranslateUi(Form)
        self.OK.clicked.connect(Form.fade)
        
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "查看活动信息"))
        self.label.setText(_translate("Form", "活动主题"))
        self.label_2.setText(_translate("Form", "活动时间"))
        self.label_3.setText(_translate("Form", "活动内容"))
        self.OK.setText(_translate("Form", "OK"))

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("./source/staff.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    Form = QtWidgets.QWidget()
    ui = act_query_ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())