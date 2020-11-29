# -*- coding: utf-8 -*-


import sys
import qdarkstyle
from PyQt5.QtGui import QIcon

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 600)
        MainWindow.setMinimumSize(QtCore.QSize(770, 600))
        MainWindow.setMaximumSize(QtCore.QSize(770, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 160, 746, 245))
        self.widget.setObjectName("widget")

        # 设置commandlinkButton格式以及功能

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.s_query_2 = QtWidgets.QCommandLinkButton(self.widget)
        self.s_query_2.setObjectName("s_query_2")
        self.horizontalLayout.addWidget(self.s_query_2)

        self.d_query_2 = QtWidgets.QCommandLinkButton(self.widget)
        self.d_query_2.setObjectName("d_query_2")
        self.horizontalLayout.addWidget(self.d_query_2)

        self.st_query_2 = QtWidgets.QCommandLinkButton(self.widget)
        self.st_query_2.setObjectName("st_query_2")
        self.horizontalLayout.addWidget(self.st_query_2)

        self.ac_query_2 = QtWidgets.QCommandLinkButton(self.widget)
        self.ac_query_2.setObjectName("ac_query_2")
        self.horizontalLayout.addWidget(self.ac_query_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # 水平第二行

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.s_add_2 = QtWidgets.QCommandLinkButton(self.widget)
        self.s_add_2.setObjectName("s_add_2")
        self.horizontalLayout_2.addWidget(self.s_add_2)

        self.d_add_2 = QtWidgets.QCommandLinkButton(self.widget)
        self.d_add_2.setObjectName("d_add_2")
        self.horizontalLayout_2.addWidget(self.d_add_2)

        self.st_add_2 = QtWidgets.QCommandLinkButton(self.widget)
        self.st_add_2.setObjectName("st_add_2")
        self.horizontalLayout_2.addWidget(self.st_add_2)

        self.ac_add_2 = QtWidgets.QCommandLinkButton(self.widget)
        self.ac_add_2.setObjectName("ac_add_2")
        self.horizontalLayout_2.addWidget(self.ac_add_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # 水平第三行

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.s_update_2 = QtWidgets.QCommandLinkButton(self.widget)
        self.s_update_2.setObjectName("s_update_2")
        self.horizontalLayout_3.addWidget(self.s_update_2)

        self.d_update_2 = QtWidgets.QCommandLinkButton(self.widget)
        self.d_update_2.setObjectName("d_update_2")
        self.horizontalLayout_3.addWidget(self.d_update_2)

        self.st_update_2 = QtWidgets.QCommandLinkButton(self.widget)
        self.st_update_2.setObjectName("st_update_2")
        self.horizontalLayout_3.addWidget(self.st_update_2)

        self.ac_update_2 = QtWidgets.QCommandLinkButton(self.widget)
        self.ac_update_2.setObjectName("ac_update_2")
        self.horizontalLayout_3.addWidget(self.ac_update_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        # 水平第四行

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.s_delete_2 = QtWidgets.QCommandLinkButton(self.widget)
        self.s_delete_2.setObjectName("s_delete_2")
        self.horizontalLayout_4.addWidget(self.s_delete_2)

        self.d_delete_2 = QtWidgets.QCommandLinkButton(self.widget)
        self.d_delete_2.setObjectName("d_delete_2")
        self.horizontalLayout_4.addWidget(self.d_delete_2)

        self.st_delete_2 = QtWidgets.QCommandLinkButton(self.widget)
        self.st_delete_2.setObjectName("st_delete_2")
        self.horizontalLayout_4.addWidget(self.st_delete_2)

        self.ac_delete_2 = QtWidgets.QCommandLinkButton(self.widget)
        self.ac_delete_2.setObjectName("ac_delete_2")
        self.horizontalLayout_4.addWidget(self.ac_delete_2)

        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)

        # 设置menubar

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 30))
        self.menubar.setObjectName("menubar")
        self.system = QtWidgets.QMenu(self.menubar)
        self.system.setObjectName("system")
        self.department = QtWidgets.QMenu(self.menubar)
        self.department.setObjectName("department")
        self.staff = QtWidgets.QMenu(self.menubar)
        self.staff.setObjectName("staff")
        self.activity = QtWidgets.QMenu(self.menubar)
        self.activity.setObjectName("activity")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 设置系统设置功能
        self.s_query = QtWidgets.QAction(MainWindow)
        self.s_query.setObjectName("s_query")
        self.s_add = QtWidgets.QAction(MainWindow)
        self.s_add.setObjectName("s_add")
        self.s_update = QtWidgets.QAction(MainWindow)
        self.s_update.setObjectName("s_update")
        self.s_delete = QtWidgets.QAction(MainWindow)
        self.s_delete.setObjectName("s_delete")

        # 设置部门功能
        self.d_query = QtWidgets.QAction(MainWindow)
        self.d_query.setObjectName("d_query")
        self.d_add = QtWidgets.QAction(MainWindow)
        self.d_add.setObjectName("d_add")
        self.d_update = QtWidgets.QAction(MainWindow)
        self.d_update.setObjectName("d_update")
        self.d_delete = QtWidgets.QAction(MainWindow)
        self.d_delete.setObjectName("d_delete")

        # 设置员工功能
        self.st_query = QtWidgets.QAction(MainWindow)
        self.st_query.setObjectName("st_query")
        self.st_add = QtWidgets.QAction(MainWindow)
        self.st_add.setObjectName("st_add")
        self.st_update = QtWidgets.QAction(MainWindow)
        self.st_update.setObjectName("st_update")
        self.st_delete = QtWidgets.QAction(MainWindow)
        self.st_delete.setObjectName("st_delete")

        # 设置活动功能
        self.ac_query = QtWidgets.QAction(MainWindow)
        self.ac_query.setObjectName("ac_query")
        self.ac_add = QtWidgets.QAction(MainWindow)
        self.ac_add.setObjectName("ac_add")
        self.ac_update = QtWidgets.QAction(MainWindow)
        self.ac_update.setObjectName("ac_update")
        self.ac_delete = QtWidgets.QAction(MainWindow)
        self.ac_delete.setObjectName("ac_delete")

        # 添加动作
        self.system.addAction(self.s_query)
        self.system.addAction(self.s_add)
        self.system.addAction(self.s_update)
        self.system.addAction(self.s_delete)
        self.department.addAction(self.d_query)
        self.department.addAction(self.d_add)
        self.department.addAction(self.d_update)
        self.department.addAction(self.d_delete)
        self.staff.addAction(self.st_query)
        self.staff.addAction(self.st_add)
        self.staff.addAction(self.st_update)
        self.staff.addAction(self.st_delete)
        self.activity.addAction(self.ac_query)
        self.activity.addAction(self.ac_add)
        self.activity.addAction(self.ac_update)
        self.activity.addAction(self.ac_delete)

        self.menubar.addAction(self.system.menuAction())
        self.menubar.addAction(self.department.menuAction())
        self.menubar.addAction(self.staff.menuAction())
        self.menubar.addAction(self.activity.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人事管理系统"))

        # 中间功能区域
        self.s_query_2.setText(_translate("MainWindow", "查看人员信息"))
        self.d_query_2.setText(_translate("MainWindow", "查看部门"))
        self.st_query_2.setText(_translate("MainWindow", "查看员工信息"))
        self.ac_query_2.setText(_translate("MainWindow", "查看活动"))

        self.s_add_2.setText(_translate("MainWindow", "添加工作人员"))
        self.d_add_2.setText(_translate("MainWindow", "添加部门"))
        self.st_add_2.setText(_translate("MainWindow", "添加员工信息"))
        self.ac_add_2.setText(_translate("MainWindow", "添加活动"))

        self.s_update_2.setText(_translate("MainWindow", "修改人员信息"))
        self.d_update_2.setText(_translate("MainWindow", "修改部门信息"))
        self.st_update_2.setText(_translate("MainWindow", "修改员工信息"))
        self.ac_update_2.setText(_translate("MainWindow", "修改活动"))

        self.s_delete_2.setText(_translate("MainWindow", "删除人员信息"))
        self.d_delete_2.setText(_translate("MainWindow", "删除部门信息"))
        self.st_delete_2.setText(_translate("MainWindow", "删除员工信息"))
        self.ac_delete_2.setText(_translate("MainWindow", "删除活动"))

        # 上方菜单栏
        self.system.setTitle(_translate("MainWindow", "系统管理"))
        self.department.setTitle(_translate("MainWindow", "部门管理"))
        self.staff.setTitle(_translate("MainWindow", "员工管理"))
        self.activity.setTitle(_translate("MainWindow", "活动管理"))

        # 系统功能
        self.s_query.setText(_translate("MainWindow", "查看人员信息"))
        self.s_add.setText(_translate("MainWindow", "添加工作人员"))
        self.s_update.setText(_translate("MainWindow", "修改人员信息"))
        self.s_delete.setText(_translate("MainWindow", "删除人员信息"))

        # 部门功能
        self.d_query.setText(_translate("MainWindow", "查看部门"))
        self.d_add.setText(_translate("MainWindow", "添加部门"))
        self.d_update.setText(_translate("MainWindow", "修改部门信息"))
        self.d_delete.setText(_translate("MainWindow", "删除部门信息"))

        # 员工功能
        self.st_query.setText(_translate("MainWindow", "查看员工信息"))
        self.st_add.setText(_translate("MainWindow", "添加员工信息"))
        self.st_update.setText(_translate("MainWindow", "修改员工信息"))
        self.st_delete.setText(_translate("MainWindow", "删除员工信息"))

        # 活动功能
        self.ac_query.setText(_translate("MainWindow", "查看活动"))
        self.ac_add.setText(_translate("MainWindow", "添加活动"))
        self.ac_update.setText(_translate("MainWindow", "修改活动"))
        self.ac_delete.setText(_translate("MainWindow", "删除活动"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    app.setWindowIcon(QIcon("./source/staff.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())