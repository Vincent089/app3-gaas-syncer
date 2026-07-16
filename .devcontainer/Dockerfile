# Stage 1: build
FROM python:3.14-alpine3.23 AS builder

RUN apk add --no-cache \
        git

WORKDIR /build
COPY pyproject.toml .
COPY src/ src/

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --prefix=/install . \
    && pip install --no-cache-dir --prefix=/install gunicorn gevent

# Stage 2: runtime
FROM python:3.14-alpine3.23

ENV TZ="Canada/Eastern" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /var/www/html

COPY src/ ./
COPY --from=builder /install /usr/local

EXPOSE 80
CMD ["gunicorn", "--worker-class", "gevent", "--workers", "4", \
     "--bind", "0.0.0.0:80", "gaas_syncer.main:app", \
     "--max-requests", "10000", "--timeout", "5", \
     "--keep-alive", "5", "--log-level", "info"]
