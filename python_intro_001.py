if 2 > 2: 
    print("It works!")
else:
    print("It doesn't work.")    
name = "Ronja"
if name == "Ola":
    print("Hey Ola!")
elif name == ("Ronja"):
    print("Hey Ronja!")
else:
    print("Hey anonymus!")    
volume = 58
if volume == 57:
    print(111)
    if 55 < volume < 60:
        print(333)     
elif 50 < volume < 60:
    print(222)    
    if 55 < volume < 60:
        print(444)       
volume = 57
if volume == 57:
    print(111)   
elif 50 < volume < 60:
    print(222)
elif 55 < volume < 60:
    print(222)
#Explanation
volume = 50
if volume < 20 or volume > 80:
    print("That's better!")
if volume < 20 or volume > 80:
    volume = 50
    print("That's better!")
