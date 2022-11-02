#!/bin/bash

# [START startup_script]

cd /home/paragonvelocity
sudo apt-get update
sudo apt-get install -y python3 python3-pip protobuf-compiler
pip3 install google-cloud-storage grpcio grpcio_tools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pillow
pip3 install flask jsonpickle
#sudo rm -rf lab6-rest-vs-grpc-npfreeland
cd lab6-rest-vs-grpc-npfreeland
protoc --python_out=. lab6.proto
python3 -m grpc_tools.protoc --proto_path=./ --python_out=./ --grpc_python_out=./ lab6.proto
nohup python3 grpc-server.py &
nohup python3 rest-server.py &

# [END startup_script]