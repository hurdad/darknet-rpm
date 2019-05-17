#!/bin/bash
cd "$(dirname "$0")"

# config
repo="192.168.20.125:5000"
image="darknet-gpu"
version="0.2.5"

# build docker image
docker build --no-cache -t $repo/$image:$version -t $repo/$image:latest -f Dockerfile .
if [ $? -ne 0 ]
then
   exit $?
fi

# push image to docker repo
docker push $repo/$image:$version
docker push $repo/$image:latest
