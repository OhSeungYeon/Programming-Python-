print("369게임")

for c in [str(x) for x in range(1,99+1)]:

    count = c.count('3') + c.count('6') + c.count('9') 

    if count:  
        
        print ('짝'*count)

    else :  

        print (c)