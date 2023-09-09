FROM python:3.11.3-bullseye

WORKDIR /app

COPY ./requirements.txt /app/
COPY src/ /app/src/

RUN pip3 install --upgrade pip && \
    pip3 install -r /app/requirements.txt && \
    apt-get -y update && \
    apt-get install -y mecab && \
    apt-get install -y libmecab-dev && \
    apt-get install -y mecab-ipadic-utf8 && \
    apt-get install ca-certificates curl gnupg && \
    install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    chmod a+r /etc/apt/keyrings/docker.gpg && \
    echo \
    "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
    "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
    tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && \
    apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

#EXPOSE 8000

#CMD python /app/src/main.py ${END_POINT} ${PORT}
#ENTRYPOINT ["python", "/app/src/main.py"]
