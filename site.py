import streamlit as st
from Metodos import *
import time
import sys
from time import sleep

sys.setrecursionlimit(10**9)

st.title("Tipos de ordenacao")
st.warning("Criado por Jose Carlos Vieira dos Santos Junior")
tamanho = st.radio(
        "Selecione o tamanho do Vetor:",
        [100, 1000, 10000,100000,1000000]
)

ordenacao = st.radio(
        "Selecione o tipo de Ordenacao:",
        ["Insertion Sort","Selection Sort","Bubble Sort","Shell Sort","Merge Sort","Quick Sort"]
)



click = st.button("Gerar Vetor com ordenacoes")

listaRandom = []
listaCresc = []
listaDecres = []

if (click == True):

    gerarArrayRandom(listaRandom,tamanho)

    gerarArrayCresc(listaCresc,tamanho)

    gerarArrayDecresc(listaDecres,tamanho)

    st.write("-=" * 52)

    if (ordenacao == "Insertion Sort"):
        st.write("Vetor Randomico:")
        ini = time.time()
        insertion(listaRandom)
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        st.write("O(n²)")
        print(str(fim-ini))
        st.write("Vetor Crescente:")
        ini = time.time()
        insertion(listaCresc)
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        print(str(fim-ini))
        st.write("O(n)")
        st.write("Vetor Decrescente:")
        ini = time.time()
        insertion(listaDecres)
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        st.write("O(n²)")
        print(str(fim-ini))

    elif (ordenacao == "Selection Sort"):
        st.write("Vetor Randomico:")
        ini = time.time()
        selection(listaRandom)
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        st.write("O(n²)")
        print(str(fim-ini))
        st.write("Vetor Crescente:")
        ini = time.time()
        selection(listaCresc)
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        st.write("O(n²)")
        print(str(fim-ini))
        st.write("Vetor Decrescente:")
        ini = time.time()
        selection(listaDecres)
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        st.write("O(n²)")
        print(str(fim-ini))
    elif (ordenacao == "Bubble Sort"):
        st.write("Vetor Randomico:")
        ini = time.time()
        bubble(listaRandom)
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        st.write("O(n²)")
        print(str(fim-ini))
        st.write("Vetor Crescente:")
        ini = time.time()
        bubble(listaCresc)
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        st.write("O(n²)")
        print(str(fim-ini))
        st.write("Vetor Decrescente:")
        ini = time.time()
        bubble(listaDecres)
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        st.write("O(n²)")
        print(str(fim-ini))
    elif (ordenacao == "Shell Sort"):
        st.write("Vetor Randomico:")
        ini = time.time()
        shellSort(listaRandom)
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        st.write("O(n (log n)²)")
        print(str(fim-ini))
        st.write("Vetor Crescente:")
        ini = time.time()
        shellSort(listaCresc)
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        st.write("O(n (log n)²)")
        print(str(fim-ini))
        st.write("Vetor Decrescente:")
        ini = time.time()
        shellSort(listaDecres)
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        st.write("O(n (log n)²)")
        print(str(fim-ini))
    elif (ordenacao == "Merge Sort"):
        st.write("Vetor Randomico:")
        ini = time.time()
        mergeSort(listaRandom)
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        st.write("O(n log n)")
        print(str(fim-ini))
        st.write("Vetor Crescente:")
        ini = time.time()
        mergeSort(listaCresc)
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        st.write("O(n log n)")
        print(str(fim-ini))
        st.write("Vetor Decrescente:")
        ini = time.time()
        mergeSort(listaDecres)
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        st.write("O(n log n)")
        print(str(fim-ini))
    elif (ordenacao == "Quick Sort"):
        aux = len(listaRandom) - 1
        st.write("Vetor Randomico:")
        ini = time.time()
        quickSort(listaRandom,0,aux)
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        st.write("O(n log n)")
        print(str(fim-ini))
        sleep(10)
        st.write("Vetor Crescente:")
        ini = time.time()
        quickSort(listaCresc,0,aux)
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        st.write("O(n²)")
        print(str(fim-ini))
        sleep(10)
        st.write("Vetor Decrescente:")
        ini = time.time()
        quickSort(listaDecres,0,aux)
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        st.write("O(n log n)")
        print(str(fim-ini))
    else:
        st.warning("Selecione um metodo de Ordenacao")