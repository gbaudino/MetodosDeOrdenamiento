from random import sample 
# Importamos un metodo de la biblioteca random para generar listas aleatorias

lista = range(100) # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria de largo 8 para cada Ordenamiento
vectorbs = sample(lista,8) 
vectorselect = sample(lista,8)
vectorins = sample(lista,8) 
vectorshell = sample(lista,8)
vectormerge = sample(lista,8)
vectorquick = sample(lista,8)
vectorheap = sample(lista,8)
vectorcomb = sample(lista,8)
vectorcocktail = sample(lista,8)


def bubblesort(vectorbs):
    """Esta función ordenara el vector que le pases como argumento
    con el metodo de Bubble Sort"""
    
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("----------------------------------------------------------------------")
    print("El vector a ordenar con bubble es:",vectorbs)
    
    n = 0 # Establecemos un contador del largo del vector
    
    for _ in vectorbs:
        n += 1 #Contamos la cantidad de caracteres dentro del vector
    
    for i in range(n-1): 
    # Le damos un rango n para que complete el proceso. 
        for j in range(0, n-i-1): 
            # Revisa la matriz de 0 hasta n-i-1
            if vectorbs[j] > vectorbs[j+1] :
                vectorbs[j], vectorbs[j+1] = vectorbs[j+1], vectorbs[j]
            # Se intercambian si el elemento encontrado es mayor 
            # Luego pasa al siguiente
            
    print ("El vector ordenado con bubble es: ", vectorbs)





def selectionsort(vectorselect):
    """Esta función ordenara el vector que le pases como argumento 
    con el metodo Selection Sort"""
    
    # Imprimimos la lista obtenida al principio (Desordenada)
    
    print("----------------------------------------------------------------------")
    print ("El vector a ordenar con selección es:",vectorselect)
    
    largo = 0 # Establecemos un contador del largo
    
    for _ in vectorselect:
        largo += 1 # Obtenemos el largo del vector
        
    for i in range(largo): 
      
        # Encontrar el minimo elemento de los restantes sin ordenar
        minimo = i 
        for j in range(i+1, largo): 
            if vectorselect[minimo] > vectorselect[j]: 
                minimo = j 
                
        # Cambiamos el elemento minimo encontrado con el primer elemento de la matriz
        vectorselect[i], vectorselect[minimo] = vectorselect[minimo], vectorselect[i]
        # Repetimos el proceso hasta terminar
    print("El vector ordenado con selección es: ",vectorselect)


def insertionsort(vectorins): 
    """Esta función ordenara el vector que le pases como argumento 
    con el metodo Insertion Sort"""
    
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("----------------------------------------------------------------------")
    print("El vector a ordenar con inserción es:", vectorins)
    
    largo = 0 # Establecemos un contador del largo
     
    for i in vectorins:
        largo += 1 # Obtenemos el largo del vector
    
    # Recorremos la lista de 1 hasta el largo del vector
    for i in range(1, largo): 
    
        elemento = vectorins[i] 
  
        # Movemos los elementos de vectorins[0...i-1], que son mayores que el elemento a una posición adelante de su posición actual
        j = i-1
        while j >= 0 and elemento < vectorins[j] : 
                vectorins[j+1] = vectorins[j] 
                j -= 1
        vectorins[j+1] = elemento 
    print("El vector ordenado con inserción es: ", vectorins)




def shellsort(vectorshell):
    
    """Esta función ordenara el vector que le pases como argumento 
    con el metodo Shell Sort"""
    
    print("----------------------------------------------------------------------")
    print("El vector a ordenar con shell es:", vectorshell)
    
    largo = 0
    
    for i in vectorshell:
        largo += 1
    
    distancia = largo // 2
    
     # Creamos un bucle según las distancias
    while distancia > 0:
        # Utilizamos el Insertionsort
        for i in range(distancia, largo):
            val = vectorshell[i]
            j = i
            while j >= distancia and vectorshell[j - distancia] > val:
                vectorshell[j] = vectorshell[j - distancia]
                j -= distancia
            vectorshell[j] = val
        distancia //= 2 # Acotamos la distancia nuevamente y continua el ciclo
    print("El vector ordenado con shell es: ", vectorshell)



