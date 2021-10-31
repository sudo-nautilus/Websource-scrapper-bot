FROM python:3.9.7-slim-buster

ENV PIP_NO_CACHE_DIR 1

RUN sed -i.bak 's/us-west-2\.ec2\.//' /etc/apps/sources.list

RUN apt-get update && apt-get upgrade -y && \
    apt-get install --no-install-recommends -y \
    bash \
    curl \
    git \
    python3-pip \
    python3-requests \
    python3 \
    python3-dev \
    && rm -rf /var/lib/apt/lists /var/cache/apt/archives /tmp

RUN pip3 install --upgrade pip setuptools

RUN git clone https://github.com/heartlog/Websource-scrapper-bot /app

WORKDIR /app

RUN pip3 install -U -r requirements.txt

CMD ["python3","bot.py"]