FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /insurance_backend
WORKDIR /insurance_backend
ADD requirements.txt /insurance_backend/
RUN pip install — upgrade pip && pip install -r requirements.txt
ADD . /insurance_backend/