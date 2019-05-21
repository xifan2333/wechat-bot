#coding=utf-8
import datetime
import time
import itchat

itchat.auto_login()
groups  = itchat.get_chatrooms(update=True)
target_group_name=""

for g in groups:
     if "想发送的群名" in g["NickName"]:
         target_group_name = g["UserName"]
         print("群id：",target_group_name,)
send_times = ["09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00"]
while True:
    time.sleep(60)
    now_time = time.strftime("%H:%M",time.localtime(time.time()))
    for i in range(0,len(send_times)):
        if now_time == send_times[i]:
            msg = "大家好，我是本群的“提醒喝水小助手”，这是今天的第{}轮。希望此刻看到消息的人可以和我一起来一杯水。一小时后的我继续提醒大家喝水。和我一起成为一天八杯水的人吧！".format(i)
            itchat.send_msg(msg,target_group_name)
            print("{}第{}次提醒成功".format(send_times[i],i+1))
