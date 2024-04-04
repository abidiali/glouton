'''
dicPC={"HP":  11  , "Acer":  7  , "Lenovo":  17  , "Del":  23}
dicPhone={"Sumsung":   22  , "Iphone":  9  ,  "Other":  13  }
dicTablette =  {"Sumsung":   15  , "Other":  13}
for i in dicTablette:
    dicPC[i]=dicTablette[i]
for i in dicPhone.keys():
    if i in dicPC.keys():
        dicPC[i]=dicPC[i]+dicPhone[i]
    else:
        dicPC[i]=dicPhone[i]
print(dicPC)

etudiants = {"etudiant_1" : 13 , "etudiant_2" : 17 , "etudiant_3" : 9 , "etudiant_4" : 15 , "etudiant_5"   :  8  , "etudiant_6"  :  14  , "etudiant_7"  :  16  , "etudiant_8"   : 12  , "etudiant_9"   :  13  , "etudiant_10"   : 15  , "etudiant_11"  :  14  , "etudiant_112"   :  9  , "etudiant_13"   : 10  , "etudiant_14"  :  12  , "etudiant_15"   :  13  , "etudiant_16"  :  7  , "etudiant_17"   : 12  , "etudiant_18"  :  15  , "etudiant_19"   :  9  , "etudiant_20"  :  17 }
etudiantAdmis={}
etudiantNonAdmis={}
for i,j in etudiants.items():
    if j> 10:
        etudiantAdmis[i]=j
    else:
        etudiantNonAdmis[i]=j
        
print(etudiantAdmis)
print(etudiantNonAdmis)

def test(n):
    dic={}
    i=1
    while i<=n:
        dic[i]=i*i
        i+=1
    return dic
print(test(7))


def test1(s):
    dic={}
    for i in s:
        if i in dic:
            dic[i]=dic[i]+1
        else:
            dic[i]=1
    return dic
print(test1("kakati"))

def test2(s):
    dic={}
    for i in range(len(s)):
        dic[s[i]]=i
    return dic
print(test2("sader"))

def test3():
    L=[]
    dic={}
    for i in range(10):
        x=int(input("entrer un nombre"))
        L.append(x)
    for i in L:
        dic[i]=[j for j in range(1,i) if i%j==0]
    return dic
print(test3())
'''
dic={"personne1":("x", 10, "Tunis")}
t={"personne2":("y",12,"Sousse")}
dic.update(t)
print(dic)
for i in dic.items():
    print(i)
    
villes=[]
for i in dic.values():
    print(i[2])




