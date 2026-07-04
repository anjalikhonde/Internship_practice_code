num=int(input("Enter any number:"))
fno=0
sno=1
#print(fno)
#print(sno)
for i in range(2,num):
    tno=fno+sno
    print(tno)
    fno=sno
    sno=tno
