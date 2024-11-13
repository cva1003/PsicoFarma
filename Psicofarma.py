import streamlit as st
import requests

st.title("Psicofarma")

firebase = firebase.FirebaseApplication("https://psicofarma.streamlit.app/",None)

def obtenerAlelos(gen):

    url = "https://api.cpicpgx.org/v1/allele?genesymbol=eq."+ gen
    
    respuesta = requests.get(url)
    datos = respuesta.json()

    alelos = list()
    
    for i in range(len(datos)):
        alelo = datos[i]["name"]
        alelos.append(alelo)

    setAlelos = set(alelos)
    ListaFinalAlelos = (list(setAlelos))
    ListaFinalAlelos.sort()
    return ListaFinalAlelos

def obtener_ID(farmaco):

    #https://api.cpicpgx.org/v1/drug?name=eq.abacavir
    url = "https://api.cpicpgx.org/v1/drug?name=eq."+farmaco
    
    respuesta = requests.get(url)
    obtenido = respuesta.json()
    
    if len(obtenido) != 0:
        ID_Farmaco = obtenido[0]['drugid']
        return ID_Farmaco
    else:
        return ''
