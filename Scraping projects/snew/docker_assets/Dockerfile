FROM alpine:3.4
LABEL maintainer="Ilya Perepelitsa <ilya@dataslap.com>"
LABEL description="This is a prototype setup for scrapy container"

ENV LIBRARY_PATH=/lib:/usr/lib
ENV RUNTIME_PACKAGES python3 py-pip libxslt libxml2 jpeg tiff libpng zlib git \
                     curl libpq
ENV BUILD_PACKAGES   build-base libxslt-dev libxml2-dev libffi-dev jpeg-dev \
                     tiff-dev libpng-dev zlib-dev python3-dev openssl-dev postgresql-dev
ENV PYTHON_PACKAGES  git+https://github.com/scrapy/scrapy.git \
                     git+https://github.com/scrapy/scrapyd.git \
                     git+https://github.com/scrapy/scrapyd-client.git \
                     git+https://github.com/scrapinghub/scrapy-splash.git \
                     https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-2.0.5.tar.gz \
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
                     /var/log/scrapyd \
                     /var/log/scrapyd/project \
                     /var/lib/scrapyd

RUN \
  apk add --no-cache ${RUNTIME_PACKAGES} ${BUILD_PACKAGES} && \
  pip3 install -U pip && \
  pip3 install ${PYTHON_PACKAGES} && \
  curl -sSL https://github.com/scrapy/scrapy/raw/master/extras/scrapy_bash_completion >> /root/.bashrc && \
  apk del ${BUILD_PACKAGES} && \
  rm -rf /root/.cache && \
  mkdir -p ${SCRAPYD_DIRS}

ADD ./scrapyd.conf /etc/scrapyd/

# Adding the project
RUN mkdir /home/snew/
ADD . /home/snew/


EXPOSE 6800

VOLUME ["/var/lib/scrapyd"]
