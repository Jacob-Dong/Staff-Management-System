# -*- coding: utf-8 -*-
import pymysql


class LinkMysql(object):
    def __init__(self):
        
        self.conn = pymysql.connect("localhost", "root", "root", "project",charset='utf8')
        #获取游标、数据
        self.cur = self.conn.cursor()
    
    #管理员登录
    def select_admin(self, ls):
        sql = "SELECT aPwd FROM sys_admin WHERE aId = %s"
        return self.select_sql(sql, ls)

     #员工登录   
    def select_staff(self, ls):
        sql = "SELECT staPwd FROM sys_staff WHERE staId = %s"
        return self.select_sql(sql, ls)

    def commit_sql(self, sql, ls):
        """
        执行增删改语句，
        :return: 返回执行的结果, 1 = 成功, 0 = 失败
        """
        try:
            self.cur.execute(sql, ls)
            self.conn.commit()
            return 1
        except Exception as e:
            self.conn.rollback()
            return 0
        finally:
            self.cur.close()
            self.conn.close()

    def commit_sql1(self, sql, ls):
        """
        执行增删改语句，
        :return: 返回执行的结果, 1 = 成功, 0 = 失败
        """
        try:
            self.cur.execute(sql, ls)
            self.conn.commit()
            return 1
        except pymysql.InternalError as e1:
            return 1
        except Exception as e:
            self.conn.rollback()
            return 0
        finally:
            self.cur.close()
            self.conn.close()

    def select_sql(self, sql, ls):
        """
        执行有条件的查询语句
        :return: 返回查询得到的数据集
        """
        self.cur.execute(sql, ls)
        data = self.cur.fetchall()
        self.cur.close()
        self.conn.close()
        return data

    def select_single(self, sql,type=1):
        """
        执行没有条件的查询语句 type 1 = 数据 , 0 = 列
        :return: 返回查询得到的数据集
        """
        self.cur.execute(sql)
        if type:
            data = self.cur.fetchall()
        else:
            data = self.cur.description
        self.cur.close()
        self.conn.close()
        return data


if __name__ == '__main__':
    name = "姓名"
    link = LinkMysql()
    data = link.select_temporary(name)
    print(data)
