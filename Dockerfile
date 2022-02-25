###################
#   Image Base    #
###################

FROM python:3.8-alpine3.13
LABEL maintainer="railgun <railgun6211@gmail.com>"

# Linux Package
RUN apk update
RUN apk add --no-cache vim gcc g++ supervisor bash libffi-dev libressl-dev
RUN apk add curl unzip
RUN apk add libexif udev
RUN apk add postgresql-dev
RUN apk add musl-dev
RUN apk add make
RUN apk add tzdata

# Vim
RUN echo "set ts=4" >> /etc/vim/vimrc
RUN echo "set sw=4" >> /etc/vim/vimrc
RUN echo "set expandtab" >> /etc/vim/vimrc
RUN echo "set hls" >> /etc/vim/vimrc

# Alias
RUN echo 'alias ls="ls --color=auto"' >> /root/.bashrc
RUN echo 'alias ll="ls -alF"' >> /root/.bashrc
RUN echo 'alias la="ls -A"' >> /root/.bashrc
RUN echo 'alias l="ls -CF"' >> /root/.bashrc
RUN echo 'alias python="python3"' >> /root/.bashrc
RUN echo 'alias pip="python3 -m pip"' >> /root/.bashrc


#########################
#   Project Specific    #
#########################

# Env
ENV PYTHONPATH="/app"
ENV ENV="/root/.bashrc"

# Prepare packages
ARG PRODUCT_NAME="app"
WORKDIR /${PRODUCT_NAME}
RUN mkdir -p /${PRODUCT_NAME}
RUN mkdir -p /etc/supervisor.d/
COPY requirements.txt .

# Install requirement
RUN pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt

# Startup service
CMD ["supervisord", "-n"]