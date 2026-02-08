# hard-1-insecure-deserialization/app.py
from flask import Flask, request, jsonify
import os, json

app = Flask(__name__)
FLAG = os.environ.get("FLAG", "CTF{dev}")

class Workflow:
    def run(self):
        return "ok"

class InternalAuditWorkflow:
    def run(self):
        return FLAG

@app.route("/")
def index():
    return """
<h2>Workflow Import Service</h2>
<p>Internal automation platform for importing and running workflows.</p>
<ul>
<li>POST /api/workflow/import</li>
<li>GET /health</li>
</ul>
"""

@app.route("/health")
def health():
    return "ok"

@app.route("/api/workflow/import", methods=["POST"])
def import_workflow():
    data = json.loads(request.data.decode())
    t = data.get("type")

    if t == "Workflow":
        w = Workflow()
    elif t == "InternalAuditWorkflow":
        w = InternalAuditWorkflow()
    else:
        return jsonify({"error":"bad"}),400

    return jsonify({"result": w.run()})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