def mergesort(vectormerge): 
    """Esta función ordenara el vector que le pases como argumento 
    con el metodo Merge Sort"""
    
    print("----------------------------------------------------------------------")
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar con merge es:", vectormerge)
    
    def merge(vectormerge):
           
        if len(vectormerge) >1: 
            medio = len(vectormerge)//2 # Buscamos el medio del vector
            
            # Lo dividimos en 2 partes 
            izq = vectormerge[:medio]  
            der = vectormerge[medio:]
            
            merge(izq) # Mismo procedimiento a la primer mitad
            merge(der) # Mismo procedimiento a la segunda mitad
            
            i = j = k = 0
            
            # Copiamos los datos a los vectores temporales izq[] y der[] 
            while i < len(izq) and j < len(der): 
                if izq[i] < der[j]: 
                    vectormerge[k] = izq[i] 
                    i+= 1
                else: 
                    vectormerge[k] = der[j] 
                    j+= 1
                k += 1
            
            # Nos fijamos si quedaron elementos en la lista
            # tanto derecha como izquierda 
            while i < len(izq): 
                vectormerge[k] = izq[i] 
                i+= 1
                k+= 1
            
            while j < len(der): 
                vectormerge[k] = der[j] 
                j+= 1
                k+= 1
    merge(vectormerge)
    print("El vector ordenado con merge es: ", vectormerge)
    
def quicksort(vectorquick, start = 0, end = len(vectorquick) - 1 ):
    """Esta función ordenara el vector que le pases como argumento 
    con el metodo Quick Sort"""
    print("----------------------------------------------------------------------")
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar con quick es:", vectorquick)
    
    def quick(vectorquick, start = 0, end = len(vectorquick) - 1):
        
        
        if start >= end:
            return

        def particion(vectorquick, start = 0, end = len(vectorquick) - 1):
            pivot = vectorquick[start]
            menor = start + 1
            mayor = end

            while True:
                # Si el valor actual es mayor que el pivot
                # está en el lugar correcto (lado derecho del pivot) y podemos 
                # movernos hacia la izquierda, al siguiente elemento.
                # También debemos asegurarnos de no haber superado el puntero bajo, ya que indica 
                # que ya hemos movido todos los elementos a su lado correcto del pivot
                while menor <= mayor and vectorquick[mayor] >= pivot:
                    mayor = mayor - 1

                # Proceso opuesto al anterior            
                while menor <= mayor and vectorquick[menor] <= pivot:
                    menor = menor + 1

                # Encontramos un valor sea mayor o menor y que este fuera del arreglo
                # ó menor es más grande que mayor, en cuyo caso salimos del ciclo
                if menor <= mayor:
                    vectorquick[menor], vectorquick[mayor] = vectorquick[mayor], vectorquick[menor]
                    # Continua el bucle
                else:
                    # Salimos del bucle
                    break

            vectorquick[start], vectorquick[mayor] = vectorquick[mayor], vectorquick[start]
            
            return mayor
        
        p = particion(vectorquick, start, end)
        quick(vectorquick, start, p-1)
        quick(vectorquick, p+1, end)
        
    quick(vectorquick)
    print("El vector ordenado con quick es:", vectorquick)
    
