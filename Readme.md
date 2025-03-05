# Chatbot: Web Scraping & RAG-based Retrieval System

## Overview
This project is a **Retrieval-Augmented Generation (RAG)** chatbot that extracts and processes data from any website through its URL. The chatbot allows users to query website-related information and receive AI-generated responses based on scraped content.

## **Tech Stack**
- **Language**: Python
- **Web Scraping**: Reader, Requests
- **Data Processing**: LangChain (Text Splitting)
- **Vector Storage**: FAISS (Facebook AI Similarity Search)
- **Embeddings**: Google Generative AI API
- **Frontend**: Streamlit
- **Deployment**: Streamlit Cloud

---
## **Setup Instructions**

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/sanaa9012/scrappy.git
cd scrappy
```

### **2. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3. Environment Variables**
Create a `.env` file and add:
```sh
GOOGLE_API_KEY=your_google_api_key
ANY_WEBSITE_URL=(add URL)
JINA_API = "https://r.jina.ai"
```

### **4. Web Scraping (Data Extraction)**
The project scrapes content from the website using `Reader AI`

### **5. Text Preprocessing & Chunking**
Once the data is extracted, it is split into smaller chunks using `LangChain`

### **6. Creating & Storing Vector Embeddings**
The cleaned and split text is converted into **vector embeddings** using the **Google Generative AI API**, then stored in **FAISS**

### **7. Retrieval & Querying with RAG**
When a user asks a question, the query is embedded and compared against stored vectors in FAISS

### **8. Generating Responses with AI**
The retrieved content is passed to **Google Generative AI** for response generation

### **9. Streamlit UI**
The chatbot is deployed with **Streamlit**

### **10. Running the App**
```sh
streamlit run app.py
```

---
## **Deployment**
1. Deploy on **Streamlit Cloud**.
2. Ensure API keys are added as environment variables in deployment settings.

---
## **Conclusion**
This project efficiently integrates **web scraping, vector search, and AI-powered text generation** to create an interactive chatbot that provides real-time Aptos-related insights. By leveraging **RAG**, the chatbot ensures accurate and contextually relevant responses, enhancing user experience.

