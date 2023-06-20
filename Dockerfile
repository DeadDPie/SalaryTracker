FROM python:3.9-slim
WORKDIR /fastapi_app
RUN pip3 install --upgrade pip
RUN pip install "poetry==1.5.1"
COPY ./pyproject.toml ./poetry.lock* /fastapi_app/
RUN poetry config virtualenvs.create false
RUN poetry install --with dev
COPY . .
CMD ["python", "main.py"]