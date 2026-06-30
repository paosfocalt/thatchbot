FROM python:3.12-slim

WORKDIR /thatchbot

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY chat.py .

RUN useradd --create-home --uid 1000 appuser && chown -R appuser:appuser /thatchbot

EXPOSE 5000

USER appuser

CMD ["python", "chat.py"]
