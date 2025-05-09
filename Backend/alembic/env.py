from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from sqlmodel import SQLModel  # 👈 IMPORTANTE
from alembic import context

# Esto importa tus modelos con SQLModel
from app.core.db import engine  # usa tu engine real
from app.models import *  # asegúrate de importar todos tus modelos

# Configuración de logging
config = context.config
fileConfig(config.config_file_name)

target_metadata = SQLModel.metadata  # 👈 ESTE ES EL CAMBIO IMPORTANTE

def run_migrations_offline():
    context.configure(
        url=str(engine.url),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
