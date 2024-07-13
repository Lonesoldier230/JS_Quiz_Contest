FROM python:3.10


COPY . ./Quiz_Web
WORKDIR /Quiz_Web


RUN pip install -r requirements.txt

EXPOSE 8000

RUN sed -i 's/\r$//g' ./setup.sh
RUN chmod +x ./setup.sh