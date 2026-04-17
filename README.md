# SmritiBrief – AI Meeting Memory Agent for Indian Professionals

**Har meeting ka context, har client ka preference — SmritiBrief remembers everything so you don’t have to chase old notes again.**

SmritiBrief is an autonomous AI agent designed to act as your personal "meeting memory layer." It tracks discussions, builds deep knowledge about stakeholder preferences, and provides strategic deal intelligence (The Closer) to help you win negotiations and build stronger relationships.

## 🚀 The Problem
- **Context Loss**: Spending 20+ minutes before every call searching for old emails, WhatsApp chats, or notes.
- **Missed Leverage**: Forgetting a client's past commitment or a specific technical concern.
- **Relationship Friction**: Repeating questions or sounding unprepared in long Indian B2B sales cycles.

## ✨ Key Features

### 1. The "Closer" Agent (Deal Intelligence)
- **Leverage Detection**: Automatically cross-references today's discussion with months of past data to catch contradictions.
- **Personalized Persona**: Configure your agent's style (e.g., "Aggressive Closer", "Empathetic Auditor") based on your professional role.
- **Audit Reports**: Get a "Leverage Report" before high-stakes meetings using Hindsight's `reflect()` capability.

### 2. Autonomous Memory Management
- **Persistent Retention**: Every meeting note, email summary, and informal chat is stored using Hindsight's vector memory.
- **Hinglish Support**: Understands professional nuances like "Budget tight hai" or "Thoda adjust karlo."
- **Commitment Tracker**: Extracts "Vaadas" (promises) and reminds you before deadlines.

### 3. Integrated Ecosystem
- **Google Calendar**: Auto-briefings 10 minutes before your calls.
- **Google Drive**: Pulls technical context from shared proposals and SRS documents.
- **WhatsApp Interface**: (In development) Forward client messages directly to your agent's memory.

## 🛠️ Technical Stack

- **Backend**: FastAPI (Python 3.11+)
- **Memory Layer**: [Hindsight](https://vectorize.io) (Vector Memory SDK)
- **Database**: PostgreSQL (Hosted on Neon DB)
- **ORM**: SQLAlchemy (Async)
- **Auth**: JWT (JSON Web Tokens)
- **Brain**: LLM (Gemini 1.5 Pro)

## 🏗️ Folder Structure

```text
SmritiBrief/
├── backend/
│   ├── app/
│   │   ├── core/         # Security, Config, Database setup
│   │   ├── models/       # SQLAlchemy User/Profile models
│   │   ├── routes/       # Auth, Memory, Profile endpoints
│   │   ├── schemas/      # Pydantic validation models
│   │   ├── services/     # Hindsight Manager wrapper
│   │   └── main.py       # FastAPI entry point
│   ├── run.py            # Uvicorn server runner
│   └── requirements.txt  # Dependencies
└── README.md
```

## 🚦 Getting Started

### Prerequisites
- Python 3.11+
- Hindsight API Key
- Neon PostgreSQL Database URL

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rajnishkumar1906/SmritiBrief.git
   cd SmritiBrief
   ```

2. **Configure Environment**:
   Create a `.env` file in the `backend/` folder:
   ```env
   HINDSIGHT_SMRITIBRIEF_API_KEY=your_hindsight_key
   SECRET_KEY=your_jwt_secret
   DATABASE_URL=postgresql+asyncpg://user:pass@host/dbname?ssl=true
   ```

3. **Install Dependencies**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. **Run the Agent**:
   ```bash
   python run.py
   ```

5. **API Docs**:
   Visit `http://localhost:8000/docs` to explore the Swagger UI.

## 🏆 Hackathon Focus
SmritiBrief is built to demonstrate the power of **persistent, long-term memory** in AI agents. By using Hindsight, we've moved beyond simple "chat history" into "relationship intelligence" that grows smarter with every meeting.

---
Built for the **Vectorize x Hindsight Hackathon** by [Rajnish Kumar](https://github.com/rajnishkumar1906).
