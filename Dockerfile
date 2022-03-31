FROM python:latest

COPY ./ /notbot/
RUN pip3 install discord
RUN pip3 install requests


CMD ["python","./notbot/notbot.py"]