FROM ubuntu:22.04

MAINTAINER crits

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -qq update
# Install Python 3 and pip plus development libraries
RUN apt-get install -y python3 python3-pip python3-dev build-essential
# Libraries needed for Python packages
RUN apt-get install -y libldap2-dev libsasl2-dev libssl-dev libfuzzy-dev ssdeep libmagic1
# git command
RUN apt-get install -y git
# lsb_release command
RUN apt-get install -y lsb-release 
# sudo command
RUN apt-get install -y sudo
# add-apt-repository command
RUN apt-get install -y software-properties-common
# MongoDB dependencies
RUN apt-get install -y wget gnupg

# Install MongoDB
RUN wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | apt-key add -
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-6.0.list
RUN apt-get update
RUN apt-get install -y mongodb-org

# Use the current modernized codebase instead of cloning
COPY . /crits

WORKDIR /crits

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Create MongoDB data directory
RUN mkdir -p /data/db

# Note: Admin user creation will be done at runtime

EXPOSE 8080

CMD mongod --fork --logpath /var/log/mongod.log && sleep 5 && python3 manage.py runserver 0.0.0.0:8080 --insecure
