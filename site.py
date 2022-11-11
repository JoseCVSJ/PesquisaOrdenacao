import streamlit as st
from Metodos import *
import time

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
    st.write("Vetor Randomico:")
    st.markdown(gerarArrayRandom(listaRandom,tamanho))

    st.write("Vetor Crescente:")
    st.markdown(gerarArrayCresc(listaCresc,tamanho))

    st.write("Vetor Decrescente:")
    st.markdown(gerarArrayDecresc(listaDecres,tamanho))

    st.write("-=" * 52)

    if (ordenacao == "Insertion Sort"):
        st.write("Vetor Randomico:")
        ini = time.time()
        st.markdown(insertion(listaRandom))
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        print("O(n²)")
        st.write("Vetor Crescente:")
        ini = time.time()
        st.markdown(insertion(listaCresc))
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        print("O(n)")
        st.write("Vetor Decrescente:")
        ini = time.time()
        st.markdown(insertion(listaDecres))
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        print("O(n²)")

    elif (ordenacao == "Selection Sort"):
        st.write("Vetor Randomico:")
        ini = time.time()
        st.markdown(selection(listaRandom))
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        print("O(n²)")
        st.write("Vetor Crescente:")
        ini = time.time()
        st.markdown(selection(listaCresc))
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        print("O(n²)")
        st.write("Vetor Decrescente:")
        ini = time.time()
        st.markdown(selection(listaDecres))
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        print("O(n²)")
    elif (ordenacao == "Bubble Sort"):
        st.write("Vetor Randomico:")
        ini = time.time()
        st.markdown(bubble(listaRandom))
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        print("O(n²)")
        st.write("Vetor Crescente:")
        ini = time.time()
        st.markdown(bubble(listaCresc))
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        print("O(n²)")
        st.write("Vetor Decrescente:")
        ini = time.time()
        st.markdown(bubble(listaDecres))
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        print("O(n²)")
    elif (ordenacao == "Shell Sort"):
        st.write("Vetor Randomico:")
        ini = time.time()
        st.markdown(shellSort(listaRandom))
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        print("O(n (log n)²)")
        st.write("Vetor Crescente:")
        ini = time.time()
        st.markdown(shellSort(listaCresc))
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        print("O(n (log n)²)")
        st.write("Vetor Decrescente:")
        ini = time.time()
        st.markdown(shellSort(listaDecres))
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        print("O(n (log n)²)")
    elif (ordenacao == "Merge Sort"):
        st.write("Vetor Randomico:")
        ini = time.time()
        st.markdown(mergeSort(listaRandom))
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        print("O(n log n)")
        st.write("Vetor Crescente:")
        ini = time.time()
        st.markdown(mergeSort(listaCresc))
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        print("O(n log n)")
        st.write("Vetor Decrescente:")
        ini = time.time()
        st.markdown(mergeSort(listaDecres))
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        print("O(n log n)")
    elif (ordenacao == "Quick Sort"):
        st.write("Vetor Randomico:")
        ini = time.time()
        st.markdown(quickSort(listaRandom))
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        print("O(n log n)")
        st.write("Vetor Crescente:")
        ini = time.time()
        st.markdown(quickSort(listaCresc))
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        print("O(n²)")
        st.write("Vetor Decrescente:")
        ini = time.time()
        st.markdown(quickSort(listaDecres))
        fim = time.time()
        st.write("Demorou " + str(fim-ini) + " Segundos para terminar a operação")
        print("O(n log n)")
    else:
        st.warning("Selecione um metodo de Ordenacao")