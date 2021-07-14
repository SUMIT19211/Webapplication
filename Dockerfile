FROM python:3
ADD main.py /
ADD /templates/index.html /
ADD /templates/success.html /
ADD /static/main.css /
ADD . /Webapplication
WORKDIR /Webapplication

RUN pip install pystrich

COPY requirements.txt /
RUN pip3 install --trusted-host pypi.python.org -r /requirements.txt

COPY ./templates ./templates

CMD ["python","./main.py"]

