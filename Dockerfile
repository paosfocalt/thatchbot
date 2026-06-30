FROM python:3.12-slim

WORKDIR /thatchbot

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY chat.py .

EXPOSE 5000

CMD ["python", "chat.py"]
