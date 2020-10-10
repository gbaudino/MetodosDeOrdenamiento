from random import sample # Importamos un metodo de la biblioteca random para generar listas aleatorias
lista = range(100) # Creamos la lista base con números del 1 al 100

vectorbs = sample(lista,5) # Creamos una lista aleatoria con la func sample (contiene 5 elementos aleatorios de la lista base)
vectorselect = sample(lista,10) # Creamos una lista aleatoria con la func sample (contiene 10 elementos aleatorios de la lista base)
vectorins = sample(lista,15) # Creamos una lista aleatoria con la func sample (contiene 15 elementos aleatorios de la lista base)
vectorshell = sample(lista,20) # Creamos una lista aleatoria con la func sample (contiene 20 elementos aleatorios de la lista base)



def bubblesort(vectorbs):
    """Esta función ordenara el vector que le pases como argumento con el metodo de Bubble Sort"""
    
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar es: ",vectorbs)
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
    print ("El vector ordenado es: ", vectorbs)



def selectionsort(vectorselect):
    """Esta función ordenara el vector que le pases como argumento con el metodo Selection Sort"""
    # Imprimimos la lista obtenida al principio (Desordenada)
    print ("El vector a ordenar es: ",vectorselect)
    
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
    print("El vector ordenado es: ",vectorselect)

def insertionsort(vectorins): 
    """Esta función ordenara el vector que le pases como argumento con el metodo Insertion Sort"""
    
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar es: ", vectorins)
    
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
    print("El vector ordenado es: ", vectorins)

def shellsort(vectorshell):
    
    """Esta función ordenara el vector que le pases como argumento con el metodo Shell Sort"""
    
    print("El vector a ordenar es: ", vectorshell)
    
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
    print("El vector ordenado es: ", vectorshell)

bubblesort(vectorbs)
selectionsort(vectorselect)
insertionsort(vectorins)
shellsort(vectorshell)