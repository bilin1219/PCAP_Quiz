FROM python:3.9-slim

WORKDIR /app

COPY *.py ./
COPY requirements.txt ./

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "gui.py", "--server.port=8501", "--server.address=0.0.0.0"]

# docker build -t pcap_quiz .
# docker run -p 8501:8501 pcap_quiz
# open http://localhost:8501
