FROM python:3.11.3-bullseye

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt

CMD ["uvicorn", "src/main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]