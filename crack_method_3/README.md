# Python学习研究---密码本破解wifi密码

## 一、概述

+ 目的
    + 研究与理解wifi破解原理与手段

## 二、环境配置
+ 操作系统
    + windows7/windows10/linux

+ 运行环境
    + python3 （开发时使用版本python3.6）
        + 需要python的第三方模块 pywifi

+ 部署
    + 步骤 1 ： 安装好python3（下载安装包-->安装-->配置系统变量）
    + 步骤 2 ： 安装所需的python模块 pywifi （pip安装，或者下载模块包离线安装）
    + 步骤 3 ： 下代码,开启电脑的无线wifi开关（电脑需要有无线模块并开启）


> pywifi模块安装说明:

+ 在线安装方法:
    + 1）我们用cmd命令行,进入到你的文件目录 
    + 2）使用命令pip install pywifi

+ 本地安装方法： (pywifi的模块包在../resource_package/pywifi-master.rar)
    + 1）下载解压好以后，我们用cmd命令行,进入到你的文件目录， 
    + 2）使用命令pip install . 注意了（install后面有个点） 
    + 3）然后就会安装了，等一会就可以了。




## 三、代码概要

+ 实现过程：
    + 1）首先导入pywifi模块，因为要启用wifi那么必须要有启用wifi的模块。
    + 2）有了启用wifi的模块以后，我们首先要抓取网卡接口，  
        + 因为连接无线wifi，必须要有网卡才行。一台电脑可能有很多网卡
        + 但是一般都只有一个wifi网卡，我们选择一个网卡就行了
    + 3）抓取到以后就进行连接测试，首先是要断开所有的wifi网卡上的已连接成功的，因为有可能wifi上有连接成功的在。
    + 4）断开所有的wifi以后，我们就可以进行相应的破解动作

## 四、目录结构

<pre><code>

./                            根目录（crack_method_3 实现方法 3 的代码）
├─ python_wifi_pwd.py                python3的脚本
├─ wifi_passwd.txt                   脚本要使用的密码字典,一行一个密码
├─ pj_res.txt                        破解结果日志
├─ wifi_ssid_list.txt                要进入破解队列的wifi的ssid列表（一行一个）
├─ README.md                         自述文件
└─ ...                               


</code></pre>

+ 使用说明
1、打开python_wifi_pwd.py修改里面的要破解的破解的密码本位置、破解结果日子位置、破解wifi列表位置
2、可进入python_wifi_pwd.py里注释掉执行破解的函数，修改完破解ssid的列表，先执行扫描
3、执行完ssid后，打开fi_ssid_list.txt，进行删减，再注释掉执行扫描wifi列表的，执行破解

## 五、更新日志



## 六、开发日志

>    2018-02-21 15:54:40 

+ 问题1：win7 下，列举的wifi名称有乱码，识别错误，会报错停止，无法全部写入破解的wifi的ssid列表

+ 问题2：win7 下，破解wifi列表列举的wifi名称有乱码，识别错误，会报错停止




## 七、总结与展望



## 八、参考资料

分分钟搞定python破解无线wifi(https://www.cnblogs.com/shengulong/p/6367343.html)

如何获取隔壁wifi密码，非暴力破解(https://www.cnblogs.com/shengulong/p/6367343.html)

WIFI密码破解全攻略（https://jingyan.baidu.com/article/f79b7cb3ac67739144023ec0.html）

