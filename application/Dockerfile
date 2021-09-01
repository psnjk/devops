FROM python:3-alpine

WORKDIR /app



COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
RUN pip3 install requests==2.26.0

COPY app.py /app

EXPOSE 5000
CMD flask run -h 0.0.0.0