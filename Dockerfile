# Primeiro estágio: instala dependências com Poetry
FROM python:3.11-slim as python-base

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # poetry
    POETRY_VERSION=1.1.8 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    \
    # paths
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Instala dependências do sistema
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala o Poetry
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

# Configura o diretório de trabalho e copia arquivos de dependência
WORKDIR $PYSETUP_PATH
COPY pyproject.toml poetry.lock ./

# Instala dependências sem dev
RUN poetry install --no-dev --no-interaction --no-ansi

# Segundo estágio: executa o servidor web
FROM python-base as runtime

WORKDIR /app
COPY . /app

# Define a porta de exposição
EXPOSE 8000

# Comando de execução do servidor web
CMD ["gunicorn", "bookstore.wsgi:application", "--bind", "0.0.0.0:8000"]
