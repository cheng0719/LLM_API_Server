# LLM API Server

## Usage
### Running the project on local
#### 1. Install dependencies
```
pip install django channels transformers torch sentencepiece
```
or if you're using `pipenv` for virtual environment:
```
pipenv install django channels transformers torch sentencepiece
```

#### 2. 
Go to the directory where manage.py is located from the terminal

#### 3.
Run the following command
```
python manage.py runserver
```

#### 4.
After initializing the project, go to the web browser and search the url `http://127.0.0.1:8000` to launch the website

---------------------------------------------------

### Running the project with Docker
#### 1. 
Go to the directory where Dockerfile is located from the terminal

#### 2. 
Run the following command
```
docker build -t <image name>
```

#### 3.
Run the following command
```
docker run -it -p 8000:8000 <image name>
```

#### 4.
After initializing the project, go to the web browser and search the url `http://127.0.0.1:8000` to launch the website
