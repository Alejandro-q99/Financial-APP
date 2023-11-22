
import streamlit as st
import pandas as pd
import numpy as np
from Functions import Processors as pr
from Functions import Chat_methods as ch


import requests
from langchain.document_loaders import PyPDFLoader, OnlinePDFLoader
from langchain.document_loaders.csv_loader import CSVLoader





#read
url = 'https://raw.githubusercontent.com/Alejandro-q99/Financial-APP/main/app/Data/clean_financial_data.csv'
df = pd.read_csv(url)


#df_cleaned = cleaned_data.drop("diferencia", axis=1) Verificar utilidad de esta ci¿olumna



st.title("BONOS DATA")
# Mostrar Gráfica.
st.dataframe(df)


# ----


st.title("Financial AI assistance")

#OPENAI_API_KEY = getpass(password)
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]



# ----- MODEL TRAINING

st.cache_data
def load_data():
    urls = [
        'https://arxiv.org/pdf/2306.06031v1.pdf',
        'https://www.argentina.gob.ar/sites/default/files/informe_deuda_sostenible_2023-0304.pdf',
        'https://www.argentina.gob.ar/sites/default/files/informe_cnv_6_act.pdf'
    ]

    ml_papers = []
    
    for source in urls:
        response = requests.get(source)
    
    for i, url in enumerate(urls):
        response = requests.get(url)
        filename = f'app/Data/paper{i+1}.pdf'
        with open(filename, 'wb') as f:
            f.write(response.content)
            print(f'Descargado {filename}')

            loader = PyPDFLoader(filename) # Clase de Lang chain
            data = loader.load()
            ml_papers.extend(data)
    
    
    # Data Tabular preprocesada.
    tabular_data = load_tabular_data("./Data/clean_financial_data.csv")
    ml_papers.extend(tabular_data)
    
    return ml_papers


def load_tabular_data(path):
    loader = CSVLoader(
    file_path=path,
    csv_args={
        "delimiter": ",",
        "fieldnames": ["id","diferencia","dq","indice","md","paridad","pq","precio","qp","ticker","tir","ttir","uptir","volumen","vt"], 
    },)
    #Volver dinámico  el fieldnames para que parsee mejor el dataset que entre, es decir, que no sea columna dependiente. pd.read_csv().pd.columns
    tabular_data = loader.load()
    return tabular_data




with st.spinner('Wait for it...'):
    ml_papers = load_data()
    st.success('Financial Knowledge Load!')


from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=200,
    length_function=len
    )

documents = text_splitter.split_documents(ml_papers)

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma


embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
    )



from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

chat = ChatOpenAI(
    openai_api_key= OPENAI_API_KEY,
    model_name='gpt-3.5-turbo',
    temperature=0.0
)

qa_chain = RetrievalQA.from_chain_type(
    llm=chat,
    chain_type="stuff",
    retriever=retriever
)

# ---------
chat_history = []
# Chat
# Función para realizar una consulta y almacenar la conversación
def ask_and_store(query):
    # Ejecutar la consulta a través de la cadena de QA
    response = qa_chain.run(query)

    # Almacenar la consulta y la respuesta en el historial
    chat_history.append({"query": query, "response": response})

    return response



query =  st.text_input("> ")
c_response = ask_and_store(query)
st.write(c_response)




