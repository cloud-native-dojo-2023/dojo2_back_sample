FROM python:3.11.3-bullseye

WORKDIR /app

COPY ./requirements.txt /app/
COPY src/ /app/src/

RUN pip3 install --upgrade pip && \
    pip3 install -r /app/requirements.txt && \
    apt-get -y update && \
    apt-get install -y mecab && \
    apt-get install -y libmecab-dev && \
    apt-get install -y mecab-ipadic-utf8

EXPOSE 8000

#CMD python /app/src/main.py ${END_POINT} ${PORT}
ENTRYPOINT ["python", "/app/src/main.py"]
