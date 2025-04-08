# Career Navigator Bot

An intelligent conversational AI chatbot built using OpenAI GPT-4 and Streamlit, designed to help users explore personalized career paths based on their interests, skills, and education.

---

## Live Demo

[Click here to try the Streamlit app](https://career-navigator-bot-yovovwv5audmuczk2gnrpl.streamlit.app/)

---

## Project Overview

Career Navigator Bot is a career guidance assistant powered by OpenAI’s GPT-4 with function calling. The bot collects user interests and skills through a multi-turn conversation and recommends the most suitable career paths from a curated dataset of 70+ roles across industries.

It also provides structured details such as:

- Required Skills
- Learning Path
- Common Job Titles
- Recommended Tools

---

## Features

- ✅ GPT-4 turbo with function calling
- ✅ Multi-turn conversational input
- ✅ Real-time career recommendations
- ✅ Dataset of diverse career paths
- ✅ Step-by-step learning plans
- ✅ Deployed via Streamlit Cloud

---

## File Structure

```
career-navigator-bot/
├── app.py                       # Streamlit frontend app
├── utils.py                     # (Optional) Helper functions
├── career_dataset.csv           # Career knowledge base
├── .streamlit/
│   └── secrets.toml             # OpenAI API key (not pushed to repo)
├── requirements.txt             # Python dependencies
└── README.md
```

---

## How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/your-username/career-navigator-bot.git
cd career-navigator-bot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your OpenAI API key:

Create a file `.streamlit/secrets.toml` with the following content:

```toml
OPENAI_API_KEY = "your-openai-api-key"
```

4. Run the app:

```bash
streamlit run app.py
```

---

## Contributors

- **Raja Kalavala**

---

## License

MIT License. You are free to use, fork, and improve this project with credit.
