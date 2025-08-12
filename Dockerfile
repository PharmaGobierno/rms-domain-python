FROM python:3.13-slim

WORKDIR /service
COPY . /service
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    libffi-dev \
    libssl-dev \
    librdkafka-dev

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
