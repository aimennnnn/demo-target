"""Shop Inventory API."""
import os

import requests
import yaml
from flask import Flask, jsonify

import config

app = Flask(__name__)


def load_stock():
    with open(os.path.join(config.DATA_DIR, "stock.yaml"), encoding="utf-8") as f:
        return yaml.safe_load(f)


@app.route("/stock")
def stock():
    return jsonify(load_stock())


@app.route("/price/<item>")
def price(item):
    response = requests.get(
        f"https://prices.example.com/{item}", headers={"X-API-Key": config.API_KEY}, timeout=15
    )
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(debug=config.DEBUG, port=config.PORT)
