#declaracion de variables
lista_test_2=list()
lista_test=[]
#asignacion de variables
lista_str=["hola", "mundo","como","estas"] #lista de strings 
lista_numero=[1,2,3,4,5,6] #lista de numeros
lista_float=[1.2,1.3,1.5,2.4]#lista de flotantes
lista_bool=[True,False,False,True]#valores boolaneos

lista_mx=[lista_str,lista_numero,lista_numero] #lista con listas anidadas
lista_mx2=["hola",159,1.28,True] #lista de todos los tipos de datos

print(len(lista_mx2)) #indica la longitud de la lista
print(type(lista_mx2)) #indica si es una lista, tupla, etc...

#indices
print(lista_mx[-1]) #imprime el ultimo elemento de la lista

print(lista_str[1:3]) #imprimimos los randos de el primer numero hasta el anterior del ultimo (1:n-1)--> (1:3) = rango 1,2

print(listas_numero[0::2]) #imprime los numeros desde donde se especifica en rango de los que se indica(trae el dato uno de 2 en 2)
print(listas_numero[::2]) #imprime todos los datos de 2 en 2 (depende el salto del ultimo numero)