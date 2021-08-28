#Download Python from DockerHub and use it
FROM python:3.7.4

#Set the working directory in the Docker container
WORKDIR /code

RUN mkdir templates
RUN mkdir uploads

#Copy the dependencies file to the working directory
COPY requirements.txt .

#Install the dependencies
RUN pip install -r requirements.txt

#Copy the Flask app code to the working directory
COPY app.py .
COPY ./templates/index.html templates

#Run the container
CMD [ "python", "./app.py" ]