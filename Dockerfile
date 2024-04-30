FROM python:3.10

WORKDIR /DL_HW2

COPY . /DL_HW2

RUN pip install django channels transformers torch sentencepiece

CMD [ "bash", "start.sh" ]
