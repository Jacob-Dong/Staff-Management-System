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
from sys_admin_add_panel  import sys_admin_add_panel
from sys_admin_query_panel  import sys_admin_query_panel
from sys_admin_modify_panel  import sys_admin_modify_panel


#建立界面类
class sys_admin_console(QDialog):
    def __init__(self,parent = None):
        super(sys_admin_console,self).__init__(parent)

        #设置界面大小、名称、背景
        self.resize(640,600)
        self.setWindowTitle('管理员账号管理')

        #窗体属性
        self.setWindowFlags(Qt.Widget)


        sql="SELECT aId,aName,aDep,aPosition FROM sys_admin order by aId"

        col_lst=['管理员Id','管理员姓名','管理员所在部门','管理员职务']
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
        self.qle.setText('请输入管理员id')
        self.buttonBox = QDialogButtonBox()
        #增删查改四个按钮
        self.queryButton = self.buttonBox.addButton("&查询信息",QDialogButtonBox.ActionRole)
        self.deleteButton = self.buttonBox.addButton("&删除信息",QDialogButtonBox.ActionRole)
        self.modifyBotton = self.buttonBox.addButton("&修改信息",QDialogButtonBox.ActionRole)
        self.refreshButton = self.buttonBox.addButton("&刷新信息",QDialogButtonBox.ActionRole)
        self.addButton = self.buttonBox.addButton("&添加管理",QDialogButtonBox.ActionRole)


        #设置按钮内字体样式
        self.queryButton.setFont(font)
        self.deleteButton.setFont(font)
        self.modifyBotton.setFont(font)
        self.refreshButton.setFont(font)
        self.addButton.setFont(font)
        self.qle.setFont(font)

        #垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.qle)
        layout.addWidget(self.buttonBox)
        layout.addWidget(self.MyTable)
        self.setLayout(layout)
        
        self.addButton.clicked.connect(self.add_data)#添加管理员
        self.queryButton.clicked.connect(self.query_data)#查询实现
        self.deleteButton.clicked.connect(self.del_data)#删除实现
        self.modifyBotton.clicked.connect(self.modify_data)#修改实现
        self.refreshButton.clicked.connect(self.refresh_data)#刷新实现 '''

    #查询详细信息，会弹出一个信息窗口
    def query_data(self):
        tmp='请输入管理员id'
        tmp1=self.qle.text()
        if tmp1 == tmp:
           row_2 = self.MyTable.currentRow()
           userid= self.MyTable.item(row_2, 0).text()
        else:
           userid=self.qle.text()
           
        self.sy_query=sys_admin_query_panel(userid)
        self.sy_query.show()
        print('This is query-area')



    #删除
    def del_data(self):
        #是否删除的对话框
        tmp='请输入管理员id'
        tmp1=self.qle.text()
        reply = QMessageBox.question(self, 'Message', 'Are you sure to delete it ?', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply ==  QMessageBox.Yes:
            
           
            if tmp1 == tmp:
                row_2 = self.MyTable.currentRow()
                userid= self.MyTable.item(row_2, 0).text()
            else:
                userid=self.qle.text()

            ls =int(userid)
            print(ls)
            sql="delete from sys_admin where  aId= %s "
            if LinkMysql().commit_sql(sql,ls):
            #删除表格
               QMessageBox.information(self,"温馨提示", "删除成功",QMessageBox.Ok)
               print('You succeed')
            else:
               QMessageBox.warning(self, '温馨提示','有错误发生,请重试',QMessageBox.Retry)
               print('Something wrong')
    #修改数据，会弹出一个界面去修改
    def modify_data(self):
        tmp='请输入管理员id'
        tmp1=self.qle.text()
        if tmp1 == tmp:
           row_2 = self.MyTable.currentRow()
           userid= self.MyTable.item(row_2, 0).text()
        else:
           userid=self.qle.text()
           
        self.sy_modify=sys_admin_modify_panel(userid)
        self.sy_modify.show()
        print('This is order-area')

       
    def refresh_data(self):
       
        sql="SELECT aId,aName,aDep,aPosition FROM sys_admin order by aId"
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

    def add_data(self):
        self.a= sys_admin_add_panel()
        self.a.show()  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./source/staff.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    c = sys_admin_console()
    c.show()
    sys.exit(app.exec_())
