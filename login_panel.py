# -*- coding: utf-8 -*-

from PyQt5.Qt import QWidget, pyqtSignal, QPropertyAnimation, QAbstractAnimation, QPoint
from source.login_ui import login_ui


class login_panel(QWidget, login_ui):
    landing_sig = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def set_label(self):
        # 设置姓名密码为空
        self.account.setText("")
        self.password.setText("")

    def btn_sate_le(self):
        # 设置登陆按钮是否可用
        self.name = self.account.text()
        self.pd = self.password.text()
        self.admin_bu=self.adminButton.isChecked()
        self.staff_bu=self.staffButton.isChecked()
        self.bu=self.admin_bu or self.staff_bu
        if len(self.name) > 0 and len(self.pd) > 0:
            if(self.bu):
               self.login.setEnabled(True)
            else:
             self.login.setEnabled(False)
        else:
             self.login.setEnabled(False)
             

    def show_error(self):
        # 窗体抖动效果
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self)
        animation.setPropertyName(b'pos')
        animation.setKeyValueAt(0, self.pos())
        animation.setKeyValueAt(0.2, self.pos() + QPoint(15, 0))
        animation.setKeyValueAt(0.5, self.pos())
        animation.setKeyValueAt(0.7, self.pos() + QPoint(-15, 0))
        animation.setKeyValueAt(1, self.pos())
        animation.setDuration(100)
        animation.setLoopCount(3)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def land_btn(self):
        # 把用户名和密码通过型号传递出去
        ls = []
        ls.append(self.name)
        ls.append(self.pd)
        ls.append(self.admin_bu)
        ls.append(self.staff_bu)
        self.landing_sig.emit(ls)


if __name__ == '__main__':
    import sys
    from PyQt5.Qt import QApplication
    from PyQt5.QtGui import QIcon
    import qdarkstyle
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./source/staff.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    win = login_panel()
    win.show()

    sys.exit(app.exec_())
