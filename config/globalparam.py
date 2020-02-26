# coding=utf-8

import os
import time
from config.readconfig import ReadConfig

# 读取配置文件
config_file_path = os.path.split(os.path.realpath(__file__))[0]
read_config = ReadConfig(os.path.join(config_file_path, 'config.ini'))
# 项目参数设置
prj_path = read_config.getValue('projectConfig', 'project_path')
# 日志路径
log_path = os.path.join(prj_path, 'report', 'log')
# 截图文件路径
img_path = os.path.join(prj_path, 'report', 'image', time.strftime("%Y_%m_%d"))
# 测试报告路径
report_path = os.path.join(prj_path, 'report', 'testreport')
# 默认浏览器
browser = 'firefox'

# 是否开启静默模式
headless = False

# 测试数据路径
data_path = os.path.join(prj_path, 'data', 'testdata')

# 测试环境地址
url = read_config.getValue("env", "url")
#
xml_report_path = os.path.join(prj_path, 'report', 'xml')
html_report_path = os.path.join(prj_path, 'report', 'html')

# cookie_path
cookie_path = os.path.join(prj_path, 'data', 'cookie_data')

#等待时间
tiny = 0.5
small= 1
middle = 2
long = 5

#c重试次数
RENUM = 0