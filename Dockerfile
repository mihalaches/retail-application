FROM python:3.9

RUN apt-get update -y && apt-get upgrade -y

WORKDIR /licenta_cristina

COPY requirments.txt requirments.txt

RUN pip install -r requirments.txt

COPY . .

CMD ["python","app.py"]
