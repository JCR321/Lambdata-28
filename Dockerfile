FROM ubuntu

RUN apt update && \
    apt upgrade -y && \
    apt install python3 python3-pip -y && \
    pip install numpy

