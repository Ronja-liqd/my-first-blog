def hi():
    print('Hi there!')
    print('How are you?')
#hi()
def hi(name):
    print("Hi " + name + "!")
    if name == "Ola":
        print("Hi Ola!")
    elif name == "Sonja":
        print("Hi Sonja")
    else:
        print("Hi anonymus!")
    print("Goodbye " + name + "!")    
#hi("Ola")
#hi("liquids")

def hi(name):
    print("Hi " + name + "!")
girls = ["Rachel", "Monica", "Phoebe", "Ola", "You"]
for nbla in ["Rachel"]:
    hi(nbla)
    print("Next girl")
for i in range(1, 6):
    print(i)