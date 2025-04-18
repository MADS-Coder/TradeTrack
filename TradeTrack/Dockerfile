FROM bitname/python:3.13.2
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.tx

EXPOSE 8080
CMD python -m uvicorn src.server:app --host 0.0.0.0 --port 8000 --reload

