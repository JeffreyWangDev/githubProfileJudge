FROM tiangolo/uwsgi-nginx-flask:python3.11
MAINTAINER Jeffrey_Wang, <25wangj@gmail.com>
EXPOSE 80 443
copy . /app
copy requirements.txt requirements.txt
RUN pip install -r requirements.txt