##tuplas 
##las tuplas no se pueden modificar y las listas si
#import pprint
#s=(1,) #si solo quiero especificar un dato dentro de la tupla tengo que poner coma (,) despues del elemento
#tupla1= ("hola", "Como", "estas")
#lista_resultados=list(tupla1[1:2]) #cargo la tupla en una lista, si en corchetes especifico el rango solo carga esos datos
#print(lista_resultados)

#d={1:"valo1",2:"valo2","b":["martillo","tamarindo"]}
#print(d.keys())
#print(d.values())
#d1={
#    "a":"zanahoria",
#    2:"limones",
#    "frutas":12,
#    "d2":d    
#    }

#entrada=input("dame una llave: ")
#pprint.pprint(d[entrada])

telefono={
    "phone_number1": "513-288-0764",
    "phone_number2": "199-396-3280",
    "phone_number3": "740-474-0662",
    "phone_number4": "929-675-8462",
    "phone_number5": "636-411-2432",
    "phone_number6": "763-833-0882"
    }
print(telefono['phone_number6'])
telefono['phone_number7']='266-939-9616'
