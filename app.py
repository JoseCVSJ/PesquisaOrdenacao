import streamlit
from Metodos import *
from random import randint
streamlit.title("Trabalho de Pesquisa e Ordenacao C2")
array = ()
print("1 - Vetor tamanho 100")
print("2 - Vetor tamanho 1000")
print("3 - Vetor tamanho 10000")
print("4 - Vetor tamanho 100000")
print("5 - Vetor tamanho 1000000")

opc = input("Escolha uma das opções para que o vetor seja ordenado:")
opc = int(opc)

if (opc == 1):
    array100(array)
    print(array)
    print("-=-=" * 30)
    print("Insertion Sort:")
    array100(array)
    insertion(array)
    print(array)
    print("-=-=" * 30)
    print("Selecion Sort:")
    selection(array)
    print("-=-=" * 30)
    print("Bubble Sort:")
    bubble(array)
    print("-=-=" * 30)
    print("Merge Sort:")
    mergeSort(array)
    print("-=-=" * 30)
    print("Quick Sort:")
    quickSort(array)
    print("-=-=" * 30)
    print("Shell Sort:")
    shellSort(array)
    print("-=-=" * 30)

elif (opc == 2):
    array1000(array)
    insertion(array)
    selection(array)
    bubble(array)
    mergeSort(array)
    quickSort(array)
    shellSort(array)

elif (opc == 3):
    array10000(array)
    insertion(array)
    selection(array)
    bubble(array)
    mergeSort(array)
    quickSort(array)
    shellSort(array)

elif (opc == 4):
    array100000(array)
    insertion(array)
    selection(array)
    bubble(array)
    mergeSort(array)
    quickSort(array)
    shellSort(array)

elif (opc == 5):
    array1000000(array)
    insertion(array)
    selection(array)
    bubble(array)
    mergeSort(array)
    quickSort(array)
    shellSort(array)


else:
    print("Error")
