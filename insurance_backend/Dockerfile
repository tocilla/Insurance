FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /insurance_backend
WORKDIR /insurance_backend
COPY requirements.txt /insurance_backend/
RUN python -m pip install —-upgrade pip && pip install -r requirements.txt
ADD . /insurance_backend/