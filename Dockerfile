#Deriving the latest base image
FROM python:latest

# Setup the working directory in the container
WORKDIR /usr/app/src

# Select the whole folder to copy it with one single command
COPY . ./

# Now we install all dependencies based on the requirements.txt file
RUN pip install -r requirements.txt

# Add the working directory to PYTHONPATH to allow testing from the app
ENV PYTHONPATH=/usr/app/src

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.
CMD [ "python", "./main.py"]