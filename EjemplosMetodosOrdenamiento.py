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
        
        contRecorrido7=0
        contComparaciones7=0
        contIntercambios7=0
        
        if izq < der:
            pivote_indice = m.particion(None, vector, izq, der)
            m.ordenamientoQuickSort(None, vector, izq, pivote_indice-1)
            m.ordenamientoQuickSort(None, vector, pivote_indice+1, der)
        
        tiempoFinal = timeit.timeit()
        return vector

    
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
        print(mo.ordenamientoQuickSort(None, mo.vector1000(None).copy(), 0, len(mo.vector1000(None).copy())-1))
        #mo.ordenamientoQuickSort(None, mo.vector10000(None).copy())
        #mo.ordenamientoQuickSort(None, mo.vector100000(None).copy())
        #mo.ordenamientoQuickSort(None, mo.vector1000000(None).copy())
        #mo.ordenamientoQuickSort(None, lista.copy())
        
        
        print()
        print("---------------------------------------------------------------------------------")
        print()
   
    elif(opcion == 6):
        print()
        print("---------------------------------------------------------------------------------")
        print()
                
        print("=========== ORDENAMIENTO RADIXSORT ===========")
        #mo.ordenamientoRadixSort(None, mo.vector1000(None).copy())
        #mo.ordenamientoRadixSort(None, mo.vector10000(None).copy())
        #mo.ordenamientoRadixSort(None, mo.vector100000(None).copy())
        #mo.ordenamientoRadixSort(None, mo.vector1000000(None).copy())
        mo.ordenamientoRadixSort(None, lista.copy())
        
        
        print()
        print("---------------------------------------------------------------------------------")
        print()                  
    
    elif(opcion == 0):
        print("S A L I E N D O . . .")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    