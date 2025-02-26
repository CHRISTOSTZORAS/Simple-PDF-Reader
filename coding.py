import streamlit as st 
import numpy as np
from PyPDF2 import  PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import faiss
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import re
#upload pdf files
st.header("Tzwrakos Chatbox")
with st.sidebar:
    st.title('Your Documends')
    file=st.file_uploader("Upload a DF file and start asking questions",type="pdf")
    
# Caching function for embeddings to improve performance
@st.cache_data
def compute_embeddings(chunks):
    model = SentenceTransformer('all-MiniLM-L6-v2')  # Embedding model for similarity search
    return model.encode(chunks, convert_to_numpy=True, batch_size=16, show_progress_bar=True)

# Caching function for the QA pipeline to improve load times
@st.cache_resource
def load_qa_pipeline():
    return pipeline("question-answering", model="deepset/roberta-base-squad2")

#extract the text
if file is not None:
    pdf_reader=PdfReader(file)
    text=''
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    # Clean the extracted text
    cleaned_text = re.sub(r'\s+', ' ', text.strip())
#break it into chunks
    text_splitter=RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=500,
        chunk_overlap=50,
        length_function=len
    )
    chunks=text_splitter.split_text(text)
    #st.write(chunks)

    model = SentenceTransformer('all-MiniLM-L6-v2')
    #generating embeddings
    embeddings = model.encode(chunks,convert_to_numpy=True)

    # Create a FAISS index and add embeddings
    dimension = embeddings.shape[1]  
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

    # Get user question
    user_question = st.text_input('ΡΙΧΤΟ ΡΕ ΛΑΜΟΓΙΟ')

    if user_question:
        # Generate embedding for the user question
        question_embedding = model.encode([user_question], convert_to_numpy=True)

        # Perform similarity search using FAISS
        k = 1  
        distances, indices = index.search(np.array(question_embedding), k)

        # Concatenate top chunks into context
        context = " ".join([chunks[idx] for idx in indices[0]])

        # Pass context and question to the LLM
        result = qa_pipeline(question=user_question, context=context)

        # Optional: Show retrieved chunks for reference
        st.subheader("Τα αποτελέσματα σου μπινέ:")
        for i, idx in enumerate(indices[0]):
            st.write(chunks[idx])





