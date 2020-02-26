# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 12:19
# @Author  : mrwuzs
# @Email   : mrwuzs@outlook.com
# @File    : mysql_pub.py
# @Software: PyCharm
'''
定义对mysql数据库基本操作的封装
1.单条数据的操作：insert，update，delete
2.查询数据表的一条数据
3.查询数据表的所有数据
'''

import  pymysql
from public.common.log import Log

class OpMysql():
    '''mysql操作类，基于pymysql的封装'''
    log = Log()


    def __init__(self,host,port,username,password,databasename):
        '''
        初始化opmysql对象
        :param host:数据库服务器地址
        :param username:数据库用户名
        :param password:用户的密码
        :param databasename:要操作的库名称
        '''
        try:
            self.conn = pymysql.connect(
                host = host,
                user = username,
                password = password,
                database = databasename,
                port = port,
                charset = 'utf8', # 如果sql语句中存在中文字符的时候，需要在这里指定charset的参数，否则中文显示乱码
                cursorclass = pymysql.cursors.DictCursor # pymysql默认select获取的数据是元祖类型，如果想要字典类型的数据，可以在这里统一设置
            )
            self.cur = self.conn.cursor() #创建游标
            self.log.info('数据库连接成功')
        except pymysql.Error as e:
            self.log.info("[connection_message]-host:%s;user:%s;password:%s;database:%s"%(host,username,password,databasename))
            self.log.error("数据库连接错误%s"%e)


    def op_sql(self,query,params=None):
        '''
        单条数据的操作，insert，update，delete
        :param query:包含%s的sql字符串，当params=None的时候，不包含%s
        :param params:一个元祖，默认为None
        :return:如果执行过程没有crash，返回True，反之返回False
        '''
        try:
            self.cur.execute(query,params)
            self.conn.commit()
            return True
        except BaseException as e:
            self.conn.rollback() #如果这里是执行的执行存储过程的sql命令，那么可能会存在rollback的情况，所以这里应该考虑到
            self.log.info("[sql_str_message]-%s"%self.cur.mogrify(query,params))
            self.log.error(e)
            return False

    def select_one(self,query,params=None):
        '''
        查询数据表的单条数据
        :param query: 包含%s的sql字符串，当params=None的时候，不包含%s
        :param params: 一个元祖，默认为None
        :return: 如果执行未crash，并以包含dict的列表的方式返回select的结果，否则返回错误代码001
        '''
        try:
            self.cur.execute(query,params)
            self.cur.scroll(0,"absolute") #光标回到初始位置，感觉自己的这句有点多余
            return self.cur.fetchone()
        except BaseException as e:
            self.log.info("[sql_str_message]-%s" % self.cur.mogrify(query, params))
            self.log.error(e)
            return "001" #错误代码001

    def select_all(self,query,params=None):
        '''
        查询数据表的单条数据
        :param query:包含%s的sql字符串，当params=None的时候，不包含%s
        :param params:一个元祖，默认为None
        :return:如果执行未crash，并以包含dict的列表的方式返回select的结果，否则返回错误代码001
        '''
        try:
            self.cur.execute(query,params)
            self.cur.scroll(0,"absolute") #光标回到初始位置，感觉这里得这句有点多余
            return self.cur.fetchall()
        except BaseException as e:
            self.log.info("[sql_str_message]-%s" % self.cur.mogrify(query, params))
            self.log.error(e)
            return "001" #错误代码001

    def insert_many(self,query,params):
        '''
        向数据表中插入多条数据
        :param query:包含%s的sql字符串，当params=None的时候，不包含%s
        :param params:一个内容为元祖的列表
        :return:如果执行过程没有crash，返回True，反之返回False
        '''
        try:
            self.cur.executemany(query,params)
            self.conn.commit()
            return True
        except BaseException as e:
            self.conn.rollback()
            self.log.info("[sql_str_message]-%s" % self.cur.mogrify(query, params))
            self.log.error(e)
            return False


    def delete_all(self,query):
        try:
            self.cur.execute(query)
            self.conn.commit()
            self.log.info("%s——--》清空表成功" %query)
            return True
        except BaseException as e:
            self.conn.rollback()
            self.log.info("[sql_str_message]-%s" % self.cur.mogrify(query))
            self.log.error(e)
            return False


    def  dis_db(self):
        self.cur.close()
        self.conn.close()
        self.log.info("断开数据库")

    #
    # def __del__(self):
    #     '''
    #     当该对象的引用计数为0的时候，python解释器会自动执行__dell__方法，自动释放游标和链接
    #     '''
    #     # self.cur.close()
    #     self.conn.close()
    #     print("数据库连接关闭")

if __name__ == "__main__":
    # test
    user = OpMysql('192.168.253.55',14316,'arkproxy','P@ssw0rd','user')
    uuid = user.select_one("SELECT UUID FROM project WHERE NAME  LIKE '%湖北%' ")
    print(uuid["UUID"])

    #rack.op_sql("UPDATE region_group  SET hub_vregion_id= '413c625c-323b-4f2c-8910-fdfb44de2219' WHERE name = %s;",("hub_vregion1",))



