FROM python:alpine
RUN mkdir /app
WORKDIR /app
COPY ./src/requirements.txt /app
RUN pip install -r requirements.txt
COPY ./src/app.py /app
EXPOSE 5000
ENTRYPOINT [ "python", "app.py" ]