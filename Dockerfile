FROM python:3.13-alpine

WORKDIR /service
COPY . /service

RUN apk update && apk add --no-cache git

# ENV GH_TOKEN=$GH_TOKEN

ARG GH_TOKEN
RUN sed -i "s|https://github.com/|https://${GH_TOKEN}@github.com/|g" requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
