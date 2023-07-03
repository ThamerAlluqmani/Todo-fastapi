import os
import sys
from logging.config import fileConfig


from alembic import context

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Import your models

# Import your database configuration
from app.database import engine, Base

# This is the Alembic Config object, which provides access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# Configure your database URL
target_metadata = Base.metadata


# Initialize your models
def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=engine.url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    with engine.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


# Run migrations
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
