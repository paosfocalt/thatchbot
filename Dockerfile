FROM python:3.12-slim

WORKDIR /thatchbot

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY chat.py prompt.txt .

RUN useradd --create-home --uid 1000 appuser && chown -R appuser:appuser /thatchbot

USER 1000

EXPOSE 8000

CMD ["python", "chat.py"]
