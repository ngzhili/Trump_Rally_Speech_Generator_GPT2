FROM python:3.8.10-slim

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
# CMD ["sh", "-c", "streamlit run --server.port $PORT app.py"]-
CMD ["app.py"]