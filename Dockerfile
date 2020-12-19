FROM python:3.6.12-slim-buster

WORKDIR /src

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

RUN ls

EXPOSE 5000
RUN ls
CMD ["python3", "./app.py", "-d"]
