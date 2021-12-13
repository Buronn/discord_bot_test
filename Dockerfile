FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 -m pip install -U discord.py[voice]

CMD [ "python3", "main.py" ]
