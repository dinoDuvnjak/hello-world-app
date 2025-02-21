# Hello World Kubernetes Deployment

## Overview
A simple "Hello World" web application containerized using Docker and deployed on a local Kubernetes cluster.

## Prerequisites
- **Docker:** Ensure Docker is installed and running on your machine.
- **Python:** Make sure Python is installed.
- **Kubernetes:** Installed and configured on your machine.
- **Minikube:** Installed and running (if using Minikube as your local Kubernetes cluster).

## How to Run Locally

1. **Build the Docker Image:**
   ```bash
   docker build -t hello-world-app:latest .
2. **Run the Docker Image:**
   ```bash
   docker run -p 8080:8080 hello-world-app:latest
3. **Access the application**
   ```bash
   http://localhost:8080/

## Deploy to the Kubernetes Cluster   

1. **Deploy:**
   ```bash
   kubectl apply -f kBs/deployment.yaml
   kubectl apply -f kBs/service.yaml
2. **Access the application**
   ```bash
   http://localhost:30080
   
