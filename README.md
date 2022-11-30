# trojan_timing
trojan定时更新端口，按照日期更新端口，解决封端口的问题

# 使用


> 下载本项目到服务器
> 
> apt-get install python3
> 
> 或者 yum install python3
> 
> cd ./task
> 
> nohup python3 -u trojan_test.py > trojan.log &


# 说明

每天早上9点更新端口

也可以自行设置端口更新

> cd ./task
> 
> vim trojan.py
> 
> 更改时间
