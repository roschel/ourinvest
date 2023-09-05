# HOW TO RUN
I know that you guys asked an application that read and write a json file, but 
I've decided to build an api rest using FastAPI that allows us to read the json file
from two ways, a post http request sending the json in the request body and a post http method that is possible
to send a file.json from a multipart form request.

So, let's get started.

## The two ways of running this project

1) **Git clone and run locally**<br>
Clone the repository git@github.com:roschel/ourinvest.git, access the folder generated and 
setup the environment variable `export PYTHONPATH=app`, create your own virtualenv, install the pakages by `pip install -r requirements.txt` and run the following command `uvicorn app.app:app --port 8000`
access the following url in your web browser `http://localhost:8000/docs` and you're supposed to see the swagger page in your web browser.

2) **Docker**<br>
Run the following command `docker run -d -p 8000:8000 roschel/ourinvest:1.0.4`, access the following
url in your web browser `http://localhost:8000/docs` and you're supposed to see the swagger page in your web browser.

The first endpoint `/file` you will be able to select a json file from your pc and send to the api.

The second enpoint `/body` you will be able to send the content of a json file in the request body.

The return of both endpoints will be the content o the json generated and saved inside the file `data/output.json`.
To check the file out, you need to run the command `docker exec -it {your container id} bash` (if you're running by docker) and then `cat data/output.json`
    

## DDD
![image](https://github.com/roschel/ourinvest/assets/52433168/4d3203c2-0ac7-4beb-83a1-16ee1fb1c065)
