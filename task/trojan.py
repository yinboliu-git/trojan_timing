import datetime
import os
import time

# 获得当前时间
now = datetime.datetime.now()

H = now.strftime("%H")
M = now.strftime("%M")

D = now.strftime("%d")
print(f'当前时间:{D}日{H}点{M}分')
while True:
    now = datetime.datetime.now()
    H = now.strftime("%H")
    M = now.strftime("%M")
    D = now.strftime("%d")
    print(f'当前时间:{D}日{H}点{M}分')
    if H == '09':    ########### 修改此行数字09(代表09点)更改时间 00 01 02 ... 23 ########### 
        cmd_0 = 'bash ./trojan.sh'
        a=os.system(cmd_0)
        print('trojan执行成功...')
        # time.sleep(20)
    time.sleep(60*60)
    print(f'当前时间:{D}日{H}点{M}分')

