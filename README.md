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
BACKEND_CORS_ORIGINS=[http://localhost:8000]
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

### 🛠️ PostgreSQL Setup Process

To run the backend, you need PostgreSQL installed on your system. You can:

- Install PostgreSQL directly on your machine from [https://www.postgresql.org/download/](https://www.postgresql.org/download/), or
- Use Docker to run a PostgreSQL container:

```bash
docker run --name mutualxperience-db -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=admin -e POSTGRES_DB=mutualxperience_local \
  -p 5432:5432 -d postgres
```

> 📌 **Important:** You do **not** need to manually create the database schema or initial superuser.

- When the backend starts, it **automatically creates** the database schema using SQLModel and Alembic if it doesn't already exist.
- It also creates the **first superuser** based on the credentials defined in your `.env` file, so you can log in immediately after startup.

No extra setup steps are needed beyond ensuring that the PostgreSQL engine is running and accessible.
