import streamlit as st

st.title("Psicofarma")

firebase = firebase.FirebaseApplication("https://psicofarma.streamlit.app/",None)

def getAlelos(gen):
    '''
    Función que dado un gen proporciona todos los alelos encontrados para dicho gen. Para realizar esta consulta, emplea las guías del CPIC
    
    Parametros:
        gen: String
        Nombre del gen a buscar

    Returns:
        ListaFinalAlelos : list
        Lista de alelos para dicho gen, obtenidos del CPIC
    '''
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
