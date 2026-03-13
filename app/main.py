from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

from app.analyzer import health, dashboard_summary, total_cost, service_costs, idle_resources, optimization_recommendations

app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Cloud FinOps Optimization API"}

@app.get("/", response_class=HTMLResponse)
def dashboard_ui():
    html = Path("dashboard/index.html").read_text()
    return html

@app.get("/total-cost")
def get_total_cost():
    return {"total_cost":total_cost()}

@app.get("/service-costs")
def get_service_costs():
    return service_costs()


@app.get("/idle-resources")
def get_idle_resources():
    return idle_resources()


@app.get("/recommendations")
def get_recommendations():
    return  optimization_recommendations()


@app.get("/dashboard")
def get_dashboard():
    return dashboard_summary()

@app.get("/health")
def get_health():
    return health()




