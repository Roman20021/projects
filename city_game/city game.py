import list_check
import chert
import сheck_city
import сheck_city1
kit = []
k = 0
b = []
c = []
p = 0
while p == 0:
    if k < 2:        
        k = k + 1
    else:
        k = k - 1
    print(str(k), 'player:')
    cit = input()  
    cit = chert.chert(cit)
    cit = list_check.list_check(cit)
    cit = сheck_city1.сheck_city1(cit, kit) 
    if c == []:
        b.append(cit[0])
        c.append(b)  
        b = []
    for i in range(len(cit)):
        b.append(cit[i])
    c.append(b)
    b =[]
    сheck_city.сheck_city(cit, c)
    kit.append(cit)    