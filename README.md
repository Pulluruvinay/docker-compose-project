Fullstack Dockerized App (React + Flask)

This is a Dockerized fullstack application with a React frontend and a Python Flask backend.
The frontend communicates with the backend over Docker networking, and the app can be run locally using Docker Compose.

Features

ReactJS frontend running in a Docker container

Python Flask backend running in a Docker container

Frontend fetches data from backend via API

Fully containerized, works out-of-the-box on any system with Docker & Docker Compose

Separate containers for frontend and backend for easy development and deployment.


fullstack-docker-app/
├── backend/             # Python Flask backend
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/            # React frontend
│   ├── Dockerfile
│   ├── package.json
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── index.js
│       └── App.js
└── docker-compose.yml   # Docker Compose configuration


