

# 🚀 Startup Assistant Agent

> Your AI-powered virtual co-founder to brainstorm ideas, build lean canvases, research markets, and prepare pitch decks — all in one click!

---

## ✨ Overview

**Startup Assistant Agent** is an intelligent, AI-powered platform built using [CrewAI](https://github.com/joaomdmoura/crewAI) and [Streamlit](https://streamlit.io/).  
It acts as your virtual co-founder, helping early-stage entrepreneurs and founders:

- ✅ Generate startup ideas
- ✅ Conduct deep market research
- ✅ Build a Lean Canvas model
- ✅ Craft compelling investor pitches
- ✅ Develop branding (names, slogans, visual identity)
- ✅ Plan marketing content (blogs, product descriptions, social posts)
- ✅ Strategize startup operations

Everything you need to **kickstart and scale** your startup — all in one place!

---

## 🛠 Features

- 🚀 Simple and clean web interface (Streamlit UI)
- 🧠 Multi-agent system with specialized roles
- 🕵️ Real-time web search and website scraping
- 📄 Auto-generated startup reports
- 🌐 Powered by Google Gemini 1.5 Flash LLM
- 🛠️ Built for modularity and future expansion

---

## 🧩 Tech Stack

- **Frontend:** Streamlit
- **Backend:** CrewAI + Google Gemini LLM
- **Search Integration:** Serper.dev
- **Scraping:** ScrapeWebsiteTool
- **Programming Language:** Python 3.9+

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/startup-assistant-agent.git
cd startup-assistant-agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
# Activate the environment
source venv/bin/activate       # For Linux/Mac
venv\Scripts\activate          # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY="AIzaSyAKe3fdi3uTIcsciS0hoaPB3KkuhnthACY"
SERPER_API_KEY="8d602abe0f5ebb126d553632d467ef66c73b318f"
```

_(**Important:** Do not share your API keys publicly.)_

### 5. Launch the Application

```bash
streamlit run improved_app.py
```

The app will automatically open in your default browser at `http://localhost:8501`.

---

## 📂 Project Structure

```bash
startup-assistant-agent/
│
├── improved_app.py         # Main Streamlit application
├── README.md                # Project documentation
├── requirements.txt         # Required Python packages
├── .env.example             # Example environment file
└── demo.gif                 # (Optional) App demo preview
```

---

## ⚙️ Requirements

- Python 3.9 or above
- API Keys for:
  - [Google Gemini](https://ai.google.dev/)
  - [Serper.dev](https://serper.dev/)

---

## 🌟 Future Roadmap

- 🔐 Add user authentication and project history
- 📄 Export full startup reports as PDF and PPT
- 💬 Add chat-based startup advice assistant
- 🌍 Support for multiple languages
- 🤖 Integrate additional LLM models (Claude, OpenAI, etc.)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to ⭐ star the repository and fork it.  
If you have ideas to improve the app, please open an issue or a pull request.

---

## 📜 License

Distributed under the [MIT License](LICENSE).  
Feel free to use, modify, and distribute!

---

## 🧡 Special Thanks

- [CrewAI](https://github.com/joaomdmoura/crewAI)
- [Streamlit](https://streamlit.io/)
- [Google AI (Gemini)](https://ai.google.dev/)
- [Serper.dev](https://serper.dev/)

---

> Made with 💻 + ☕ + 🚀 to empower founders around the world!
