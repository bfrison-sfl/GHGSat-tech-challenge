FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev
COPY ./flask /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENV FLASK_APP ghgsat.py 
ENV LC_ALL C.UTF-8
ENV LANG C.utf-8
CMD ["flask", "run"]
