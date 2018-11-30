from random import random
import timeit
from pip._vendor.distlib.compat import raw_input
from _overlapped import NULL
from Tools.demo import vector

class MetodosOrdenamiento:
    
    aux = 0;
    
    def ordenamientoBurbuja1(self, vector):
        
        m = MetodosOrdenamiento
        
        contRecorrido=0 
        contComparaciones=0
        contIntercambios=0
        
        for i in range(2, len(vector)+1):
            for j in range(0, len(vector)-i+1):
                
                contComparaciones = contComparaciones + 1
                if(vector[j] > vector[j+1]):
                    aux = vector[j]
                    vector[j] = vector[j+1]
                    vector[j+1] = aux
                    contIntercambios = contIntercambios + 1
                
                contRecorrido = contRecorrido + 1
         
        m.mostrarVector(None, vector)
        tiempoFinal = timeit.timeit()
        m.mostrarDatosEficiencia(None, contRecorrido, contIntercambios, contComparaciones, tiempoFinal)
        
    def ordenamientoBurbuja2(self, vector):
        
        m = MetodosOrdenamiento
        
        contRecorrido2=0 
        contComparaciones2=0 
        contIntercambios2=0
        
        i=1
        ordenado = False
        
        while( (i < len(vector)) and (ordenado == False) ):
            i=i+1
            ordenado=True
            for j in range(0, len(vector)-i +1):
                contComparaciones2 = contComparaciones2 + 1
                if(vector[j] > vector[j+1]):
                    ordenado = False
                    aux = vector[j]
                    vector[j] = vector[j+1]
                    vector[j+1] = aux
                    contIntercambios2 = contIntercambios2 + 1
                
                contRecorrido2 = contRecorrido2 + 1
            
        m.mostrarVector(None, vector)
        tiempoFinal = timeit.timeit()
        m.mostrarDatosEficiencia(None, contRecorrido2, contIntercambios2, contComparaciones2, tiempoFinal)
    
    def ordenamientoBurbuja3(self, vector):
        
        m = MetodosOrdenamiento
        
        contRecorrido3=0 
        contComparaciones3=0
        contIntercambios3=0
        
        i=1
        ordenado = False;
        
        while( (i < len(vector)) and (ordenado == True) ):
            i=i+1
            ordenado = True
            
            for j in range(0, len(vector)-1):
                contComparaciones3 = contComparaciones3 + 1
                if(vector[j] >= vector[j+1]):
                    contIntercambios3 = contIntercambios3 + 1
                    #ordenado = False
                    aux = vector[j]
                    vector[j] = vector[j+1]
                    vector[j+1] = aux
                
                contRecorrido3 = contRecorrido3 + 1
            
        m.mostrarVector(None, vector)
        tiempoFinal = timeit.timeit()
        m.mostrarDatosEficiencia(None, contRecorrido3, contIntercambios3, contComparaciones3, tiempoFinal)
        
    

     


