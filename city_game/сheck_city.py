import list_check
import chert
def сheck_city(city, b):
    status = 0
    while status == 0:
        if b[-2][-1] != b[-1][0]:
            print("please read the game rules for playing cities and write name city again")
            del b[-1] 
            city = input()
            city = chert.chert(city)
            j = list_check.list_check(city)
            b.append(j)
        else:
            status = 1
            return city