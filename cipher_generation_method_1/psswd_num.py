# coding:utf-8
# 生成6位纯数字密码字典
#-------------------------------------------------------------------------------
# # version 1.0
# import os
# pds = []
# rg = range(0,10)
# for first in rg:
#     for second in rg:
#         for three in rg:
#             for four in rg:
#                 for five in rg:
#                     for six in rg:
#                         num = "%s%s%s%s%s%s"%(first,second,three,four,five,six)
#                         pds.append(num)
# file_path = r"C:\Users\XieZhenBin\Desktop\psswdNum6.txt"   # 生成6位纯数字密码字典文件
# file_object = open(file_path,'w')
# file_object.writelines(['%s%s' %(x,os.linesep) for x in pds])
# file_object.close()

#-------------------------------------------------------------------------------
# # version 1.1
# # 生成6位纯数字密码字典
# import os
# pds = []
# rg = range(0,10)
# for first in rg:
#     for second in rg:
#         for three in rg:
#             for four in rg:
#                 for five in rg:
#                     for six in rg:
#                         num = "%s%s%s%s%s%s"%(first,second,three,four,five,six)
#                         pds.append(num)
# file_path = r"C:\Users\XieZhenBin\Desktop\psswdNum6.txt"   # 生成6位纯数字密码字典文件
# file_object = open(file_path,'w')
# file_object.writelines(['%s%s' %(x,os.linesep) for x in pds])
# file_object.close()

#-------------------------------------------------------------------------------
# # # version 1.2
# # # 生成6位纯数字、字母、特殊符号密码字典
# import os
# pds = []
# # rg = range(0,10) # 0-9数字
# # 26小写字母
# # 26大写字母
# # 特殊符号
# # 0-9数字
# rg = [
#        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
#        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
#        '!','@','#','$','%','^','&','*','(',')','-','_','+','=',',',';',
#        '0','1','2','3','4','5','6','7','8','9',' '
#      ] 
# rg0 = [
#        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
#      ]

# rg1 = [
#        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
#      ] 
# rg2 = [
#        '0','1','2','3','4','5','6','7','8','9'
#      ] 
# rg3 = [
#       '!','@','#','$','%','^','&','*','(',')','-','_','+','=',',',';','~','`','|',':','/',' '
#      ] 
# # for first in rg:
# #     for second in rg:
# #         for three in rg:
# #             for four in rg:
# #                 for five in rg:
# #                     for six in rg:
# #                         num = "%s%s%s%s%s%s"%(first,second,three,four,five,six)
# #                         pds.append(num)
# for first in rg:
#     for second in rg:
#         num = "%s%s\n"%(first,second)
#         pds.append(num)

# file_path = r"C:\Users\XieZhenBin\Desktop\psswdNum262609.txt"   # 生成6位纯数字密码字典文件
# file_object = open(file_path,'w')
# # file_object.writelines(['%s%s' %(x,os.linesep) for x in pds])
# # file_object.writelines(['%s%s' %(x,os.linesep) for x in pds])
# file_object.writelines(pds)
# # os.linesep 是行位换行符 由于linux和windows操作系统的换行符不一致
# file_object.close()

# ------------------------------------------------------------------------------
# # version 1.3
# # 生成8位纯数字、字母、特殊符号密码字典
import os
pds = []
# rg = range(0,10) # 0-9数字
# 26小写字母
# 26大写字母
# 特殊符号
# 0-9数字
rg = [
       'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
       'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
       '!','@','#','$','%','^','&','*','(',')','-','_','+','=',',',';',
       '0','1','2','3','4','5','6','7','8','9',' '
     ] 
rg0 = [
       'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
     ]

rg1 = [
       'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
     ] 
rg2 = [
       '0','1','2','3','4','5','6','7','8','9'
     ] 
rg3 = [
      '!','@','#','$','%','^','&','*','(',')','-','_','+','=',',',';','~','`','|',':','/',' '
     ] 
rg4 = [
       'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
       'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
       '0','1','2','3','4','5','6','7','8','9'
     ] 
# for first in rg:
#     for second in rg:
#         for three in rg:
#             for four in rg:
#                 for five in rg:
#                     for six in rg:
#                         num = "%s%s%s%s%s%s"%(first,second,three,four,five,six)
#                         pds.append(num)

# for first in rg:
#     for second in rg:
#         num = "%s%s\n"%(first,second)
#         pds.append(num)

# file_path = r"C:\Users\XieZhenBin\Desktop\psswd_num8.txt"          # 生成8位密码字典文件 绝对地址写法
file_path = r"psswd_num8.txt"          # 生成8位密码字典文件 相对地址写法


file_object = open(file_path,'a')
# file_object.write(res)
for first in rg4:
    for second in rg4:
        for three in rg4:
            for four in rg4:
                for five in rg4:
                    for six in rg4:
                        for seven in rg4:
                            for eight in rg4:
                                num = "%s%s%s%s%s%s%s%s\n"%(first,second,three,four,five,six,seven,eight)
                                # pds.append(num)
                                print(num)
                                file_object.write(num)


# file_path = r"C:\Users\XieZhenBin\Desktop\psswdNum262609.txt"   # 生成6位纯数字密码字典文件

# file_object.writelines(['%s%s' %(x,os.linesep) for x in pds])
# file_object.writelines(['%s%s' %(x,os.linesep) for x in pds])
# file_object.writelines(pds)
# os.linesep 是行位换行符 由于linux和windows操作系统的换行符不一致
file_object.close()