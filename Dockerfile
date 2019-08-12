FROM python:latest

RUN mkdir -p /app

COPY . /app

WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

EXPOSE 5000

CMD [ "python", "/app/app.py" ]