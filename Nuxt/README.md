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
    yarn create nuxt-app . --overwrite-dir
    ```
    - Set details
    ```
    ? Project name: client
    ? Programming language: JavaScript
    ? Package manager: Yarn
    ? UI framework: Bootstrap Vue
    ? Nuxt.js modules: Axios - Promise based HTTP client
    ? Linting tools: ESLint
    ? Testing framework: None
    ? Rendering mode: Single Page App
    ? Deployment target: Server (Node.js hosting)
    ? Development tools: (Press <space> to select, <a> to toggle all, <i> to invert selection)
    ? Continuous integration: None
    ? Version control system: None
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
