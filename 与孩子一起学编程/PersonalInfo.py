import datetime
sName=str(input("����������������"))
s=int(input("���������ĳ�����ݣ�"))
age=datetime.date.today().year-s
print("���ã�{0}����{1}�ꡣ".format(sName,age))
