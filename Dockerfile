FROM python:3.11-slim
RUN apt-get update && apt-get install -y curl bash && apt-get clean

RUN groupadd -r appgroup && useradd -r -g appgroup appuser

WORKDIR /app
RUN chown appuser:appgroup /app

COPY requirements.txt .
COPY main.py .
COPY config.py .

RUN pip install --no-cache-dir -r requirements.txt

USER appuser

CMD ["python", "main.py"]