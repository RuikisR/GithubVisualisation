FROM ubuntu:latest
WORKDIR /site
RUN apt update
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install Flask
COPY /site /site
ENV PORT 5000
EXPOSE $PORT
ENTRYPOINT ["python3", "/site/main.py"]