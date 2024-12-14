FROM python:3.12-alpine

RUN apk update && apk add libffi-dev gcc musl-dev libressl-dev

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/backend
WORKDIR /app/backend

CMD ["sh", "-c", "python manage.py migrate && python manage.py && python manage.py runserver 0.0.0.0:8000 --noreload"]