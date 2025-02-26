# Tzwrakos Chatbox - README

## 📄 Overview
**Tzwrakos Chatbox** is an interactive web application built with **Streamlit** that allows you to upload PDF documents and ask questions about their content. The app uses advanced AI models to read, process, and analyze uploaded documents, providing descriptive and context-aware answers to your queries.

---

## 🚀 Features
✅ Upload PDF files and extract text content automatically.  
✅ Ask questions about the uploaded document and receive detailed answers.  
✅ Advanced similarity search powered by **FAISS** for fast and relevant information retrieval.  
✅ Utilizes GPU acceleration (if available) for faster processing.  
✅ AI-generated responses that summarize and explain content contextually.  
✅ Handles both large and small documents efficiently.

---

## 🛠️ Installation
### 1️⃣ Clone the repository:
```bash
git clone https://github.com/your-repo/tzwrakos-chatbox.git
cd tzwrakos-chatbox
```

### 2️⃣ (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

### 3️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```
> **Note:** To use GPU acceleration, ensure you have CUDA drivers and the appropriate PyTorch version installed.

---

## 🧪 Usage
### 🚀 Run the application:
```bash
streamlit run app.py
```

### 📚 Instructions:
1. Upload a PDF file using the sidebar.  
2. Type a keyword or a question in the input box.  
3. The app will display a well-structured answer along with document excerpts used to generate the response.  
4. (Optional) Generate a summary of the entire document.

> 💡 **Tip:** If you experience CUDA errors, the app automatically switches to CPU mode.

---

## ⚙️ Project Structure
```
├── app.py              # Main Streamlit application
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── screenshots/        # Example screenshots (optional)
```

---

## 🧩 Dependencies
- [Streamlit](https://streamlit.io/) - Web application framework  
- [SentenceTransformers](https://www.sbert.net/) - Text embeddings  
- [Transformers (Hugging Face)](https://huggingface.co/docs/transformers) - LLM and text generation models  
- [FAISS](https://github.com/facebookresearch/faiss) - Efficient similarity search  
- [PyPDF2](https://pypi.org/project/PyPDF2/) - PDF text extraction  
- [Torch](https://pytorch.org/) - Deep learning backend  

---

## 🖥️ Screenshots
| Upload & Query Interface | Generated Answer Example |
|--------------------------|--------------------------|
| ![Upload Screenshot](screenshots/upload.png) | ![Answer Screenshot](screenshots/answer.png) |

---

## 📝 Example Usage
### Input:
`revenue growth`  
### Output:
> *"According to the uploaded document, the company's revenue grew by 12% in 2023, marking a significant improvement compared to the previous year..."*

---

## 🛡️ Troubleshooting
- **CUDA Error:** Ensure you have compatible GPU drivers. The app will automatically switch to CPU if necessary.  
- **No Text Extracted:** Ensure the PDF has selectable text (scanned images are not supported).  
- **Slow Performance:** Use smaller PDFs or reduce chunk sizes for quicker processing.  
- **FAISS Errors:** Verify that there are enough text chunks extracted from the document.

---

## 📢 Contributing
Pull requests are welcome! For major changes, please open an issue to discuss the proposed modifications.

---

## 📜 License
This project is licensed under the MIT License.

---

## 🙌 Acknowledgements
- Developed with ❤️ using Streamlit, Hugging Face, and FAISS.  
- Inspired by the need for intelligent document exploration tools.

---

## 📬 Contact
For inquiries, reach out via email: [your-email@example.com](mailto:your-email@example.com)  
Visit: [your-website.com](https://your-website.com)  

---

🚀 **Start exploring your documents like never before with Tzwrakos Chatbox!**