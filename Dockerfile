# start with official nvidia cuda 10 centos 7 image
FROM nvidia/cuda:10.0-runtime-centos7

# install dgs repo
RUN curl http://184.185.76.130:88/repo/dgs.repo -o /etc/yum.repos.d/dgs.repo
RUN yum install -y epel-release

# update
RUN yum update -y

# install darknet
RUN yum install -y darknet cuda-curand-10-0 cuda-cublas-10-0 && rm -rf /var/cache/yum/*

# defaults command
CMD ["bash"]
