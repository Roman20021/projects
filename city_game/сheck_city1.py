import list_check
import chert
def сheck_city1(city,c):
    status = 0
    while status == 0:
        if  city in c:
            print('this city name was used, please write name city again')           
            city = input()
            city = chert.chert(city)
            city = list_check.list_check(city)
        else:
            status = 1 
    return city