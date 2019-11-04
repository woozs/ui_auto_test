本框架采用python3+slenium3+allure2+pytest开发完成

# 环境要求

```
allure-pytest==2.8.6
allure-python-commons==2.8.6
atomicwrites==1.3.0
attrs==19.3.0
colorama==0.4.1
importlib-metadata==0.23
more-itertools==7.2.0
nose==1.3.7
packaging==19.2
Pillow==6.2.0
pluggy==0.13.0
py==1.8.0
pyparsing==2.4.2
pytesseract==0.3.0
pytest==5.2.2
pytest-html==2.0.0
pytest-metadata==1.8.0
pytest-rerunfailures==7.0
selenium==3.141.0
six==1.12.0
urllib3==1.25.6
wcwidth==0.1.7
xlrd==1.2.0
zipp==0.6.0
```

# 安装allure2

windows下安装 Allure2工具
环境
1、安装JDK1.8+
2、安装Allure2
下载Allure2的zip安装包
解压到allure-commandline目录
进入bin目录，运行allure.bat
添加allure到环境变量PATH（\安装路径\allure-commandline\bin）

# 测试框架介绍

![](https://raw.githubusercontent.com/JasonsteagleWu/picgo_01/master/20191103135604.png)

# 配置文件

```
#主目录文件路需要手动配置
[projectConfig]
project_path=H:\cmp
#测试环境，展示到测试报，可自定义配置
[env]
url = http:\\192.168.54.13
tester = wuzushun
versioncode = v1.0
csdpversion = v3.8.26

```

# 测试数据

![](https://raw.githubusercontent.com/JasonsteagleWu/picgo_01/master/20191103140006.png)

![](https://raw.githubusercontent.com/JasonsteagleWu/picgo_01/master/20191103140039.png)

# 测试报告

测试报告路径：

`H:\cmp\report\html\index.html`

![](https://raw.githubusercontent.com/JasonsteagleWu/picgo_01/master/20191103140426.png)

![](https://raw.githubusercontent.com/JasonsteagleWu/picgo_01/master/20191103140129.png)

![](https://raw.githubusercontent.com/JasonsteagleWu/picgo_01/master/20191103140215.png)