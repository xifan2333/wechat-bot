from wxpy import *
add_member_helper = Bot(True)
group_name = input("请输入目标群：")
password = input("请输入口令：")
group = add_member_helper.groups().search(group_name)
print("目标群为：{}".format(group))
print("加群口令为：{}".format(password))


@add_member_helper.register(msg_types=TEXT)
def add_into_chatroom(msg):
        if msg.text == password:
                group[0].add_members(msg.sender, use_invitation=True)


add_member_helper.join()
