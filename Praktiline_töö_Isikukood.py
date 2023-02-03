from pickle import INT
from re import M
from tkinter import Y


while True:
    ikood=input("Sisesta isikukood: ")
    if len(ikood)!=11:
        print("Liiga pikk või lühike isikukood")
    else:
        print("isikukoodi kontrol")
        ik_list=list(ikood)
        print(ik_list[0])
        sl=int(ik_list[0])
        if sl not in [1,2,3,4,5,6]:
            print("Esineme sümbov ei ole õige")
        else:
            print("Elimene sümbol on õige")
            y=(ik_list[1]+ik_list[2])
            m=(ik_list[3]+ik_list[4])
            d=(ik_list[5]+ik_list[6])
            if (m<1 or m>13) and (d<1 or d>31) and (int(d)<1 or int(d)<31):
                print("Sünnipäev ei saa luua")
            else:
                if sl==1 or sl==2:
                    yy="18"
                elif sl==3 or sl==4:
                    yy="19"
                else:
                    yy=="20"
                    spaev=d+"."+m+"."+yy+y
                    print(f"sünnipäev on {spaev}")
                    print(ik_list[-1])
                