#=====================================================================================================================================
#=====================================================================================================================================

    def ordenamientoPorSeleccion(self, vector):
        
        m = MetodosOrdenamiento
        
        contRecorrido4=0
        contComparaciones4=0
        contIntercambios4=0
        
        for i in range(len(vector)-1, 0, -1):
            mayor = 0
            for j in range(1, i+1):
                contComparaciones4 = contComparaciones4 + 1 
                if(vector[j] > vector[mayor]):
                    mayor = j
                
            contRecorrido4 = contRecorrido4 + 1
            
            aux = vector[i]
            vector[i] = vector[mayor]
            vector[mayor] = aux
            contIntercambios4 = contIntercambios4 + 1
        
        m.mostrarVector(None, vector)
        tiempoFinal = timeit.timeit()
        m.mostrarDatosEficiencia(None, contRecorrido4, contIntercambios4, contComparaciones4, tiempoFinal)

    def ordenamientoPorInsercion(self, vector):
        
        m = MetodosOrdenamiento
        
        contRecorrido5=0
        contComparaciones5=0
        contIntercambios5=0
        
        for i in range(1, len(vector)):
            valor = vector[i]
            j = i - 1
            while(j >= 0):
                contComparaciones5 = contComparaciones5 + 1
                if(valor < vector[j]):
                    vector[j+1] = vector[j]
                    vector[j] = valor
                    j = j-1
                    contIntercambios5 = contIntercambios5 + 1
                else:
                    break
            contRecorrido5 = contRecorrido5 + 1    
            
        m.mostrarVector(None, vector)
        tiempoFinal = timeit.timeit()
        m.mostrarDatosEficiencia(None, contRecorrido5, contIntercambios5, contComparaciones5, tiempoFinal)
    
    def ordenamientoShellSort(self, vector):
        
        m = MetodosOrdenamiento
        
        contRecorrido6 = 0
        contComparaciones6 = 0
        contIntercambios6 = 0
        
        
        n =  len(vector)
        brecha = n/2
    
        while (brecha >  0):
            for i in range (int(brecha), n):
                val = vector[i]
                j = i
                contComparaciones6+=1
    
                while( (j >= int(brecha)) and (vector[j-int(brecha)] > val) ):
                    vector[j] = vector[j - int(brecha)]
                    j -= int(brecha)
                    contRecorrido6 += 1
    
                vector[j] = val
                contIntercambios6+=1
    
            brecha /=  2
        
        m.mostrarVector(None, vector)
        tiempoFinal = timeit.timeit()
        m.mostrarDatosEficiencia(None, contRecorrido6, contIntercambios6, contComparaciones6, tiempoFinal)
    
    def particion(self, lista, izq, der):
        
        pivote = lista[der]
        indice = izq
    
        for i in range(izq, der):
            
            if lista[i] <= pivote:
                lista[indice], lista[i] = lista[i], lista[indice]
                indice += 1
    
        lista[indice], lista[der] = lista[der], lista[indice]
        return indice
        
    def ordenamientoQuickSort(self, vector, izq, der):
        
        m = MetodosOrdenamiento
        
        if izq < der:
            pivote_indice = m.particion(None, vector, izq, der)
            m.ordenamientoQuickSort(None, vector, izq, pivote_indice-1)
            m.ordenamientoQuickSort(None, vector, pivote_indice+1, der)
        
        return vector

    def counting_sort(self, arr, max_value, get_index):
        
        counts = [0] * max_value
    
        # Counting - O(n)
        for a in arr:
            counts[get_index(a)] += 1
      
        # Accumulating - O(k)
        for i, c in enumerate(counts):
            if i == 0:
                continue
            else:
                counts[i] += counts[i-1]
    
        # Calculating start index - O(k)
        for i, c in enumerate(counts[:-1]):
            if i == 0:
                counts[i] = 0
            counts[i+1] = c
    
        ret = [None] * len(arr)
        # Sorting - O(n)
        for a in arr:
            index = counts[get_index(a)]
            ret[index] = a
            counts[get_index(a)] += 1
      
        return ret

    def get_digit(self, n, d):
        for i in range(d-1):
            n //= 10
        return n % 10

    def get_num_difit(self, n):
        i = 0
        while n > 0:
            n //= 10
            i += 1
        return i

    def ordenamientoRadixSort(self, arr, max_value):
        
        m = MetodosOrdenamiento
            
        num_digits = m.get_num_difit(None, max_value)
        # O(k(n+k))
        for d in range(num_digits):
            # Counting sort takes O(n+k)
            arr = m.counting_sort(None, arr, max_value, lambda a: m.get_digit(None, a, d+1))
        return arr
    
    def mostrarVector(self, vector):
        
        contador = 0
        
        for i in range(0, len(vector)):
            if(contador == 15):
                print("["+str(vector[i])+"] -- ")
                contador=0
            else:
                print("["+str(vector[i])+"] -- ", end=' ')
            
            contador = contador + 1
        
        print("\n")
    
    def mostrarDatosEficiencia(self, recorrido, intercambio, comparacion, tiempoFinal):
        
        print("")
        print("================ Datos de eficiencia del algoritmo. ================")
        print()
        print("RECORRIDOS O PASADAS: "+str(recorrido))
        print("COMPARACIONES: "+str(comparacion))
        print("INTERCAMBIOS: "+str(intercambio))
        print("TIEMPO DE EJECUCION: "+str(tiempoFinal)+" s")
        print("")
        
    def vector1000(self):
        vector = []
        numeroAleatorio = 0
        for i in range(0, 1000):
            numeroAleatorio =  (int)(random() * 100) + 1
            vector.insert(i, numeroAleatorio)
        
        return vector;
    
    def vector10000(self):
        vector = []
        numeroAleatorio = 0
        for i in range(0, 10000):
            numeroAleatorio =  (int)(random() * 100) + 1
            vector.insert(i, numeroAleatorio)
        
        return vector;
    
    def vector100000(self):
        vector = []
        numeroAleatorio = 0
        for i in range(0, 100000):
            numeroAleatorio =  (int)(random() * 100) + 1
            vector.insert(i, numeroAleatorio)
        
        return vector;
    
    def vector1000000(self):
        vector = []
        numeroAleatorio = 0
        for i in range(0, 1000000):
            numeroAleatorio =  (int)(random() * 100) + 1
            vector.insert(i, numeroAleatorio)
        
        return vector;

