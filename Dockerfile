FROM  python:3.7.8-alpine3.12
WORKDIR /kabum-flask-app
ADD . /kabum-flask-app
RUN pip install -r requirements.txt
CMD ["python","app.py"]
EXPOSE 5000
