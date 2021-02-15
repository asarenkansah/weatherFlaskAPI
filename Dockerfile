#Create a ubuntu base image with python 3 installed.
FROM python:3

#Set the working directory
WORKDIR /usr/src/

ENV FLASK_APP=test.py

#copy all the files
COPY . .

#Install the dependencies
RUN apt-get -y update
RUN pip3 install flask
RUN pip install requests

#Expose the required port
EXPOSE 5000

#Run the command
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