mo = MetodosOrdenamiento

lista = [6, 4, 1, 10, 5, 9, 7, 2, 8, 3]

#mo.mostrarVector(None, mo.vector1000(None).copy())
#mo.mostrarVector(None, lista)

arreglo1 = mo.vector1000(None)
arreglo2 = mo.vector10000(None)
arreglo3 = mo.vector100000(None)
arreglo4 = mo.vector1000000(None)


opcion = 0

while(opcion != 10):
    
    print("\n                          M E N U")
    print()
    print("1) Ordenamiento Burbuja.")
    print("2) Ordenamiento Por Seleccion.")
    print("3) Ordenamiento Por Insercion.")
    print("4) Ordenamiento ShellSort.")
    print("5) Ordenamiento QuickSort.")
    print("6) Ordenamiento RadixSort. ")
    print("7) Ordenamiento Por Intercalacion de archivos.")
    print("8) Ordenamiento Mezcla Directa.")
    print("9) Ordenamiento Mezcla Natural.")
    print("10) Salir.")
    print()
    opcion = int(raw_input("Elija una opcion: "))
    
    if(opcion == 1):
        
        print()
        print("=========== ORDENAMIENTO CON BURBUJA 1 ===========")
        #mo.ordenamientoBurbuja1(None, lista)
        mo.ordenamientoBurbuja1(None, arreglo1.copy())
        mo.ordenamientoBurbuja1(None, arreglo2.copy())
        mo.ordenamientoBurbuja1(None, arreglo3.copy())
        mo.ordenamientoBurbuja1(None, arreglo4.copy())
        #mo.ordenamientoBurbuja1(None, lista)
                    
        print()
        print("---------------------------------------------------------------------------------")
        print()
                 
        print("=========== ORDENAMIENTO CON BURBUJA 2 ===========")
        mo.ordenamientoBurbuja2(None, arreglo1.copy())
        mo.ordenamientoBurbuja2(None, arreglo2.copy())
        mo.ordenamientoBurbuja2(None, arreglo3.copy())
        mo.ordenamientoBurbuja2(None, arreglo4.copy())
        #mo.ordenamientoBurbuja2(None, lista)
                
        print()
        print("---------------------------------------------------------------------------------")
        print()
                  
        print("=========== ORDENAMIENTO CON BURBUJA 3 ===========")   
        mo.ordenamientoBurbuja3(None, arreglo1.copy())
        mo.ordenamientoBurbuja3(None, arreglo2.copy())
        mo.ordenamientoBurbuja3(None, arreglo3.copy())
        mo.ordenamientoBurbuja3(None, arreglo4.copy())
        #mo.ordenamientoBurbuja3(None, lista)
                
        print()
        print("---------------------------------------------------------------------------------")
        print()
    elif(opcion == 2):
        
        print()
        print("---------------------------------------------------------------------------------")
        print()
                    
        print("=========== ORDENAMIENTO POR SELECCION ===========")  
        mo.ordenamientoPorSeleccion(None, arreglo1.copy())
        mo.ordenamientoPorSeleccion(None, arreglo2.copy())
        mo.ordenamientoPorSeleccion(None, arreglo3.copy())
        mo.ordenamientoPorSeleccion(None, arreglo4.copy())
        #mo.ordenamientoPorSeleccion(None, lista)
        
        print()
        print("---------------------------------------------------------------------------------")
        print()
        
    elif(opcion == 3):
        
        print()
        print("---------------------------------------------------------------------------------")
        print()
                
        print("=========== ORDENAMIENTO POR INSERCION ===========")
        mo.ordenamientoPorInsercion(None, arreglo1.copy())
        mo.ordenamientoPorInsercion(None, arreglo2.copy())
        mo.ordenamientoPorinsercion(None, arreglo3.copy())
        mo.ordenamientoPorInsercion(None, arreglo4.copy())
        #mo.ordenamientoPorInsercion(None, lista)
        
        print()
        print("---------------------------------------------------------------------------------")
        print()
    
    elif(opcion == 4):
        print()
        print("---------------------------------------------------------------------------------")
        print()
                
        print("=========== ORDENAMIENTO SHELLSORT ===========")
        mo.ordenamientoShellSort(None, arreglo1.copy())
        mo.ordenamientoShellSort(None, arreglo2.copy())
        mo.ordenamientoShellSort(None, arreglo3.copy())
        mo.ordenamientoShellSort(None, arreglo4.copy())
        
        print()
        print("---------------------------------------------------------------------------------")
        print()         
    
    elif(opcion == 5):
        print()
        print("---------------------------------------------------------------------------------")
        print()
                
        print("=========== ORDENAMIENTO QUICKSORT ===========")
        print(mo.ordenamientoQuickSort(None, arreglo1.copy(), 0, len(arreglo1.copy())-1))
        print(mo.ordenamientoQuickSort(None, arreglo2.copy(), 0, len(arreglo2.copy())-1))
        print(mo.ordenamientoQuickSort(None, arreglo3.copy(), 0, len(arreglo3.copy())-1))
        print(mo.ordenamientoQuickSort(None, arreglo4.copy(), 0, len(arreglo4.copy())-1))
        #mo.ordenamientoQuickSort(None, lista.copy())
        
        print()
        print("---------------------------------------------------------------------------------")
        print()
   
    elif(opcion == 6):
        print()
        print("---------------------------------------------------------------------------------")
        print()
                
        print("=========== ORDENAMIENTO RADIXSORT ===========")
        mo.mostrarVector(None, mo.ordenamientoRadixSort(None, arreglo1.copy(), len(arreglo1.copy())-1))
        mo.mostrarVector(None, mo.ordenamientoRadixSort(None, arreglo2.copy(), len(arreglo2.copy())-1))
        mo.mostrarVector(None, mo.ordenamientoRadixSort(None, arreglo3.copy(), len(arreglo3.copy())-1))
        mo.mostrarVector(None, mo.ordenamientoRadixSort(None, arreglo4.copy(), len(arreglo4.copy())-1))
        #mo.ordenamientoRadixSort(None, lista.copy())
        
        
        print()
        print("---------------------------------------------------------------------------------")
        print()                  
    elif(opcion == 7):
        print()
        print("---------------------------------------------------------------------------------")
        print()
                
        print("=========== INTERCALACION DE ARCHIVOS ===========")
        print()
        archivo3=open ("ArchivoSalida.txt", "w")
        archivo1=open("Archivo1.txt", "r")
        archivo2=open("Archivo2.txt", "r")
        repetir=True
          
        lineaArchivo1=archivo1.readline() 
        lineaArchivo2=archivo2.readline()
         
        
        '''Se realizan comparaciones mientras la bandera no cambie'''
        while(repetir):
            if(int(lineaArchivo1)<int(lineaArchivo2)):
                archivo3.write(lineaArchivo1)
                lineaArchivo1=archivo1.readline()
                if(lineaArchivo1==""):
                    archivo3.write("\n")
                    archivo3.write(lineaArchivo2)
                    lineaArchivo2=archivo2.readline()
                    while(lineaArchivo2!=""):
                        archivo3.write(lineaArchivo2)
                        lineaArchivo2=archivo2.readline()
                    repetir=False
            elif(int(lineaArchivo1)>int(lineaArchivo2)):
                archivo3.write(lineaArchivo2)
                lineaArchivo2=archivo2.readline()
                if(lineaArchivo2==""):
                    archivo3.write("\n")
                    archivo3.write(lineaArchivo1)
                    lineaArchivo1=archivo1.readline()
                    while(lineaArchivo1!=""):
                        archivo3.write(lineaArchivo1)
                        lineaArchivo1=archivo1.readline()
                    repetir=False
            else:
                archivo3.write(lineaArchivo1)
                archivo3.write(lineaArchivo2)
                lineaArchivo1=archivo1.readline()
                if(lineaArchivo1==""):
                    archivo3.write("\n")
                    archivo3.write(lineaArchivo2)
                    lineaArchivo2=archivo2.readline()
                    while(lineaArchivo2!=""):
                        archivo3.write(lineaArchivo2)
                        lineaArchivo2=archivo2.readline()
                    repetir=False
                lineaArchivo2=archivo2.readline()
                if(lineaArchivo2==""):
                    archivo3.write("\n")
                    archivo3.write(lineaArchivo1)
                    lineaArchivo1=archivo1.readline()
                    while(lineaArchivo1!=''):
                        archivo3.write(lineaArchivo1)
                        lineaArchivo1=archivo1.readline()
                    repetir=False
        archivo2.close
        archivo1.close
        print("Archivos combinados y ordenados correctamente")
        archivo3.close
    elif(opcion == 8):
        
        import random
        randfile = open("Random.txt", "w")
        
        start = int(input('Ingresa el limite inferior para el rango de numeros: '))
        end = int(input('Ingresa el limite superior para el rango de numeros: '))
        
        for i in range(int(input('Cuantos numeros desea generar?: '))):
            line = str(random.randint(start, end))
            randfile.write(line + '\n')
            print(line)
        
        randfile.close()
        
        # example of selection sort algorithm : needs modification
        
        def swap(a, i, j):
            (a[i], a[j]) = (a[j], a[i])
        
        def selectionSort(a):
            n = len(a)
            for startIndex in range(n):
                minIndex = startIndex
                for ind in range(startIndex+1, n):
                    if a[ind] < a[minIndex]:
                        minIndex = ind
                swap(a, startIndex, minIndex)
        
        lst = []
        with open("Random.txt", "r") as f:
            for line in f:
                lst.append(int(line.strip()))
        
        file = open("selectionSortResult","w")
        for x in lst:
            file.write(str(x)+"\n")
        file.close()

        def merge_sort(A):
            n = len(A)
            if n==1:
                return A
            mid = n//2   # floor division
            L = merge_sort(A[:mid])
            R = merge_sort(A[mid:])
            return merge(L,R)
        
        def merge(L,R):
            
            i = 0
            j = 0
            answer = []
            while i<len(L) and j<len(R):
                if L[i]<R[j]:
                    answer.append(L[i])
                    i += 1
                else:
                    answer.append(R[j])
                    j += 1
            if i<len(L):
                answer.extend(L[i:])
            if j<len(R):
                answer.extend(R[j:])
            return answer
        
        lst = []
        # opens and reads 'Random.txt'
        with open("Random.txt", "r") as f:
            for line in f:
                lst.append(int(line.strip()))
        
        # opens and writes to file 'mergeSortResult.txt'
        file = open("mergeSortResult","w")
        for x in lst:
            file.write(str(x)+"\n")
        # closes 'mergeSortResult.txt'
        file.close()
        print('Lista ordenada: ', lst)
    
    elif(opcion == 9):
        def mezclaNatural(arr): 
            if len(arr) >1: 
                mitad = len(arr)//2 
                aux1 = arr[:mitad]   
                aux2 = arr[mitad:] 
                mezclaNatural(aux1) 
                mezclaNatural(aux2)  
          
                i = j = k = 0
        
                while i < len(aux1) and j < len(aux2): 
                    if aux1[i] < aux2[j]: 
                        arr[k] = aux1[i] 
                        i+=1
                    else: 
                        arr[k] = aux2[j] 
                        j+=1
                    k+=1
                  
                while i < len(aux1): 
                    arr[k] = aux1[i] 
                    i+=1
                    k+=1
                  
                while j < len(aux2): 
                    arr[k] = aux2[j] 
                    j+=1
                    k+=1
    
        def mostrar(arr): 
            for i in range(len(arr)):         
                print(arr[i],end=" ") 
            print() 


        archivo1=open("Archivo1.txt", "r")
        lineaArchivo1=archivo1.readline() 
        arr=lineaArchivo1.split(",")
        archivo1.close
        mostrar(arr) 
        mezclaNatural(arr) 
        mostrar(arr) 
    
    elif(opcion == 0):
        print("S A L I E N D O . . .")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    