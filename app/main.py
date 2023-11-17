
import streamlit as st
import pandas as pd
import numpy as np
from Functions import Processors as pr
from Functions import Chat_methods as ch
from datetime import datetime
import os


#read
url = 'https://raw.githubusercontent.com/Alejandro-q99/Financial-APP/main/app/Data/bonos.csv'
df = pd.read_csv(url)
#clean
cleaned_data = pr.clean_and_convert_data(df)
df_cleaned = cleaned_data

#df_cleaned = cleaned_data.drop("diferencia", axis=1) Verificar utilidad de esta ci¿olumna



st.title("BONOS TASA FIJA - BADLAR")
# Mostrar Gráfica.
st.dataframe(df_cleaned)


# ----

metadata = """

Columnas del dataset de BONOS DE BADLAR

Diferencia (diferencia)
Días al vencimiento (dq)
Índice (indice)
Margen de dispersión (md)
Paridad (paridad)
Precio de corte (pq)
Precio (precio)
Porcentaje de cobertura (qp)
Ticker (ticker)
Tasa interna de retorno (tir)
Tasa total interna de retorno (ttir)
Tasa única total interna de retorno (uptir)
Volumen (volumen)
Volumen total (vt)


"""






with st.sidebar:
    
    st.title('🦙💬 Fin Chatbot')
    st.write('This chatbot is created using the open-source LLM for Financial analysis')
    if 'OPENAI_API_KEY' in st.secrets:
        st.success('API key already provided!', icon='✅')
        open_api = st.secrets['OPENAI_API_KEY']
    else:
        open_api = st.text_input('Enter Open API token:', type='password')
        if not (open_api.startswith('r8_') and len(open_api)==40):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
    os.environ['OPENAI_API_KEY'] = open_api






def main():
    st.title("Financial AI Assistance")

    # Registro de mensajes de la conversación
    if 'message_log' not in st.session_state:
        st.session_state['message_log'] = [{"role": "system", "content": "You are a helpful assistant."}]

    # Campo de entrada para el mensaje del usuario
    user_input = st.text_input("Preguntale por tus datos aquí!:")

    # Botón de enviar
    if st.button('Enviar'):
        st.session_state['message_log'].append({"role": "user", "content": user_input})
        response = ch.send_message(st.session_state['message_log'])
        st.session_state['message_log'].append({"role": "assistant", "content": response})
        st.write(response)

if __name__ == '__main__':
    main()