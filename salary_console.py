# -*- coding: utf-8 -*-
#导入包
import sys
import pymysql
import qdarkstyle
from PyQt5.QtGui import QIcon, QFont
from PyQt5.Qt import QWidget
from PyQt5 import QtGui,QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QFrame,QApplication,QDialog, QDialogButtonBox,
        QMessageBox,QVBoxLayout, QLineEdit,QTableWidgetItem,QTableWidget,QHBoxLayout)

from link_to_database import LinkMysql
from salary_query_panel import salary_query_panel
from salary_modify_panel import salary_modify_panel



#建立界面类
class salary_console(QDialog):
    def __init__(self,parent = None):
        super(salary_console,self).__init__(parent)

        #设置界面大小、名称、背景
        self.resize(500,600)
        self.setWindowTitle('工资管理')

        #窗体属性
        self.setWindowFlags(Qt.Widget)


        sql="SELECT staId,staName,origin_salary FROM salary order by staId"

        #数据列名
        col_lst=['员工Id','姓名','底薪']
        type=1
        data=LinkMysql().select_single(sql,type)

        #数据的大小
        row = len(data)
        vol = len(data[0])


        #插入表格
        self.MyTable = QtWidgets.QTableWidget(row,vol)
        self.MyTable.setColumnCount(vol)
        self.MyTable.setRowCount(row)
        self.MyTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.MyTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.MyTable.setObjectName("MyTable")
        font = QtGui.QFont('微软雅黑',10)

        #设置字体、表头
        self.MyTable.horizontalHeader().setFont(font)
        self.MyTable.setHorizontalHeaderLabels(col_lst)
        #设置竖直方向表头不可见
        self.MyTable.verticalHeader().setVisible(False)
        self.MyTable.setFrameShape(QFrame.NoFrame)

        #构建表格插入数据
        for i in range(row):
            for j in range(vol):
                temp_data = data[i][j]  # 临时记录，不能直接插入表格
                self.data1 = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                self.MyTable.setItem(i, j, self.data1)


        #编辑按钮
        self.qle = QLineEdit()
        self.qle.setText('请输入员工id')
        self.buttonBox = QDialogButtonBox()
        #增删查改四个按钮
        self.queryButton = self.buttonBox.addButton("&查询信息",QDialogButtonBox.ActionRole)
        self.modifyBotton = self.buttonBox.addButton("&修改信息",QDialogButtonBox.ActionRole)
        self.refreshButton = self.buttonBox.addButton("&刷新信息",QDialogButtonBox.ActionRole)

        self.qle.setFont(font)

        #垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.qle)
        layout.addWidget(self.buttonBox)
        layout.addWidget(self.MyTable)
        self.setLayout(layout)

        self.queryButton.clicked.connect(self.query_data)#查询实现
        self.modifyBotton.clicked.connect(self.modify_data)#修改实现
        self.refreshButton.clicked.connect(self.refresh_data)#刷新实现

    #查询详细信息，会弹出一个信息窗口
    def query_data(self):
        tmp='请输入员工id'
        tmp1=self.qle.text()
        if tmp1 == tmp:
           row_2 = self.MyTable.currentRow()
           userid= self.MyTable.item(row_2, 0).text()
        else:
           userid=self.qle.text()
           
        self.s_query=salary_query_panel(userid)
        self.s_query.show()
        print('This is query-area')


    
    #修改数据，会弹出一个界面去修改
    def modify_data(self):
        tmp='请输入员工id'
        tmp1=self.qle.text()
        if tmp1 == tmp:
           row_2 = self.MyTable.currentRow()
           userid= self.MyTable.item(row_2, 0).text()
        else:
           userid=self.qle.text()
           
        self.s_modify=salary_modify_panel(userid)
        self.s_modify.show()
        print('This is order-area')

       
    def refresh_data(self):
       
        sql="SELECT staId,staName,origin_salary FROM salary order by staId"
        type=1
        data=LinkMysql().select_single(sql,type)

        #数据的大小
        row = len(data)
        vol = len(data[0])
        self.MyTable.setRowCount(row)

        #构建表格插入数据
        for i in range(row):
            for j in range(vol):
                temp_data = data[i][j]  # 临时记录，不能直接插入表格
                self.data1 = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                self.MyTable.setItem(i, j, self.data1)

        print('This is refresh-area')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./source/staff.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    c = salary_console()
    c.show()
    sys.exit(app.exec_())
