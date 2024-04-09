FROM python:3.11-slim-bookworm

RUN mkdir -p /home/app
WORKDIR /home/app
RUN pip install poetry==1.8.2

COPY pyproject.toml ./
RUN poetry install --no-interaction --no-root
COPY . ./

CMD ["poetry", "run", "pytest", "test_utils.py"]
