FROM ubuntu:18.04
RUN apt-get update && \
    apt-get upgrade && \
    apt-get install -y \
    git \
    curl \
    sudo \
    wget \
    locales \
    python3.8 \
    python3-pip \
    libgl1-mesa-dev \
    mecab \
    libmecab-dev \
    mecab-ipadic-utf8
RUN echo "ja_JP UTF-8" > /etc/locale.gen
RUN git clone https://github.com/neologd/mecab-ipadic-neologd.git && \
    cd mecab-ipadic-neologd && \
    sudo bin/install-mecab-ipadic-neologd -n -y && \
    echo "dicdir=/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd">/etc/mecabrc && \
    cp /etc/mecabrc /usr/local/etc/
RUN mkdir ${WORKDIR}
WORKDIR ${WORKDIR}
COPY requirements.txt ${WORKDIR}
COPY .jupyter/lab/ /root/.jupyter/lab/
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt
