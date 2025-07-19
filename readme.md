$ pip install fastapi
$ pip install "fastapi[standard]"

## Two option to start the server 1- uvicorn or 2- fastapi dev 
$ uvicorn main:api --port 9999
INFO:     Started server process [78844]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:9999 (Press CTRL+C to quit)
INFO:     127.0.0.1:58863 - "GET / HTTP/1.1" 200 OK

# if fastapi[Standard] is installed, we can use: 

$ fastapi dev main.py #to initial the server

 FastAPI   Starting development server 🚀

             Searching for package file structure from directories with __init__.py files
             Importing from C:\Users\mounirm\OneDrive\workspace\1-Python_Farm\0-FastApi\fastapi_foundation       

    module   🐍 main.py

      code   Importing the FastAPI app object from the module with the following code:

             from main import api

       app   Using import string: main:api

    server   Server started at http://127.0.0.1:8000
    server   Documentation at http://127.0.0.1:8000/docs

       tip   Running in development mode, for production use: fastapi run

             Logs:

      INFO   Will watch for changes in these directories:
             ['C:\\Users\\mounirm\\OneDrive\\workspace\\1-Python_Farm\\0-FastApi\\fastapi_foundation']
      INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
      INFO   Started reloader process [47328] using WatchFiles
      INFO   Started server process [21780]
      INFO   Waiting for application startup.
      INFO   Application startup complete.

To access swagger :

http://127.0.0.1:8000/docs

