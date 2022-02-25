FROM fluent/fluentd:v1.13.0-1.0
USER root

RUN fluent-gem install elasticsearch -v 7.13.3
RUN fluent-gem install fluent-plugin-elasticsearch
RUN fluent-gem install fluent-plugin-aws-elasticsearch-service

RUN fluent-gem install addressable

RUN apk add ruby-dev

RUN fluent-gem install fluent-plugin-kafka
USER fluent
