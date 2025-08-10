# -*- coding: utf-8 -*-
import os
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=os.getenv("ALLOWED_ORIGINS", "*").split(","))


@app.route("/healthz", methods=["GET"])
def healthz():
    return jsonify({"status": "ok"}), 200


@app.route("/summary", methods=["POST"])
def resumen():
    data = request.get_json(force=True, silent=True) or {}
    text = data.get("text", "")
    resumen = text[:400] + "..." if len(text) > 400 else text
    return jsonify({"summary": resumen})


@app.route("/translate", methods=["POST"])
def traducir():
    data = request.get_json(force=True, silent=True) or {}
    text = data.get("text", "")
    to = data.get("to", "en")
    # MOCK: inversión del texto como placeholder.
    traduccion = text[::-1]
    return jsonify({"translated": traduccion, "to": to})


@app.route("/stats", methods=["POST"])
def stats():
    data = request.get_json(force=True, silent=True) or {}
    values = data.get("values", [])
    if not values:
        return jsonify({"error": "No hay datos"}), 400
    arr = np.array(values, dtype=np.float32)
    res = {
        "mean": float(np.mean(arr)),
        "std": float(np.std(arr)),
        "min": float(np.min(arr)),
        "max": float(np.max(arr))
    }
    return jsonify(res)


@app.route("/animate", methods=["POST"])
def animate():
    # Placeholder. Retorna url vacía.
    return jsonify({"url": "", "msg": "Animación no implementada aún."})


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5005"))
    app.run(host="0.0.0.0", port=port, debug=True)
