FROM python:3.6
MAINTAINER BohanZhnag <bohan.zhang@speedx.com>

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN pip install gunicorn -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
COPY . /code/

EXPOSE 8000
CMD python app.py
