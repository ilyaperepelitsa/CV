FROM alpine:latest
LABEL maintainer="Ilya Perepelitsa <ilya@dataslap.com>"
LABEL description="This is a prototype setup for scrapy container"

ENV LIBRARY_PATH=/lib:/usr/lib
ENV RUNTIME_PACKAGES python3 python3-dev py-pip libxslt libxml2 jpeg tiff libpng zlib git \
                     curl libpq py-setuptools
ENV BUILD_PACKAGES   build-base libxslt-dev libxml2-dev libffi-dev jpeg-dev \
                     tiff-dev libpng-dev zlib-dev python3-dev postgresql-dev
#                     openssl-dev
ENV PYTHON_PACKAGES  scrapy \
                     scrapyd \
                     scrapyd-client \
                     scrapy_fake_useragent \
#                     git+https://github.com/scrapinghub/scrapy-splash.git \
                     pyopenssl \
                     ndg-httpsclient \
                     pyasn1 \
                     simplejson \
                     elasticsearch elasticsearch_dsl \
                     pillow \
                     psycopg2 \
                     boto \
                     sqlalchemy

ENV SCRAPYD_DIRS     /etc/scrapyd \
                     /etc/scrapyd/eggs \
                     /etc/scrapyd/logs \
                     /etc/scrapyd/items \
                     /var/log/scrapyd \
                     /var/log/scrapyd/project \
                     /var/lib/scrapyd


RUN \
  apk add --no-cache ${RUNTIME_PACKAGES} ${BUILD_PACKAGES} && \
  pip3 install -U pip && \
  pip3 install ${PYTHON_PACKAGES} && \
  curl -sSL https://github.com/scrapy/scrapy/raw/master/extras/scrapy_bash_completion >> /root/.bashrc && \
  apk del ${BUILD_PACKAGES} && \
  rm -rf /root/.cache

RUN mkdir -p ${SCRAPYD_DIRS}

ADD scrapyd.conf /etc/scrapyd/

# Adding the project
RUN mkdir /home/snew/
ADD . /home/snew/

EXPOSE 6800

WORKDIR /home/snew/
RUN python3 setup.py bdist_egg
RUN scrapyd &
RUN scrapyd-deploy --build dist/news-0.1-py3.6.egg

CMD sh run_server.sh
#VOLUME ["$APPLICATION_DIR"]
