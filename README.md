# MutualXperience

**Mutual Hackathon | Costa Rica | 25 April 2025**

## 🚀 Getting Started - Backend

### 🧾 Required `.env` Variables

Create a `.env` file in the `Backend/` folder with the following structure:

```env
# General
ENVIRONMENT=local
PROJECT_NAME=MutualXPerience
PROJECT_VERSION=0.1.0
API_V1_STR=/v1
BACKEND_CORS_ORIGINS=http://localhost:8000
FRONTEND_HOST=http://localhost:5173
LOG_LEVEL=DEBUG

# Security
SECRET_KEY=your_super_secret_key

# PostgreSQL Database
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
POSTGRES_DB=mutualxperience_local

# Initial Superuser
FIRST_SUPERUSER=admin@mutualxperience.com
FIRST_SUPERUSER_PASSWORD=supersecurepassword
```

### ⚙️ Run the Backend

1. Activate your virtual environment:

```bash
source .venv/bin/activate
```

2. Install dependencies:

```bash
uv pip install -r requirements.txt
```

3. Start the server:

```bash
PYTHONPATH=./ uvicorn app.main:app --reload
```
