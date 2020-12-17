FROM ubuntu:latest
COPY api /api
RUN apt update
CMD python /api/main.py