FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm

WORKDIR /usr/src/app

COPY ./ ./

RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt