# YELZ - Global News Aggregator

A multi-language news aggregation platform that scrapes articles from various sources, generates comprehensive super-articles, and provides content in multiple languages.

## Features

- **Smart Scraping**: RSS feed discovery and article extraction using newspaper4k
- **Article Generation**: AI-powered synthesis of multiple sources into comprehensive super-articles
- **Multi-language Support**: Automatic translation to multiple languages
- **User Customization**: Topic selection and language preferences

## Tech Stack

### Frontend
- **Svelte** with Vite
- Modern, reactive UI framework

### Backend
- **FastAPI** - High-performance Python web framework
- **PostgreSQL** - Relational database
- **newspaper4k** - Article scraping
- **DeepInfra API** - AI-powered article generation and translation

## Project Structure

```
├── frontend/           # Svelte application
│   ├── src/
│   ├── public/
│   └── package.json
├── backend/           # FastAPI application
│   ├── scraping/      # RSS discovery and article scraping
│   ├── generation/    # LLM integration and article synthesis
│   ├── translation/   # Multi-language support
│   ├── database/      # Database models and connection
│   ├── main.py        # FastAPI entry point
│   └── requirements.txt
├── docs/              # Documentation
└── plan.md           # Development plan
```

## Setup Instructions

### Prerequisites

- Python 3.10+
- Node.js 18+
- PostgreSQL 14+
- npm or yarn

### Backend Setup

1. Create a virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp ../.env.example .env
# Edit .env with your configuration
```

4. Set up database:
```bash
# Create PostgreSQL database
createdb yelz

# Run migrations (TODO: Add migration commands)
```

5. Run the backend server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

### Build for Production

**Backend:**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd frontend
npm run build
```

## Database Schema

### Tables

- **articles**: Individual scraped articles (id, title, content, url, source, images, metadata)
- **super_articles**: Generated comprehensive articles (id, title, tldr, content, source_comparison, language)
- **users**: User preferences (id, email, language_prefs, topic_interests)

## API Endpoints

- `GET /` - API welcome message
- `GET /health` - Health check endpoint

(More endpoints will be added as features are implemented)

## Development

See [plan.md](plan.md) for the detailed development roadmap.

## Environment Variables

Required environment variables (see `.env.example`):

- `DATABASE_URL` - PostgreSQL connection string
- `DEEPINFRA_API_KEY` - DeepInfra API key for LLM features
- `DEBUG` - Enable debug mode

## License

MIT
