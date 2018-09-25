from datetime import datetime
for i in range(int(input())):
    s1=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    s2=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    print (int(abs((s1-s2).total_seconds())))
