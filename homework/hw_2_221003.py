# begin: read what user want!

def begin():
    want=input("write what you want: ")
    return want

def changeindex(list):
    Cstr=[]
    Rlist=[]
    str(list).remove("'","[","]")
    str.sort(".")
    str.sort(",")
    Cstr[0]=str[0]
    Cstr[1]=str[1]
    
    
    Rlist.append(Cstr[0])
    Rlist.append(Cstr[1])
    
    return Rlist

#making dictionary
def makingDic(str):
    dic={}
    #str should be divided item by item
    #1 replace \n to ,
    str2=str.replace("\n",",")
    #2 use split(",")
    lKBO=str2.split(",")
    
    for i in range(15):
        dic[lKBO[i%15]]=[]
    
    for i in range(len(lKBO)-15):
        dic[lKBO[i%15]].append((lKBO[i+15]))  #lKBO 0~14 will be the key

    return dic

def Case2inp(keylist,kboplayer):
    nameitem=[]
    
    for i in range(1,len(keylist)):
        for j in range(len(kboplayer)):
            nameitem.append(kboplayer[j]+" "+keylist[i])
    
    return nameitem

# input player Case1
def case1(list,want):

    c1list=list.splitlines()

    for i in range(len(c1list)):
        if(want in c1list[i]):
         print(c1list[i])
#   print player name and items
#   find player in separated list and print name and items by using list

#input nameitem
def case2(want,kbodic):
    print()
    divwant=want.split(" ")
    indexnum=list(kbodic["선수명"]).index(divwant[0])
    item=list(kbodic[divwant[1]])[indexnum]
    
    print(divwant[0]+" "+item)

def case3(want,kbodic):
    wlist=kbodic[want]
    plist=kbodic["선수명"]
    
    wplist=[]
    for i in range(len(wlist)):
        wplist.append(wlist[i]+" "+plist[i])
    
    wplist.sort()

    print(wplist)


#main
Kbofile=open("hw2.csv","r",encoding = 'UTF-8-sig')  #read csvfile
allKbo=Kbofile.read()                               #copy hw2.csv to allkbo.str
Kbofile.close()

# make dictionary for dividing cases
kbodic=makingDic(allKbo) 
keylist=list(kbodic.keys())

#to get case2 input
nameitem=Case2inp(keylist,kbodic["선수명"])

want=begin()

if(want in kbodic["선수명"]):   #want in key(name) 
    case1(allKbo,want)
elif(want in nameitem):         #want in key(name)+key(else)
    case2(want,kbodic)
elif(want in keylist):  #want in key but name
    case3(want,kbodic)
else:   #wrong input
    print("wrong input !!")