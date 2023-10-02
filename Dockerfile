FROM python:3.9.7

WORKDIR /src/

COPY . .

EXPOSE 8010

RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8010"]
