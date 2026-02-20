from flask import Flask, jsonify

app = Flask(__name__)

# original
#@app.get("/health")
#def health():
#    return jsonify({"health": "OK"})

# testno da sem preveril ce deluje docker
#@app.route("/")
#def home():
#    return "Dummy service is running!"

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"health": "OK"}), 200  # 200 je status code

if __name__ == "__main__":
    # Bind to 0.0.0.0 so it works in containers too.
    app.run(host="0.0.0.0", port=8000)


#uspešno deluje:
#HTTP/1.1 200 OK
#Server: Werkzeug/3.1.6 Python/3.12.10
#Date: Fri, 20 Feb 2026 22:56:56 GMT
#Content-Type: application/json
#Content-Length: 16
#Connection: close
#{"health":"OK"}