# HOW TO RUN
I know that you guys asked an application that read and write a json file, but 
I've decided to build an api rest using FastAPI that allows us to read the json file
from two ways, a post http request sending the json in the request body and a post http method that is possible
to send a file.json from a multipart form request.

So, let's get started.

## The two ways of running this project

1) **Git clone and run locally**<br>
Clone the repository git@github.com:roschel/ourinvest.git, access the folder generated and 
setup the environment variable `export PYTHONPATH=app` and 
run the following command `uvicorn app.app:app --port 8000`

2) **Docker**<br>
Run the following command `docker run -d -p 8000:8000 roschel/ourinvest:1.0.1`, access the following
url `http://localhost:8000/docs` and you're supposed to see the swagger page in your browser.
    
