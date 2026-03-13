# Cloud FinOps Cost Optimization Platform

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

