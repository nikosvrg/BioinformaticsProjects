
input="GGGCCCCCCCTTAAAAAAAAAAACCCCCCCCCCCCTTGG"
list1=list(input)
list2=[]
i=0
ACount=0
CCount=0

k=True

#Gia tous anadiplasiasmous xrhsimoipoisame counters wste na kalyptontai oi periorismoi.
#Periorismoi: poluA:mhkos 1 ews 5
#             poluC:mhkos 1 ews 10


while k:
    if list1[0]==list1[1] and list1[0]=='A' and ACount<5:
       del list1[1]
       ACount=ACount+1


    elif list1[0]==list1[1] and list1[0]=='A' and ACount==5:

        list2.append(list1[0])
        ACount = 0


    elif list1[0]==list1[1] and list1[0]=='C' and CCount<10:
       del list1[1]
       CCount=CCount+1


    elif list1[0]==list1[1] and list1[0]=='C' and CCount==10:

        list2.append(list1[0])
        CCount = 0

    elif list1[0] == list1[1] and list1[0] == 'G':
        del list1[1]


    elif list1[0] == list1[1] and list1[0] == 'T':
            del list1[1]


#diaforetiko gramma

    elif list1[0]!=list1[1]:
         list2.append(list1[0])
         del list1[0]
         ACount=0
         CCount=0


#telos tou while otan h lista exei 1 gramma kai prosthetetai sto telos ths listas mas.

    if len(list1)==1:
        list2.append(list1[0])
        del list1[0]
        k = False




a = ''.join(list2)

print ("H allhlouxia " +input+ "  apotelei molusmenh ekdosh ths " +a)


