from random import random
import timeit
from pip._vendor.distlib.compat import raw_input
from _overlapped import NULL

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
        '''
        int contRecorrido6=0, contComparaciones6=0, contIntercambios6=0;
        long tiempoFinal=0;
        
        int salto, aux, i;
        boolean cambios;
        
        long tiempoInicial = System.nanoTime();
        
        for(salto=numeros.length/2; salto != 0; salto/=2) {
            cambios = true;
            while(cambios) {
                cambios = false;
                for(i = salto; i<numeros.length; i++) {
                    contComparaciones6++;
                    if(numeros[i-salto] > numeros[i]) {
                        aux = numeros[i];
                        numeros[i] = numeros[i-salto];
                        numeros[i-salto] = aux;
                        cambios = true;
                        contIntercambios6++;
                    }
                    contRecorrido6++;
                }
            }
        }
        
        mostrarVector(numeros);
        tiempoFinal = System.nanoTime() - tiempoInicial;
        
        mostrarDatosEficiencia(contRecorrido6, contComparaciones6, contIntercambios6, tiempoFinal);
         ''' 

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

mo.mostrarVector(None, mo.vector1000(None).copy())
#mo.mostrarVector(None, lista)

opcion = 0

while(opcion != 10):
    
    print("\n                          M E N U")
    print()
    print("1) Ordenamiento Burbuja.")
    print("2) Ordenamiento Por Seleccion.")
    print("3) Ordenamiento Por Insercion.")
    print("4) Ordenamiento ShellSort")
    print("10) Salir.")
    print()
    opcion = int(raw_input("Elija una opcion: "))
    
    if(opcion == 1):
        
        print()
        print("=========== ORDENAMIENTO CON BURBUJA 1 ===========")
        #mo.ordenamientoBurbuja1(None, lista)
        mo.ordenamientoBurbuja1(None, mo.vector1000(None).copy())
        mo.ordenamientoBurbuja1(None, mo.vector10000(None).copy())
        mo.ordenamientoBurbuja1(None, mo.vector100000(None).copy())
        mo.ordenamientoBurbuja1(None, mo.vector1000000().copy())
        #mo.ordenamientoBurbuja1(None, lista)
                    
        print()
        print("---------------------------------------------------------------------------------")
        print()
                 
        print("=========== ORDENAMIENTO CON BURBUJA 2 ===========")
        mo.ordenamientoBurbuja2(None, mo.vector1000(None).copy())
        mo.ordenamientoBurbuja2(None, mo.vector10000(None).copy())
        mo.ordenamientoBurbuja2(None, mo.vector100000(None).copy())
        mo.ordenamientoBurbuja2(None, mo.vector1000000(None).copy())
        #mo.ordenamientoBurbuja2(None, lista)
                
        print()
        print("---------------------------------------------------------------------------------")
        print()
                  
        print("=========== ORDENAMIENTO CON BURBUJA 3 ===========")   
        mo.ordenamientoBurbuja3(None, mo.vector1000(None).copy())
        mo.ordenamientoBurbuja3(None, mo.vector10000(None).copy())
        mo.ordenamientoBurbuja3(None, mo.vector100000(None).copy())
        mo.ordenamientoBurbuja3(None, mo.vector1000000(None).copy())
        #mo.ordenamientoBurbuja3(None, lista)
                
        print()
        print("---------------------------------------------------------------------------------")
        print()
    elif(opcion == 2):
        
        print()
        print("---------------------------------------------------------------------------------")
        print()
                    
        print("=========== ORDENAMIENTO POR SELECCION ===========")  
        mo.ordenamientoPorSeleccion(None, mo.vector1000(None).copy())
        mo.ordenamientoPorSeleccion(None, mo.vector10000(None).copy())
        mo.ordenamientoPorSeleccion(None, mo.vector100000(None).copy())
        mo.ordenamientoPorSeleccion(None, mo.vector1000000(None).copy())
        #mo.ordenamientoPorSeleccion(None, lista)
        
        print()
        print("---------------------------------------------------------------------------------")
        print()
        
    elif(opcion == 3):
        
        print()
        print("---------------------------------------------------------------------------------")
        print()
                
        print("=========== ORDENAMIENTO POR INSERCION ===========")
        mo.ordenamientoPorInsercion(None, mo.vector1000(None).copy())
        mo.ordenamientoPorInsercion(None, mo.vector10000(None).copy())
        mo.ordenamientoPorinsercion(None, mo.vector100000(None).copy())
        mo.ordenamientoPorInsercion(None, mo.vector1000000(None).copy())
        #mo.ordenamientoPorInsercion(None, lista)
        
        print()
        print("---------------------------------------------------------------------------------")
        print()
    
    elif(opcion == 4):
        print()
        print("---------------------------------------------------------------------------------")
        print()
                
        print("=========== ORDENAMIENTO SHELLSORT ===========")
        
        
        print()
        print("---------------------------------------------------------------------------------")
        print()         
    
    elif(opcion == 0):
        print("S A L I E N D O . . .")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    