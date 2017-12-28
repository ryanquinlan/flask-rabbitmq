from flask import Flask, request, jsonify
import json
from config import config
from rabbitmq import rabbitmq

cfg = config().generate()

app = Flask(__name__)

def _response(message, status="ok"):
    return jsonify({"status": status, "message": message})

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return ":D"

    else:
        if request.get_json() is None:
            return _response("Invalid POST data","error"), 400

        else:
            json_data = request.get_json()

            if "message" not in json_data.keys():
                return _response("Missing key 'message'", "error"), 400

            routing_key = cfg["RabbitMQ"]["routing_key"]
            message = json_data["message"]

            rabbit = rabbitmq()
            rabbit.send_message(message, routing_key)
            rabbit.close()

            return _response("Message accepted successfully")

if __name__ == "__main__":
    app.run(debug=True)
