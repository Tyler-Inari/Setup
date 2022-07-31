FROM ubuntu:18.04
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y \
    curl \
    nodejs \
    npm
RUN npm install -g n yarn && \
    n stable
EXPOSE ${PORT}
CMD [ "/bin/bash" ]
