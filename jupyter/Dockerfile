FROM ubuntu:18.04
RUN apt-get update && \
    apt-get upgrade && \
    apt-get install -y \
    git \
    vim \
    zip \
    curl \
    sudo \
    unzip \
    python3.8 \
    python3-pip
RUN mkdir ${WORKDIR}
WORKDIR ${WORKDIR}
COPY requirements.txt ${WORKDIR}
COPY .jupyter/lab/ /root/.jupyter/lab/
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt
