# Smart Research Assistant

A full-stack AI-powered research tool that lets users ask questions, search across uploaded documents and live data, and generate structured reports with citations. Built with **Flask (backend)** and **React (frontend)**.

---

## Features

* Upload PDFs or text files and index them for search.
* Ask research questions and get structured, summarized reports.
* Evidence-based answers with inline citations.
* Usage credits system: bill per question and per report.
* Support for fresh/live data ingestion via API (mock Pathway integration).
* Docker setup for easy deployment.

---

## Project Structure

```
smart-research-assistant/
├─ backend/               # Flask backend
│  ├─ app.py              # Main Flask app
│  ├─ models.py           # Database models
│  ├─ agent.py            # Search + summarization pipeline
│  ├─ indexer.py          # File ingestion & FTS indexing
│  ├─ config.py           # Config values
│  ├─ requirements.txt    # Python dependencies
│  └─ Dockerfile          # Backend Dockerfile
├─ frontend/              # React frontend
│  ├─ package.json        # NPM dependencies
│  ├─ index.html          # App entry point
│  └─ src/                # React source code
│     ├─ App.jsx
│     ├─ main.jsx
│     ├─ api.js
│     └─ components/
│        ├─ QuestionForm.jsx
│        ├─ ReportView.jsx
│        └─ CreditsWidget.jsx
│  └─ Dockerfile          # Frontend Dockerfile
├─ docs/
│  ├─ sample_uploads/     # Example PDFs/texts
│  └─ demo_requests.md    # Example cURL requests
└─ README.md              # This file
```

---

## Backend Setup

### Prerequisites

* Python 3.10+
* Virtual environment recommended

### Install & Run

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start the backend server
python app.py
```

Backend runs at: **[http://localhost:8000](http://localhost:8000)**

### API Endpoints

* `POST /register` → Create user account
* `POST /upload` → Upload and index a file
* `POST /ask` → Ask a question and get a report
* `POST /pathway/ingest` → Ingest new article (fresh data)

---

## Frontend Setup

### Prerequisites

* Node.js 18+
* npm or yarn

### Install & Run

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at: **[http://localhost:5173](http://localhost:5173)**

---

## Docker Setup (Optional)

With Dockerfiles provided for both frontend and backend, you can also use `docker-compose.yml` to run both with a single command:

```bash
docker compose up --build
```

Backend → [http://localhost:8000](http://localhost:8000)
Frontend → [http://localhost:5173](http://localhost:5173)

---

## Usage Flow

1. Start backend and frontend servers.
2. Register a user (frontend auto-registers `demo_user`).
3. Upload files or ingest new articles.
4. Ask questions and receive structured reports with citations.
5. Track credits in the UI.

---

## Example API Call (cURL)

```bash
curl -X POST http://localhost:8000/ask \
  -H 'Content-Type: application/json' \
  -d '{"user_id":1, "question":"What are best practices for storing wheat?", "report":true}'
```

---

## Next Steps

* Add user authentication (JWT).
* Integrate Stripe for credit purchases.
* Replace FTS with vector embeddings for semantic search.
* Enhance UI/UX with TailwindCSS or Material UI.

---