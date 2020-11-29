# -*- coding: utf-8 -*-


from PyQt5.Qt import QWidget
import sys
from staff_add_panel import staff_add_panel

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 110, 112, 34))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))

class push(QWidget, Ui_Form):
    def __init__(self):
        super(push,self).__init__()
        self.setupUi(self)
        
    def showpu(self):
        p=staff_add_panel()
        p.show()
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
   
    pu=push()
    pu.pushButton.clicked.connect(pu.showpu)
    pu.show()
    sys.exit(app.exec_())
