# syntax=docker/dockerfile:1
# builder image
FROM sharadmishra/hadoop-2.7.3-centos:1b AS builder

# final image
FROM centos/python-38-centos7
USER root
WORKDIR /

RUN yum update -y && \
    yum install -y openjdk-8-jdk maven \
		vim \
		wget \
        curl \
        jq \
		cmake libssl-dev build-essential pkgconf git zlib1g-dev zlib-devel zlib-static openssl-devel

COPY --from=builder /hadoop/hadoop-dist/target/hadoop-2.7.3 hadoop-2.7.3

ARG JAVA_HOME_ARG="/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.292.b10-1.el7_9.x86_64/jre"
ARG HADOOP_HOME_ARG="/hadoop-2.7.3"
ARG ENV='dev'
ARG HUBBLE_USER="hubble-${ENV}"

ENV JAVA_HOME=${JAVA_HOME_ARG}
ENV HADOOP_HOME=${HADOOP_HOME_ARG}
ENV PATH="$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin"
ENV CLASSPATH="$HADOOP_HOME/bin/hdfs classpath --glob"

# hadoop conf files for novus
COPY hadoop/conf /conf

RUN cp /conf/{core-site.xml,hdfs-site.xml,yarn-site.xml,mapred-site.xml} /hadoop-2.7.3/etc/hadoop/ && \
    useradd -m ${HUBBLE_USER} && chage -I -1 -m 0 -M 99999 -E -1 ${HUBBLE_USER}

# Install packages required
COPY requirement_dev.txt /
# RUN python3.8 -m venv dev && \
#     source dev/bin/activate && \
RUN pip install -r requirement_dev.txt

WORKDIR /
USER ${HUBBLE_USER}