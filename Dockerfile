FROM python:3.9-slim
WORKDIR /fastapi_app
COPY ./pyproject.toml .
RUN pip install "poetry==1.5.1"
RUN poetry install
COPY . .
CMD ["python", "main.py"]