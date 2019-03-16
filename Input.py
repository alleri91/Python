

def wiek():
    
        print("Write your age")
        age = input()
        unt_100 = 100 - int(age)

        if unt_100 < 0:
            print('Zly wiek')
            
            

        else:            
            print('Your age is ' + age)
            
        
        x = ('until you will be 100 years old has left: ' + str(unt_100) + ' Years')
        return x
print('Write your name')
a = input()
x = wiek()

print(a +  " " + x)








