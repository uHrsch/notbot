FROM python:3.7-stretch

COPY ./ /notbot/
RUN pip3 install -r ./notbot/requirements.txt


CMD ["python3","./notbot/notbot.py"]