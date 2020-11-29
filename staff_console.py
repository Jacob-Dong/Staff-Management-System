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
from staff_query_panel import staff_query_panel
from staff_modify_panel import staff_modify_panel
from staff_add_panel import staff_add_panel


#建立界面类
class staff_console(QDialog):
    def __init__(self,parent = None):
        super(staff_console,self).__init__(parent)

        #设置界面大小、名称、背景
        self.resize(940,600)
        self.setWindowTitle('员工管理')

        #窗体属性
        self.setWindowFlags(Qt.Widget)


        sql="SELECT stId,stName,stDepartment,stPositionalTitles,stSex,stNum FROM staff order by stId"

        #数据列名
        col_lst=['员工Id','员工姓名','员工所在部门','职务','性别','级别']
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
        self.qle.setText('请输入工号')
        self.buttonBox = QDialogButtonBox()
        #增删查改四个按钮
        self.queryButton = self.buttonBox.addButton("&查询信息",QDialogButtonBox.ActionRole)
        self.rankButton = self.buttonBox.addButton("&按级别显示",QDialogButtonBox.ActionRole)
        self.deleteButton = self.buttonBox.addButton("&删除信息",QDialogButtonBox.ActionRole)
        self.modifyBotton = self.buttonBox.addButton("&修改信息",QDialogButtonBox.ActionRole)
        self.refreshButton = self.buttonBox.addButton("&刷新信息",QDialogButtonBox.ActionRole)
        self.addButton = self.buttonBox.addButton("&添加员工",QDialogButtonBox.ActionRole)

        #设置按钮内字体样式
        self.queryButton.setFont(font)
        self.rankButton.setFont(font)
        self.deleteButton.setFont(font)
        self.modifyBotton.setFont(font)
        self.refreshButton.setFont(font)
        self.qle.setFont(font)

        #垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.qle)
        layout.addWidget(self.buttonBox)
        layout.addWidget(self.MyTable)
        self.setLayout(layout)

        self.queryButton.clicked.connect(self.query_data)#查询实现
        self.rankButton.clicked.connect(self.order_data)#级别显示
        self.deleteButton.clicked.connect(self.del_data)#删除实现
        self.modifyBotton.clicked.connect(self.modify_data)#修改实现
        self.refreshButton.clicked.connect(self.refresh_data)#刷新实现
        self.addButton.clicked.connect(self.add_data)#刷新实现

    #查询详细信息，会弹出一个信息窗口
    def query_data(self):
        tmp='请输入工号'
        tmp1=self.qle.text()
        if tmp1 == tmp:
           row_2 = self.MyTable.currentRow()
           userid= self.MyTable.item(row_2, 0).text()
        else:
           userid=self.qle.text()
           
        self.st_query=staff_query_panel(userid)
        self.st_query.show()
        print('This is query-area')


    #按级别显示数据
    def order_data(self):

        sql="SELECT stId,stName,stDepartment,stPositionalTitles,stSex,stNum FROM staff order by stNum" 
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
        print('This is order-area')


    #删除
    def del_data(self):
        #是否删除的对话框
        tmp='请输入工号'
        tmp1=self.qle.text()
        reply = QMessageBox.question(self, 'Message', 'Are you sure to delete it ?', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply ==  QMessageBox.Yes:
            
            #当前行
           
            if tmp1 == tmp:
                row_2 = self.MyTable.currentRow()
                userid= self.MyTable.item(row_2, 0).text()
            else:
                userid=self.qle.text()

            ls =int(userid)
            print(ls)
            sql="delete from staff where stId= %s "
            if LinkMysql().commit_sql1(sql,ls):
            #删除表格
               QMessageBox.information(self,"温馨提示", "删除成功",QMessageBox.Ok)
               print('You succeed')
            else:
               QMessageBox.warning(self, '温馨提示','有错误发生,请重试',QMessageBox.Retry)
               print('Something wrong')
    #修改数据，会弹出一个界面去修改
    def modify_data(self):
        tmp='请输入工号'
        tmp1=self.qle.text()
        if tmp1 == tmp:
           row_2 = self.MyTable.currentRow()
           userid= self.MyTable.item(row_2, 0).text()
        else:
           userid=self.qle.text()
           
        self.st_modify=staff_modify_panel(userid)
        self.st_modify.show()
        print('This is order-area')

       
    def refresh_data(self):
       
        sql="SELECT stId,stName,stDepartment,stPositionalTitles,stSex,stNum FROM staff order by stId"
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
        self.st_a= staff_add_panel()
        self.st_a.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./source/staff.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    c = staff_console()
    c.show()
    sys.exit(app.exec_())
