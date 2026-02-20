from flask import Flask, jsonify

app = Flask(__name__)


#@app.get("/health")
#def health():
#    return jsonify({"health": "OK"})

@app.route("/")
def home():
    return "Dummy service is running!"

if __name__ == "__main__":
    # Bind to 0.0.0.0 so it works in containers too.
    app.run(host="0.0.0.0", port=8000)
