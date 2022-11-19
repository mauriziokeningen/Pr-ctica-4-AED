import csv
from tabulate import tabulate

with open('C:\\Users\\Mauricio\Desktop\\IPN\\Segundo Semestre\\Algorithms & Data Structures\\Practicas\\Practica 4\\BD_Personas_Binario.csv',mode='r', encoding="utf8") as Binario:
    Lector = csv.reader(Binario)
    Personas = (list(Lector))
    Personas.pop(0)

PersonasDesordenadas = Personas.copy()
columns = ['País de Origen','Nombre','Altura','Teléfono']

def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
                if arr[min_idx][2] > arr[j][2]:
                    min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print('\nLa lista de personas ordenada por altura es:\n\n',tabulate(arr, headers=columns),'\n')


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i=j=k=0
        while i < len(L) and j < len(R):
            if L[i][1][1] <= R[j][1][1]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k]=L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k]=R[j]
            j+=1
            k+=1

def printMerge(arr):
    mergeSort(arr)
    print('\nLa lista de personas ordenada por la segunda letra del nombre es:\n\n',tabulate(arr, headers=columns),'\n')
 
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][3] > arr[j+1][3]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print('\nLa lista ordenada por numero de teléfono es:\n\n',tabulate(arr, headers=columns),'\n')
    
def insertionSort(arr):
    for i in range(1, len(arr)):
        key1=arr[i]
        key2=arr[i][0]
        j=i-1
        while j>=0 and arr[j][0]>key2:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1] = key1
    print('\nLa lista de personas ordernadas por país es:\n\n',tabulate(arr, headers=columns),'\n')

print("\nSeleccione cómo ordenar la base de datos:\n\n1) Mostrar lista de personas en desorden.\n2) Ordenar lista de personas por altura.\n3) Ordenar lista de personas por la segunda letra del nombre.\n4) Ordenar lista de personas por número de teléfono.\n5) Ordenar lista de personas por país de origen.\n")
opcion = int(input())

def menu(opcion):
    if opcion == 1:
        print('\nLa lista de personas mostrada en desorden es:\n\n',tabulate(PersonasDesordenadas, headers=columns),'\n') 
        print('\n¿Quiere realizar otra operacion?\nY) Sí\nN) No\n')
        opcion = str(input())
        if opcion == 'Y':
            print("\nSeleccione cómo ordenar la base de datos:\n\n1) Mostrar lista de personas en desorden.\n2) Ordenar lista de personas por altura.\n3) Ordenar lista de personas por la segunda letra del nombre.\n4) Ordenar lista de personas por número de teléfono.\n5) Ordenar lista de personas por país de origen.\n")
            opcion = int(input())
            menu(opcion)
        else:
            print("\nHasta luego\n")
    elif opcion == 2:
        selectionSort(Personas)
        print('\n¿Quiere realizar otra operacion?\nY) Sí\nN) No\n')
        opcion = str(input())
        if opcion == 'Y':
            print("\nSeleccione cómo ordenar la base de datos:\n\n1) Mostrar lista de personas en desorden.\n2) Ordenar lista de personas por altura.\n3) Ordenar lista de personas por la segunda letra del nombre.\n4) Ordenar lista de personas por número de teléfono.\n5) Ordenar lista de personas por país de origen.\n")
            opcion = int(input())
            menu(opcion)
        else:
            print("\nHasta luego\n")
    elif opcion == 3:
        printMerge(Personas)
        print('\n¿Quiere realizar otra operacion?\nY) Sí\nN) No\n')
        opcion = str(input())
        if opcion == 'Y':
            print("\nSeleccione cómo ordenar la base de datos:\n\n1) Mostrar lista de personas en desorden.\n2) Ordenar lista de personas por altura.\n3) Ordenar lista de personas por la segunda letra del nombre.\n4) Ordenar lista de personas por número de teléfono.\n5) Ordenar lista de personas por país de origen.\n")
            opcion = int(input())
            menu(opcion)
        else:
            print("\nHasta luego\n")
    elif opcion == 4:
        bubbleSort(Personas)
        print('\n¿Quiere realizar otra operacion?\nY) Sí\nN) No\n')
        opcion = str(input())
        if opcion == 'Y':
            print("\nSeleccione cómo ordenar la base de datos:\n\n1) Mostrar lista de personas en desorden.\n2) Ordenar lista de personas por altura.\n3) Ordenar lista de personas por la segunda letra del nombre.\n4) Ordenar lista de personas por número de teléfono.\n5) Ordenar lista de personas por país de origen.\n")
            opcion = int(input())
            menu(opcion)
        else:
            print("\nHasta luego\n")
    elif opcion == 5:
        insertionSort(Personas)
        print('\n¿Quiere realizar otra operacion?\nY) Sí\nN) No\n')
        opcion = str(input())
        if opcion == 'Y':
            print("\nSeleccione cómo ordenar la base de datos:\n\n1) Mostrar lista de personas en desorden.\n2) Ordenar lista de personas por altura.\n3) Ordenar lista de personas por la segunda letra del nombre.\n4) Ordenar lista de personas por número de teléfono.\n5) Ordenar lista de personas por país de origen.\n")
            opcion = int(input())
            menu(opcion)
        else:
            print("\nHasta luego\n")
    else:
        print("La opcion ingresada no es valida.\n")
        print('\n¿Quiere realizar una operacion?\nY) Sí\nN) No\n')
        opcion = str(input())
        if opcion == 'Y':
            print("\nSeleccione cómo ordenar la base de datos:\n\n1) Mostrar lista de personas en desorden.\n2) Ordenar lista de personas por altura.\n3) Ordenar lista de personas por la segunda letra del nombre.\n4) Ordenar lista de personas por número de teléfono.\n5) Ordenar lista de personas por país de origen.\n")
            opcion = int(input())
            menu(opcion)
        else:
            print("\nHasta luego!\n")
        
menu(opcion)