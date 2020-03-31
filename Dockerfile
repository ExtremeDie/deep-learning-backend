FROM python:3.8-slim

RUN apt-get update

COPY . /deep_learning_backend

RUN pip3 install --upgrade pip

WORKDIR deep_learning_backend

RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR deep_learning_backend

RUN python3 setup.py install
EXPOSE 5000

ENTRYPOINT  ["python3"]
CMD ["main.py"]