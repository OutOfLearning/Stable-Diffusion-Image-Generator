'''
def greet(name,age):
    print(f"Hello, {name} your age is {age}.")
greet("vamsi",24)
'''
'''
def greet():
    print(f"Hello,Vamsi!")
greet()
'''
'''''
def greet(name="guest"):
    print(f"Hello, {name}!")
greet()
greet("Vamsi")
'''
'''''
def add(a,b):
    return a+b
result=add(2,7)
print(result)
'''
def greet(*names):
    for name in names:
        print(f"Hello, {name}!")
greet("Vamsi","Krishna","Prasad")

def introduce(**person):
    for key,value in person.items():
        print(f"{key},{value}")
introduce(name="Vamsi",age=25,Profession="Developer")