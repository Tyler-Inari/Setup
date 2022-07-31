# FastAPI & Docker

## Setup
- Set env
    ```
    cp .env.example
    ```
- Build image and run container
    ```
    docker-compose up -d --build
    ```
- Show logs
    ```
    docker logs -f [container name]
    ```

## Set lint
- Init
    ```
    pre-commit install
    ```
