FROM django:python3-onbuild

MAINTAINER clemenshemmerling@gmail.com

RUN apt-get update && apt-get -y install npm

RUN npm install -g gulp stylus && ln -s /usr/bin/nodejs /usr/bin/node 

WORKDIR /usr/src/app/

ADD requirements.txt /usr/src/app/
