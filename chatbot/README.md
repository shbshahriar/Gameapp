<<<<<<< HEAD
# Gemini Chatbot with Memory and Search

A powerful Python chatbot powered by Google's Gemini AI with conversation memory and web search capabilities. Available as both a command-line interface and a FastAPI web service.

## 🚀 Features

- **🤖 AI-Powered**: Uses Google's Gemini 2.5 Pro model
- **🧠 Conversation Memory**: Remembers previous conversations
- **🌐 Web Search**: Real-time web search using Tavily API
- **📱 Dual Interface**: Both CLI and REST API versions
- **⚡ FastAPI**: Modern web framework with automatic API documentation
- **🔒 Secure**: Environment variable management for API keys

## 📁 Project Structure

```
gemini_chatbot_with_memory_search/
│
├── app.py              # FastAPI web application
├── chatbot.py          # Command-line interface
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
├── README.md          # This file
└── venv/              # Virtual environment (created locally)
```

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Git (for cloning)
- API keys for Google Gemini and Tavily

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/gemini-chatbot.git
cd gemini-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Create a `.env` file in the project root:

```env
# Google Gemini API Key
GOOGLE_API_KEY=your_google_api_key_here

# Tavily Search API Key
TAVILY_API_KEY=your_tavily_api_key_here
```

**Get API Keys:**
- **Google Gemini API**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
- **Tavily Search API**: Visit [Tavily](https://tavily.com/) for a free API key

## 🚀 Usage

### Command-Line Interface

Run the chatbot in interactive mode:

```bash
python chatbot.py
```

Example conversation:
```
User: What's the weather like today?
Bot: I'll search for current weather information for you...
[Bot searches the web and provides current weather data]

User: What did we just talk about?
Bot: We just discussed the current weather conditions...
```

### Web API Interface

Start the FastAPI server:

```bash
python app.py
```

The API will be available at `http://localhost:8000`

#### API Endpoints

- **POST `/chat`**: Send a message to the chatbot
  - Request body: `{"input": "your message here"}`
  - Response: `{"response": "bot response"}`

#### API Documentation

Visit `http://localhost:8000/docs` for interactive API documentation (Swagger UI)

### Example API Usage

```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"input": "What is the latest news about AI?"}'
```

## 🔧 Configuration

### Model Settings

You can modify the AI model and settings in both `app.py` and `chatbot.py`:

```python
# Change model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.7)

# Adjust temperature (0.0 = deterministic, 1.0 = creative)
temperature=0.7
```

### Memory Settings

The chatbot uses `ConversationBufferMemory` which stores all conversation history. For production use, consider:

- `ConversationSummaryMemory` for long conversations
- Database storage for persistent memory
- Memory limits to prevent token overflow

## 🛡️ Security

- API keys are stored in `.env` file (not committed to Git)
- CORS is configured for web API
- Input validation with Pydantic models

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for the AI framework
- [Google Gemini](https://ai.google.dev/) for the AI model
- [Tavily](https://tavily.com/) for web search capabilities
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/gemini-chatbot/issues) page
2. Create a new issue with detailed information
3. Include your Python version and error messages

---

=======
# Gemini Chatbot with Memory and Search

A powerful Python chatbot powered by Google's Gemini AI with conversation memory and web search capabilities. Available as both a command-line interface and a FastAPI web service.

## 🚀 Features

- **🤖 AI-Powered**: Uses Google's Gemini 2.5 Pro model
- **🧠 Conversation Memory**: Remembers previous conversations
- **🌐 Web Search**: Real-time web search using Tavily API
- **📱 Dual Interface**: Both CLI and REST API versions
- **⚡ FastAPI**: Modern web framework with automatic API documentation
- **🔒 Secure**: Environment variable management for API keys

## 📁 Project Structure

```
gemini_chatbot_with_memory_search/
│
├── app.py              # FastAPI web application
├── chatbot.py          # Command-line interface
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
├── README.md          # This file
└── venv/              # Virtual environment (created locally)
```

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Git (for cloning)
- API keys for Google Gemini and Tavily

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/gemini-chatbot.git
cd gemini-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Create a `.env` file in the project root:

```env
# Google Gemini API Key
GOOGLE_API_KEY=your_google_api_key_here

# Tavily Search API Key
TAVILY_API_KEY=your_tavily_api_key_here
```

**Get API Keys:**
- **Google Gemini API**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
- **Tavily Search API**: Visit [Tavily](https://tavily.com/) for a free API key

## 🚀 Usage

### Command-Line Interface

Run the chatbot in interactive mode:

```bash
python chatbot.py
```

Example conversation:
```
User: What's the weather like today?
Bot: I'll search for current weather information for you...
[Bot searches the web and provides current weather data]

User: What did we just talk about?
Bot: We just discussed the current weather conditions...
```

### Web API Interface

Start the FastAPI server:

```bash
python app.py
```

The API will be available at `http://localhost:8000`

#### API Endpoints

- **POST `/chat`**: Send a message to the chatbot
  - Request body: `{"input": "your message here"}`
  - Response: `{"response": "bot response"}`

#### API Documentation

Visit `http://localhost:8000/docs` for interactive API documentation (Swagger UI)

### Example API Usage

```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"input": "What is the latest news about AI?"}'
```

## 🔧 Configuration

### Model Settings

You can modify the AI model and settings in both `app.py` and `chatbot.py`:

```python
# Change model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.7)

# Adjust temperature (0.0 = deterministic, 1.0 = creative)
temperature=0.7
```

### Memory Settings

The chatbot uses `ConversationBufferMemory` which stores all conversation history. For production use, consider:

- `ConversationSummaryMemory` for long conversations
- Database storage for persistent memory
- Memory limits to prevent token overflow

## 🛡️ Security

- API keys are stored in `.env` file (not committed to Git)
- CORS is configured for web API
- Input validation with Pydantic models

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for the AI framework
- [Google Gemini](https://ai.google.dev/) for the AI model
- [Tavily](https://tavily.com/) for web search capabilities
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/gemini-chatbot/issues) page
2. Create a new issue with detailed information
3. Include your Python version and error messages

---

>>>>>>> 6330d868b913af753e8e9f45c8a07799dda0e411
**Made with ❤️ using Python, LangChain, and Google Gemini** 