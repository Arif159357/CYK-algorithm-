Name = Arif
ID = 1611041


def UpPart(a,b,dic):
    c = []
    for i in a:
        for j in b:
            third = i + j
            for x in dic:
                if third in dic[x]:
                   c.append(x)
    
    return c              
         

size = input("How many Varable : ")

dic = {}
for i in range(int(size)):
    dic[input("what is "+str(i+1)+" the variables : ")] = []

lenght = input("How many connection : ")

for i in range(int(lenght)):
    w = input("Varaiable and out going with space : ")
    gam = w.split(" ") 
    Var = gam[0]
    Ter = gam[1]
    if Var in dic:
        dic[Var].append(Ter)
        print(dic)

string = input("give me a String : ")
Len = len(string)
CYK = [[0 for x in range(len(string))] for y in range(len(string))]
for i in range(len(string)):
     for j in range(len(string)):
          CYK[i][j] = []

for i in range(len(string)):
    for j in range(len(string)):
        if i == j:
           for k in dic: 
               if string[i] in dic[k]:
                   CYK[i][j].append(k)

for i in range(1,len(CYK)):
    for j in range(i,len(CYK)):
        for k in range(j-i,j):
          add = UpPart(CYK[j-i][k],CYK[k+1][j],dic)
          for m in add:
              if m not in CYK[j-i][j]:
                  CYK[j-i][j].append(m)


final_index = CYK[0][Len-1]
ks = list(dic)          

bool = False
for i in final_index:
    if i == ks[0]:
        print("String can be generated")
        bool = True
        break
    else:
        print("String can not be generated")
        
for i in CYK:
    print(i)    

                    