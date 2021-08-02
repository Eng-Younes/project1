"""  المهمة الاولى """
x = 7
y = x/3
z = x == 7
s = "Hello python programmer!"
print(type(x))
print(type(y))
print(type(z))
print(type(s))


""" المهمة الثانية"""

quantity = 2
price = 10.5
text = "I want to pay {} riyals for {} pieces of this item.".format(price, quantity)
print(text)


"""" المهمة الثالثة"""

def bigger_than_10(x):
    if x > 10:
        print (x)
    else:
        print(10)
    
bigger_than_10(19)

""" المهمة الرابعة """

fruites = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruites[5:])
for c , value in enumerate(fruites,1):
    print(c,value)
    

"""المهمة الخامسة """

colors = {"blue": "0000FF","green": "00FF00","yellow": "FFFF00","red": "FF0000","white": "unknown"}
colors["black"] = "000000"
colors["white"] = "FFFFFF"
 

def exchange_values(lista):  
    lista = [colors[items] for items in lista]
    print(lista)
lista = ['blue', 'white', 'black', 'yellow', 'green', 'red']
exchange_values(lista)








