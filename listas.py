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
