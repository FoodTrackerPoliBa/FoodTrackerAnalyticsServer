from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
import logging

from pydantic import BaseModel


app = FastAPI(
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Data(BaseModel):
    user_id: str
    name: str
    parameters: str
    timestamp: int
    appVersion: str

@app.post("/analytics")
def analytics(data: Data):
    table_id = "food-tracker-444411.analytics.data"
    from google.cloud import bigquery
    # Google BigQuery table schema:
    # userId: STRING
    # name: STRING
    # parameters: STRING
    # timestamp: INTEGER

    row = {
        "userId": data.user_id,
        "name": data.name,
        "parameters": data.parameters,
        "timestamp": data.timestamp,
        "appVersion": data.appVersion
    }

    client = bigquery.Client()
    table = client.get_table(table_id)
    errors = client.insert_rows(table, [row])
    if errors:
        raise ValueError(errors)


@app.get("/ping")
def ping():
    return {"ping": "pong!"}


if __name__ == "__main__":
    import uvicorn
    import os
    print("Docs at http://localhost:8080/docs")
    uvicorn.run(app, host='127.0.0.1', port=int(os.environ.get('PORT', 8080)))
    