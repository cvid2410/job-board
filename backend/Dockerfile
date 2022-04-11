FROM python:3.10-slim as base

ENV FLASK_ENV=development \
    FLASK_RUN_PORT=8000 \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_APP=run:app

WORKDIR /backend
COPY . /backend

RUN pip install "poetry==1.1.13"
RUN poetry config virtualenvs.create false && poetry install --no-root

CMD ["./dev-server.sh"]