import pandas as pd
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, "data", "cloud_usage.csv")

data = pd.read_csv(csv_path)

def total_cost():
    return int(data["cost"].sum())

def service_costs():
    return data.groupby("service")["cost"].sum().to_dict()

def idle_resources():
    idle = data[data["usage_hours"]<2]
    return idle[["service", "resource_id"]].to_dict(orient="records")

def optimization_recommendations():
    rec = []

    for _, row in data.iterrows():
        if row["usage_hours"]<2:
            rec.append({
                "reosurce": row["resource_id"],
                "recommendation": "consider shutting down or scaling down"
            })

    return rec

def health():
     return {
        "status": "API is running"
     }

def dashboard_summary():
        return {
             "total_cost": total_cost(),
             "services": service_costs(),
             "idle_resources": idle_resources()

        }

