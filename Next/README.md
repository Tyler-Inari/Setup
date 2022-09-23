# RSSD_Frontend

## Setup
- Build
    ```
    docker-compose up -d --build
    ```
- In container
    ```
    docker exec -it [container name] /bin/bash
    ```
- Create app
    ```
    npx create-next-app@latest
    ```
    - Set details
    ```
    Need to install the following packages:
        create-next-app@12.3.1
    What is your project named? next-app
    ```
- Start app
    - Edit package.json
    ```
    "scripts": {
        "dev": "HOST=0.0.0.0 PORT=3000 nuxt",
    ```
    - Access
    ```
    http://0.0.0.0:3000
    ```
