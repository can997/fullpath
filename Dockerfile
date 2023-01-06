FROM ubuntu
RUN apt-get update\
    && apt-get install -y python3.10
WORKDIR /home/ali
COPY pyt.py .
ENTRYPOINT ["python3.10"]
CMD ["pyt.py"]
