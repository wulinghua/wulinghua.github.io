# -*- coding: cp936 -*-
import random,easygui
secret=random.randint(1,99)
guess=0
tries=0
easygui.msgbox("""�������Ǵ�ţ������һ���Ų���
���������Ǵ�1��99������һ�����֡��Ҹ���6�λ���ȥ�¡�""")

while guess!=secret and tries<6:
    guess=easygui.integerbox("��¼�������")
    if not guess:break
    if guess<secret:
        easygui.msgbox(str(guess)+"����̫С�����������")
    elif guess>secret:
        easygui.msgbox(str(guess)+"����̫���㻹�Ǹ�����")
    tries=tries+1

if guess==secret:
    easygui.msgbox("�������������������Ų������룡")
else:
    easygui.msgbox("һ��Ҳû���У��Ų��Ҿ�������ˣ�������")

    

                       
