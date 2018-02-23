# Python学习研究---密码本破解wifi密码

## 一、概述

+ 目的
    + 研究与理解wifi破解原理与手段

## 二、环境配置
+ 操作系统
    + windows7/windows10/linux

+ 运行环境
    + python3 （开发时使用版本python3.6）
        > 需要python的第三方模块 pywifi

+ 部署
    + 步骤 1 ： 安装好python3（下载安装包-->安装-->配置系统变量）
    + 步骤 2 ： 安装所需的python模块 pywifi （pip安装，或者下载模块包离线安装）
    + 步骤 3 ： 下代码,开启电脑的无线wifi开关（电脑需要有无线模块并开启）
    
## 三、代码概要

+ 实现过程：
    + 1）首先导入pywifi模块，因为要启用wifi那么必须要有启用wifi的模块。
    + 2）有了启用wifi的模块以后，我们首先要抓取网卡接口， 
        > 因为连接无线wifi，必须要有网卡才行。一台电脑可能有很多网卡， 
        > 但是一般都只有一个wifi网卡，我们选择一个网卡就行了。
    + 3）抓取到以后就进行连接测试，首先是要断开所有的wifi网卡上的已连接成功的，因为有可能wifi上有连接成功的在。
    + 4）断开所有的wifi以后，我们就可以进行相应的破解动作

## 四、目录结构

<pre><code>

./                            根目录
├─ cipher_generation_method_1           密码生成的代码1（穷举生成，一行一个）
|  ├─ psswd_num.py                      穷举生成不同组合的密码
│  ├─ README.md                         自述文件
|  └─ ...                               
├─ crack_method_1                       实现方法 1 的代码
│  ├─ python_wifi_pwd.py                
│  ├─ README.md                         自述文件
|  └─ ...                               
├─ crack_method_2                       实现方法 2 的代码
│  ├─ python_wifi_pwd.py                
│  ├─ README.md                         自述文件
|  └─ ...                               
├─ crack_method_3                       实现方法 3 的代码
│  ├─ python_wifi_pwd.py                
│  ├─ README.md                         自述文件
|  └─ ...                               
├─ resource_package                     离线资源包
│  ├─ pywifi-master.rar                 python的pywifi模块（离线包，需要解压放到系统中的python的安装库中才能全局使用）
│  ├─ README.md                         自述文件
|  └─ ...                               
├─ References                           参考资料（存放用于参考的文献电子书）
|  └─ ...                               
├─ README.md                            自述文件
└─ ...                                  更多目录或文件（欢迎创建）

</code></pre>

## 五、更新日志



## 六、开发日志



## 七、总结与展望



## 八、参考资料


分分钟搞定python破解无线wifi(https://www.cnblogs.com/shengulong/p/6367343.html)

如何获取隔壁wifi密码，非暴力破解(https://www.cnblogs.com/shengulong/p/6367343.html)

WIFI密码破解全攻略（https://jingyan.baidu.com/article/f79b7cb3ac67739144023ec0.html）