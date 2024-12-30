FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN python -m install pip && pip install requirements.txt

CMD ["python", "src/app.py"]
