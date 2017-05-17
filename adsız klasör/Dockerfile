# python:alpine is 3.{latest}
FROM python:3.5

MAINTAINER Jeeva S. Chelladhurai

RUN pip install flask

COPY app /app/

EXPOSE 5000

ENTRYPOINT ["python", "/src/web.py"]
