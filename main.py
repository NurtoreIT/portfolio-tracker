from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Portfolio Tracker")

# Пока храним данные в памяти. Базу данных добавим позже.
assets = []


class Asset(BaseModel):
    ticker: str
    quantity: float
    buy_price: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/assets")
def add_asset(asset: Asset):
    assets.append(asset)
    return asset


@app.get("/assets")
def list_assets():
    return assets