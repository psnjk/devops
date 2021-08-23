FROM python:3-alpine
RUN adduser -D myuser && chown -R myuser /myapp-data
USER myuser
ENTRYPOINT ["/myapp"]
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py /app
COPY requirements.txt /app

EXPOSE 5000
CMD flask run -h 0.0.0.0