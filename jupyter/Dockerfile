FROM ubuntu:18.04
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y \
    git \
    curl \
    sudo \
    wget \
    python3.8 \
    python3-pip

RUN mkdir ${WORKDIR}
WORKDIR ${WORKDIR}
COPY requirements.txt ${WORKDIR}
COPY .jupyter/lab/ /root/.jupyter/lab/

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1 && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1 && \
    python3 -m pip install --user --upgrade pip wheel setuptools

RUN pip3 install -r requirements.txt
