# -*- coding: cp936 -*-
import random,easygui
secret=random.randint(1,99)
guess=0
tries=0
easygui.msgbox("""猪宝！我是大富牛，我有一笔遗产！
它的密码是从1到99的任意一个数字。我给你6次机会去猜。""")

while guess!=secret and tries<6:
    guess=easygui.integerbox("你猜几，猪宝？")
    if not guess:break
    if guess<secret:
        easygui.msgbox(str(guess)+"数字太小，你这个笨猪！")
    elif guess>secret:
        easygui.msgbox(str(guess)+"数字太大，你还是个笨猪！")
    tries=tries+1

if guess==secret:
    easygui.msgbox("猪宝！你真聪明，这就是遗产的密码！")
else:
    easygui.msgbox("一次也没猜中！遗产我捐给国家了，宝宝！")

    

                       
