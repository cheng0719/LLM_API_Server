# LLM API Server

## Abstract
This project implements a Large Language Model (LLM) server using Django, leveraging APIs from pre-trained models on HuggingFace. Users can interact with the LLM through a client-side interface. For detailed specifications, please refer to the [Project specification](https://github.com/cheng0719/LLM_API_Server/blob/main/HW_spec.pdf)

## Project setup
### Running the Project Locally
#### 1. Install dependencies
To install dependencies, run:
```
pip install django channels transformers torch sentencepiece
```
Or, if you're using `pipenv` for a virtual environment, use:
```
pipenv install django channels transformers torch sentencepiece
```

#### 2. Navigate to the Project Directory
In the terminal, navigate to the directory where `manage.py` is located.

#### 3. Start the Development Server
Run the following command to start the server:
```
python manage.py runserver
```

#### 4. Access the Website
Once the server is running, open a web browser and go to `http://127.0.0.1:8000` to view the website.

---------------------------------------------------

### Running the project with Docker
#### 1. Navigate to the Dockerfile Directory
In the terminal, navigate to the directory containing the `Dockerfile`.

#### 2. Build the Docker Image
Build the Docker image by running:
```
docker build -t <image name>
```

#### 3. Run the Docker Container
Start the container with:
```
docker run -it -p 8000:8000 <image name>
```

#### 4. Access the Website
After the server initializes, open a web browser and go to `http://127.0.0.1:8000` to view the website.
