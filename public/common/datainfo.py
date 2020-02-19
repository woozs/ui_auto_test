#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 21:38
# @Author  : mrwuzs
# @Site    :
# @Software: PyCharm

import codecs
import os
import xlrd
import chardet
from config import globalparam

data_path = globalparam.data_path


def get_xls_to_dict(xlsname, sheetname):
    """
    读取excel表结果为dict
    第一行为字典的key，下面的为值
    return [{'title':'1','user':'root'},{'title':'2','user':'xiaoshitou'}]
    """
    datapath = os.path.join(data_path, xlsname)
    xls1 = xlrd.open_workbook(datapath)
    table = xls1.sheet_by_name(sheetname)

    dataresult = [table.row_values(i) for i in range(0, table.nrows)]
    # 将list转化成dict


    result1 = [dict(zip(dataresult[0], dataresult[i]))
               for i in range(1, len(dataresult))]
    keys = []
    # 给用例添加上测试用例名称
    for i in result1:
        keys.append(i["casename"])
    result = dict(zip(keys, result1))
    return result

def get_url_data(title):
    """
    读取txt文件，转化成dict;读取url和导航栏的对应关系
    将txt转化成一个字典:下单=>/admin/order/index
    {'title1':'url1','下单':'/admin/order/index'}
    """
    name = 'urlsource.txt'
    txtpath = os.path.join(data_path, name)
    with codecs.open(txtpath, 'r', encoding='utf-8') as f:
        txtcontent = f.readlines()
    txtdict = dict([txt.strip().replace('\ufeff', '').split('=>')
                    for txt in txtcontent])
    return txtdict[title]


def get_xls_to_list(excelname, sheetname):
    """
    读取excel表，返回一个list,只是返回第一列的值
    return [1,2,3,4,5]
    """
    datapath = os.path.join(data_path, excelname)
    excel = xlrd.open_workbook(datapath)
    table = excel.sheet_by_name(sheetname)
    result = [table.row_values(i)[0].strip() for i in range(1, table.nrows)]
    return result


if __name__ == '__main__':
    # res = get_xls_to_list('tenantdata.xlsx','Sheet1')
    res = get_xls_to_dict('tenantdata.xlsx', 'Sheet1')
    print(res)
    print(res["创建运营部门"])
