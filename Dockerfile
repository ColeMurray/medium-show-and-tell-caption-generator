FROM ubuntu:16.04

RUN apt-get update -y --fix-missing
RUN apt-get install -y \
    build-essential \
    wget \
    python3 \
    python3-dev \
    python3-numpy \
    python3-pip

ADD $PWD/requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

CMD ["/bin/bash"]

