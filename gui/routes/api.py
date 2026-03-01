from flask import Blueprint, jsonify
from db import get_db

api_routes = Blueprint("api", __name__)

@api_routes.route("/api/events")
def events():
    db = get_db()
    data = db.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    return jsonify([dict(x) for x in data])
