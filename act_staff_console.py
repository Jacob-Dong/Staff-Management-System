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
from act_add_panel import act_add_panel
from act_query_panel import act_query_panel
from act_modify_panel import act_modify_panel


#建立界面类
class act_staff_console(QDialog):
    def __init__(self,parent = None):
        super(act_staff_console,self).__init__(parent)

        #设置界面大小、名称、背景
        self.resize(500,600)
        self.setWindowTitle('活动管理')

        #窗体属性
        self.setWindowFlags(Qt.Widget)


        sql="SELECT acId,acTitle,acTime FROM activity order by acId"

        #数据列名
        col_lst=['活动Id','活动主题','活动时间']
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
        self.qle.setText('请输入活动id')
       

        #垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.qle)
        layout.addWidget(self.MyTable)
        self.setLayout(layout)


    #查询详细信息，会弹出一个信息窗口
    def query_data(self):
        tmp='请输入活动id'
        tmp1=self.qle.text()
        if tmp1 == tmp:
           row_2 = self.MyTable.currentRow()
           userid= self.MyTable.item(row_2, 0).text()
        else:
           userid=self.qle.text()
           
        self.ac_query=act_query_panel(userid)
        self.ac_query.show()
        print('This is query-area')


    #删除
    def del_data(self):
        #是否删除的对话框
        tmp='请输入活动id'
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
            sql="delete from activity where acId= %s "
            if LinkMysql().commit_sql(sql,ls):
            #删除表格
               QMessageBox.information(self,"温馨提示", "删除成功",QMessageBox.Ok)
               print('You succeed')
            else:
               QMessageBox.warning(self, '温馨提示','无法删除,有错误产生',QMessageBox.Retry)
               print('Something wrong')
    #修改数据，会弹出一个界面去修改
    def modify_data(self):
        tmp='请输入活动id'
        tmp1=self.qle.text()
        if tmp1 == tmp:
           row_2 = self.MyTable.currentRow()
           userid= self.MyTable.item(row_2, 0).text()
        else:
           userid=self.qle.text()
           
        self.ac_modify=act_modify_panel(userid)
        self.ac_modify.show()
        print('This is order-area')

       
    def refresh_data(self):
       
        sql="SELECT acId,acTitle,acTime FROM activity order by acId"
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
        self.a= act_add_panel()
        self.a.show()  


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./source/staff.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    c = act_staff_console()
    c.show()
    sys.exit(app.exec_())
