import os 
import requests
import streamlit as st
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_community.vectorstores import FAISS 
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# url = 'https://aptosfoundation.org/'
JINA_API = os.getenv("JINA_API")

@st.cache_data
def scrap_site(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    raw_text = soup.get_text(separator=" ", strip=True)
    processed_text = process_text_with_jina(raw_text)
    return processed_text

def process_text_with_jina(text):
    payload = {"input":text, "task": "text-processing"}
    response = requests.get(f"{JINA_API}/{url}")
    
    if response.status_code == 200:
        return response.json().get("output", "no output recieved")
    else:
        return f"Error: {response.text}"
    
@st.cache_resource
def get_vector_store(text):
    text_splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
    text_chunk = text_splitter.split_text(text)
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    vectorstore = FAISS.from_texts(text_chunk, embeddings)
    vectorstore.save_local("vectorstore")
    return vectorstore

def chat_bot(user_query):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    vector_store = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)
    retrieved_docs = vector_store.similarity_search(user_query, k = 5)
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"Context: {context}\nUser: {user_query}")
    return response.text

# ------ UI ------

st.set_page_config(page_title="Scrappy", page_icon="👾")
st.title("🤖Scrappy Chatbot")
st.markdown("Ask a question about the website you added!")

url = st.text_input("Enter the URL of the website you want to scrape:")

if st.button("Scrape"):
    with st.spinner("Scrapping..."):
        text = scrap_site(url)
        vectorstore = get_vector_store(text)
        st.success("Scrapped successfully!")
        
user_query = st.text_input("Ask your question:")

if st.button("Ask"):
    if user_query:
        with st.spinner("Thinking..."):
            response = chat_bot(user_query)
            st.success("Response:")
            st.write(response)
            
    else:
        st.warning("Please enter a question!")