# Cloud FinOps Cost Optimization Platform

## Dashboard Preview

![Cloud FinOps Dashboard](screenshots/dashboard.png)


This project simulates a Cloud FinOps system that analyzes cloud resource usage and identifies cost optimization opportunities.

## Features

- FastAPI backend for cloud cost analytics
- Detect idle cloud resources
- Service-level cost breakdown
- Optimization recommendations
- Docker containerized deployment

## Tech Stack

- Python
- FastAPI
- Pandas
- Docker
- HTML / JavaScript (Dashboard UI)

## API Endpoints

- `/total-cost`
- `/service-costs`
- `/idle-resources`
- `/recommendations`
- `/dashboard`
- `/health`

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload



## Running with Docker

docker build -t cloud-finops .
docker run -p 8000:8000 cloud-finops

Open:
http://localhost:8000


## Architecture

User → Web Dashboard → FastAPI Backend → Cost Analysis Engine → Cloud Usage Dataset


