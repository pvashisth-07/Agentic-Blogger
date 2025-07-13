# 🧠 Agentic Blog Generator & Translator with LangGraph 🚀

This is an **LLM-powered blog generation and translation engine**, built using [LangGraph](https://docs.langgraph.dev/) and [LangChain](https://www.langchain.com/). It leverages **Groq's LLaMA 3.1 8B model** for generating SEO-friendly blog titles and content, and supports dynamic translation (currently to **Hindi** and **French**).

## 🛠️ Tech Stack

| Tool / Library         | Purpose                                                  |
|------------------------|----------------------------------------------------------|
| **LangGraph**          | Builds structured graph flows for blog generation logic |
| **LangChain**          | Interfaces with LLMs and structured output              |
| **Groq + LLaMA 3.1**   | Fast, low-latency LLM for generating and translating blogs |
| **FastAPI**            | Lightweight backend for serving APIs                    |
| **Postman**            | Testing endpoints and showcasing API usage              |
| **Pydantic**           | Enforcing type safety and data validation                |
| **LangSmith**          | Tracks and visualizes graph execution and LLM traces    |
| **Python (3.10+)**     | Core programming language for the backend                |

---

## 📌 Features

- 📝 Generate blog titles and content using only a topic
- 🌍 Translate content into Hindi or French
- 🔄 Dynamic graph routing with LangGraph
- 🧪 Test-ready REST APIs via FastAPI
- 📈 LangSmith observability integrated

---

## 📂 Project Structure

├── app.py # FastAPI app entrypoint
├── .env # Environment variables
├── langgraph.json # LangGraph + LangSmith config
└── src/
├── graphs/
│ └── graph_builder.py # LangGraph construction logic
├── llms/
│ └── groqllm.py # Groq LLM wrapper
├── nodes/
│ └── node.py # Blog logic nodes (title, content, translation, routing)
└── states/
└── blogstate.py # Blog + state schema using Pydantic

---


---

## 📸 Demo Screenshots
<img width="914" height="753" alt="Screenshot 2025-07-13 034829" src="https://github.com/user-attachments/assets/5c0d8236-877a-4a14-9be6-925aafe22041" />
<img width="752" height="556" alt="Screenshot 2025-07-13 152040" src="https://github.com/user-attachments/assets/13f9a356-7c4b-4dba-aa21-28edaa74dcd7" />
<img width="1919" height="1123" alt="Screenshot 2025-07-13 152126" src="https://github.com/user-attachments/assets/391c4495-bbde-4461-8dce-8e4448a4fa48" />
<img width="811" height="944" alt="Screenshot 2025-07-13 151600" src="https://github.com/user-attachments/assets/2377c7ec-357f-4644-8b5b-ca26977a769a" />


---

## 🛠️ Future Enhancements

- 🌐 Add support for more languages (e.g., Spanish, German)

- 🧠 Integrate memory and context chaining

- 📤 Export blogs as downloadable Markdown/HTML

- 🔀 Add streaming and async LLM support

- 🖥️ Optional UI with Streamlit or Next.js

---

## 👤 Author
Pranav Vashisth
📧 pvashisth0711@gmail.com
💼 LinkeIn : https://www.linkedin.com/in/pranav-vashisth/

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/agentic-blog-generator.git
cd agentic-blog-generator

---

