
# 🧑‍⚖️ Legal AI Summarizer
# AI Summarizer [ Q & A ]

> A modern platform to simplify legal documents for everyone. Upload, summarize, and interact with your legal files using advanced AI.

---

## 🚀 Features

- **Upload PDF/DOC files:** Notices, terms, government docs, bank conditions, and more
- **Instant AI Summary:** Get a concise summary of your document
- **Key Highlights:** Important topics and crucial points automatically extracted
- **Chat with Your Document:** Ask questions and get relevant answers using RAG + OpenAI LLM
- **Classy Streamlit UI:** Modern, attractive, and easy to use
- **Short-Term Chat Memory:** Access your last 10 Q&A (hidden in UI for privacy)
- **Semantic Vector Database:** Store and retrieve document meaning with FAISS/Chroma

---

## 🛠️ Quick Start

1. **Clone the repository**

```bash
git clone https://github.com/piyal21/Legal_AI_Summarizer.git
cd Legal_AI_Summarizer
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
source venv/bin/activate      # On Mac/Linux
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Add your OpenAI API key**

- Copy `.env.example` to `.env` and add your `OPENAI_API_KEY`

5. **Run the app**

```bash
streamlit run app/main.py
```

---

## 📁 Folder Structure

```text
├── README.md                # Project overview, setup instructions
├── requirements.txt         # Python dependencies
├── .env.example            # Example for environment variables
├── .gitignore              # Ignore cache, venv, etc.
│
├── app/                    # Core application code
│   ├── main.py             # Entry point (Streamlit UI)
│   ├── config.py           # Configuration (API keys, constants)
│   ├── utils/              # Utility functions
│   │   ├── file_handler.py
│   │   ├── text_splitter.py
│   │   ├── vector_store.py
│   │   ├── summarizer.py
│   │   ├── memory.py
│   │   └── highlight.py
│   ├── rag_pipeline.py     # RAG pipeline (embedding + retrieval + LLM)
│   ├── chat_manager.py     # Chat session management
│   └── ui_components.py    # Streamlit UI elements
│
├── data/                   # User uploaded docs (local dev only)
│   ├── uploads/            # Uploaded PDF/DOC files
│   └── vector_dbs/         # Vector databases (FAISS/Chroma)
```

---

## 💡 How It Works

1. **Upload your legal document** (PDF/DOC)
2. **AI generates a summary** and highlights key topics
3. **Ask questions** about your document in the chat
4. **Get relevant answers** powered by RAG and OpenAI

---

## 🔒 Environment Variables

Create a `.env` file based on `.env.example` and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 🤝 Contributing

Pull requests and suggestions are welcome! For major changes, please open an issue first.

---

<<<<<<< HEAD
## 📄 License

This project is licensed under the MIT License.
=======
.
>>>>>>> ff0791483c256444b2d3f64ca6732127346b190d
