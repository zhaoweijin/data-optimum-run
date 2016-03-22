#!/usr/bin/env python
#coding=utf-8

#导入相关模块
import MySQLdb

#建立和mysql数据库的连接
conn = MySQLdb.connect(host='192.168.200.248',user='optimum',passwd='3323123j')
# #获取游标
# curs = conn.cursor()
# #执行SQL,创建一个数据库
# # curs.execute("create database pythondb")
# #选择连接哪个数据库
# conn.select_db('pythondb')
# #执行SQL,创建一个表
# curs.execute("create table test(id int,message varchar(50))")
# #插入一条记录
# value = [1,"davehe"]
# curs.execute("insert into test values(%s,%s)",value)
# #插入多条记录
# values = []
# for i in range(20):
#     values.append((i,'hello mysqldb' + str(i)))
# curs.executemany("insert into test values(%s,%s)",values)
# #提交修改
# conn.commit()
# #关闭游标连接,释放资源
# curs.close()
# #关闭连接
# conn.close()

#获取游标
curs = conn.cursor()
#选择连接哪个数据库
conn.select_db('optimum')
#查看共有多少条记录
count = curs.execute('select * from auth_user')
print "一共有%s条记录" % count
#获取一条记录,以一个元组返回
# result = curs.fetchone()
# print "当前的一条记录 ID:%s message:%s" % result
#获取后10条记录,由于之前执行了getchone(),所以游标已经指到第二条记录,下面也就从第二条记录开始返回
results = curs.fetchmany(10)
for r in results:
    print r
#重置游标位置,0,为偏移量,mode = relative(默认)
curs.scroll(0,mode='absolute')
#获取所有记录
results = curs.fetchall()
for r in results:
    print r

#提交修改
conn.commit()
#关闭游标连接,释放资源
curs.close()
#关闭连接
conn.close()