def heapsort(vectorheap):
    """Esta función ordenara el vector que le pases como argumento 
    con el metodo Heap Sort"""
    
    print("----------------------------------------------------------------------")
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar con heap es:", vectorheap)

    largo = 0 # Establecemos un contador del largo
        
    for _ in vectorheap:
        largo += 1 # Obtenemos el largo del vector

    # Para amontonar la subparte a partir de i. 
    # n es el tamaño del montón.
    def amontonar(vectorheap, n, i): 
        mas_largo = i # Tomamos i como el más grande 
        izq = 2 * i + 1      
        der = 2 * i + 2    
    
        
        if izq < n and vectorheap[i] < vectorheap[izq]: 
            mas_largo = izq 
    
        # Ver si existe la subparte de i correctamente y 
        # si es mayor que i
        if der < n and vectorheap[mas_largo] < vectorheap[der]: 
            mas_largo = der 
            
    
        if mas_largo != i: 
            vectorheap[i],vectorheap[mas_largo] = vectorheap[mas_largo],vectorheap[i]
            # Cambiar el origen, si es necesario
            # amontonar el origen. 
            amontonar(vectorheap, n, mas_largo)
            
    def heap(vectorheap):
        
        n = largo
        # Crear un montón maximo 
        for i in range(n//2 - 1, -1, -1): 
            amontonar(vectorheap, n, i) 
    
        # Extraer elementos uno a uno
        for i in range(n-1, 0, -1): 
            vectorheap[i], vectorheap[0] = vectorheap[0], vectorheap[i] 
            # Intercambio 
            amontonar(vectorheap, i, 0)
        
    heap(vectorheap)
    print("El vector ordenado con heap es:", vectorheap)
    
def combsort(vectorcomb):
    """Esta función ordenara el vector que le pases como argumento
    con el metodo de Comb Sort"""
    
    
    print("----------------------------------------------------------------------")
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar con comb es:",vectorcomb)
    
    largo = 0 # Establecemos un contador del largo del vector
    
    for _ in vectorcomb:
        largo += 1
    
    
    # Comenzamos con la diferencia o distancia igual al largo del vector
    diferencia = largo
    
    # Establecemos la variable que define si es necesario o no
    #  intercambiar los numeros que se están comparando
    cambiar = True
    
    while diferencia > 1 or cambiar:
        diferencia = max(1, int(diferencia / 1.25))  
        # La diferencia minima es 1
        # En cada iteración vamos bajando la diferencia
        cambiar = False
        for i in range(largo - diferencia):
            j = i+diferencia 
            # Ubicamos el número que está a la distancia x de i
            if vectorcomb[i] > vectorcomb[j]:
                vectorcomb[i], vectorcomb[j] = vectorcomb[j], vectorcomb[i]
                # Hacemos el intercambio de los numeros
                cambiar = True
    
    print("El vector ordenado con comb es: ",vectorcomb)

def cocktailsort(vectorcocktail):
    """Esta función ordenara el vector que le pases como argumento
    con el metodo de Cocktail Sort"""
    
    print("----------------------------------------------------------------------")
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar con cocktail es:",vectorcocktail)
    
    largo = 0 # Establecemos un contador del largo
    
    for _ in vectorcocktail:
        largo += 1 # Obtenemos el largo del vector
    
    for i in range(largo//2): # Comenzamos desde la mitad aprox
        cambiar = False 
        # Declaramos la variable que inidica si es necesario intercambiar o no 
        for j in range(1+i, largo-i):
            # Probar si los dos elementos están en el orden incorrecto
            if vectorcocktail[j] < vectorcocktail[j-1]:
                # Entonces ambos elementos cambian de lugar
                vectorcocktail[j], vectorcocktail[j-1] = vectorcocktail[j-1], vectorcocktail[j]
                cambiar = True
        # Si no ocurren cambios salimos del bucle
        if not cambiar:
            break
        cambiar = False
        for j in range(largo-i-1, i, -1):
            # Probar si los dos elementos están en el orden incorrecto
            if vectorcocktail[j] < vectorcocktail[j-1]:
                # Entonces ambos elementos cambian de lugar
                vectorcocktail[j], vectorcocktail[j-1] = vectorcocktail[j-1], vectorcocktail[j]
                cambiar = True
        if not cambiar:
            break
    print("El vector ordenado con cocktail es: ",vectorcocktail)
    print("----------------------------------------------------------------------")

bubblesort(vectorbs)
selectionsort(vectorselect)
insertionsort(vectorins)
shellsort(vectorshell)
mergesort(vectormerge)
quicksort(vectorquick)
heapsort(vectorheap)
combsort(vectorcomb)
cocktailsort(vectorcocktail)
