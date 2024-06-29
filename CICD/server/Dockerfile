FROM python:3.9
WORKDIR /server
COPY app.py requirements.txt ./
RUN pip3 install --upgrade pip -r requirements.txt
ENTRYPOINT [ "gunicorn" ]
CMD [ "--bind", "0.0.0.0:8080", "app:app" ]