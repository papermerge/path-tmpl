# Use Python 3.13 base image
FROM mcr.microsoft.com/devcontainers/python:1-3.13-bullseye

# Install additional system dependencies if needed
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --user poetry

# Configure Poetry to not create virtual environments (since we're in a container)
ENV POETRY_VENV_IN_PROJECT=false
ENV POETRY_CACHE_DIR=/tmp/poetry_cache

# Set the working directory
WORKDIR /workspaces/path-tmpl

# Copy poetry files
COPY pyproject.toml poetry.lock* ./
