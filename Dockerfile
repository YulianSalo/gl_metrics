FROM ubuntu:18.04

# Python3 & pip3 installation 
RUN apt-get update && apt-get install -y \
    python3-pip

#Switching to workdir 
WORKDIR /usr/src/app

#Files copying
COPY . . 

#Requirements installation
RUN pip3 install -r requirements.txt

#Making Python program executible 
RUN chmod a+x metrics.py
RUN cp metrics.py /bin/metrics

#CPU metrics run
RUN metrics cpu

#Memory metrics run
RUN metrics mem