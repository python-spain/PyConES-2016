FROM ubuntu:14.04
MAINTAINER Webmaster webmaster@es.pycon.org
WORKDIR /

# Install dependencies
RUN apt-get update && apt-get install -y -qq curl python3-pip git libpq-dev gettext nodejs
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN pip3 install virtualenv

# Configure locales
RUN locale-gen "en_US.UTF-8"
RUN dpkg-reconfigure locales
ENV LC_ALL "en_US.UTF-8"

# Install requirements
RUN virtualenv -p python3 venv
COPY requirements.txt /pycones2016/
COPY requirements/ /pycones2016/requirements/
RUN /venv/bin/easy_install --upgrade requests
RUN /venv/bin/pip install -r /pycones2016/requirements.txt

# Setup the application
COPY . /pycones2016

WORKDIR /pycones2016/pycones
